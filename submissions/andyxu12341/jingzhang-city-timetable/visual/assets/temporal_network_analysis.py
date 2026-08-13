#!/usr/bin/env python3
"""
Scenario-based time-expanded accessibility proof for JINGZHANG TIME RIGHTS.

This script intentionally uses conceptual design geometry and explicit schedule assumptions.
It does NOT claim observed field performance. Replace nodes, demand weights and schedule
windows with official / surveyed data before empirical use.
"""
import math, json
from pathlib import Path
import numpy as np
import networkx as nx

HERE = Path(__file__).resolve().parent
model = json.loads((HERE / "temporal_network.json").read_text(encoding="utf-8"))

nodes = {n["id"]:(n["lon"],n["lat"],n["key_area"],n["type"]) for n in model["nodes"]}
baseline = {k:[tuple(x) for x in v] for k,v in model["baseline_windows"].items()}
timerights = {k:[tuple(x) for x in v] for k,v in model["time_rights_windows"].items()}

def haversine_m(a,b):
    lon1,lat1=a[:2]; lon2,lat2=b[:2]; R=6371000
    p1,p2=math.radians(lat1),math.radians(lat2)
    dp=math.radians(lat2-lat1); dl=math.radians(lon2-lon1)
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))

def demand(h):
    if 0<=h<5:return .10
    if 5<=h<7:return .30
    if 7<=h<9:return 1.00
    if 9<=h<12:return .80
    if 12<=h<17:return .70
    if 17<=h<21:return 1.00
    return .60

def active(node,h,windows):
    return any(s<=h<e for s,e in windows.get(node,[]))

G=nx.Graph()
for n,v in nodes.items(): G.add_node(n,area=v[2],typ=v[3])
names=list(nodes)
for i,a in enumerate(names):
    for b in names[i+1:]:
        if nodes[a][2]!=nodes[b][2]: continue
        d=haversine_m(nodes[a],nodes[b])
        if d<=650: G.add_edge(a,b,walk_min=d/75)
local_edges=[(a,b,d["walk_min"]) for a,b,d in G.edges(data=True)]

def build_time_graph():
    TG=nx.DiGraph()
    for q in range(96):
        for n in nodes: TG.add_node((n,q))
    for q in range(95):
        for n in nodes: TG.add_edge((n,q),(n,q+1),minutes=15)
        for a,b,walk in local_edges:
            k=max(1,math.ceil(walk/15))
            if q+k<96:
                TG.add_edge((a,q),(b,q+k),minutes=k*15)
                TG.add_edge((b,q),(a,q+k),minutes=k*15)
    return TG

TG=build_time_graph()

def run(windows):
    peak_q=[q for q in range(96) if demand(q/4)>=.8]
    flex=["ZZ_TEST","OR_DEMO","DZ_LIFE"]
    conflict=0.0; avail=0.0; total=0.0; reach=[]
    for q in peak_q:
        h=q/4
        for f in flex:
            total += .25
            if active(f,h,windows): conflict += .25
            else: avail += .25
        for n in nodes:
            lengths=nx.single_source_dijkstra_path_length(TG,(n,q),cutoff=30,weight="minutes")
            reached=set()
            for (j,qq),mins in lengths.items():
                if nodes[j][2]!=nodes[n][2]: continue
                if not active(j,qq/4,windows): reached.add(j)
            reach.append(len(reached))
    machine=sum((e-s) for v in windows.values() for s,e in v)
    return {"machine_hours":machine,"peak_conflict_hours":conflict,
            "peak_flexible_availability":avail/total,
            "mean_30min_peak_reachability":float(np.mean(reach))}

b=run(baseline); t=run(timerights)
out={
 "model_id":"TIME-RIGHTS-PROOF-001",
 "baseline":b, "time_rights":t,
 "derived":{
   "peak_conflict_reduction_ratio":1-t["peak_conflict_hours"]/b["peak_conflict_hours"],
   "peak_flexible_availability_gain_pp":(t["peak_flexible_availability"]-b["peak_flexible_availability"])*100,
   "temporal_reachability_gain_ratio":t["mean_30min_peak_reachability"]/b["mean_30min_peak_reachability"]-1
 },
 "interpretation":"Scenario-based proof-of-method; not observed operational performance."
}
print(json.dumps(out,ensure_ascii=False,indent=2))
