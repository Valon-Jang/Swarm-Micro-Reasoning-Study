#!/usr/bin/env python3
"""Scale 6-10 paired benchmark v1.1.0.

Extends the calibrated v0.9 / scale-5 v1.0 benchmark without changing cases,
scoring, partitioning, routing, node budget, or timing method. Adds paired
2D/3D structures from 6 through 10 so scaling can be studied under one fixed
benchmark contract.

Important: this is a deterministic swarm reasoning scaffold, not a Qwen model.
"""
from __future__ import annotations
import argparse, json, statistics, hashlib
import swarm_fair_scale_v0_8 as base
import swarm_calibrated_L1_L5_v0_9 as cal

VERSION = "1.1.0"
SIZES = list(range(2,11))
VARIANTS = ["reference_1"]
for n in range(6,11):
    VARIANTS += [f"grid_{n}x{n}", f"cube_{n}x{n}x{n}"]

cal.VARIANTS = VARIANTS
base.VARIANTS = VARIANTS


def expected_count(name:str)->int:
    if name=="reference_1": return 1
    if name.startswith("grid_"):
        n=int(name.split('_')[1].split('x')[0]); return n*n
    n=int(name.split('_')[1].split('x')[0]); return n*n*n


def self_test()->dict:
    checks=[]
    checks.append(("25_calibrated_cases", len(cal.RUBRICS)==25 and all(k in base.CASES for k in cal.RUBRICS)))
    checks.append(("five_difficulty_levels", set(base.CASES[k]["difficulty"] for k in cal.RUBRICS)=={1,2,3,4,5}))
    for name in VARIANTS:
        t=base.topology(name); count=expected_count(name)
        checks.append((f"{name}_count",len(t["nodes"])==count))
        checks.append((f"{name}_neighbor_symmetry",all(n in t["neighbors"][m] for n,ns in t["neighbors"].items() for m in ns)))
        checks.append((f"{name}_readout_exists",t["readout"] in t["nodes"]))
    sample=base.CASES["L5_noise1200_versioned"]
    atoms=base.flatten_input(sample["full_input"])
    target=sorted(base.compact(a) for a in atoms)
    for n in range(6,11):
        for name in (f"grid_{n}x{n}",f"cube_{n}x{n}x{n}"):
            parts=base.partition_atoms(sample,base.topology(name))
            flat=sorted(base.compact(a) for xs in parts.values() for a in xs)
            checks.append((f"{name}_lossless_partition",flat==target))
    checks.append(("negative_delete_readonly",base.classify_risk(base.CASES["L2_negative_delete"]["task"],base.CASES["L2_negative_delete"]["full_input"])["risk_level"]=="read_only"))
    checks.append(("quoted_side_effect_readonly",base.classify_risk(base.CASES["L4_quoted_side_effect"]["task"],base.CASES["L4_quoted_side_effect"]["full_input"])["risk_level"]=="read_only"))
    return {"ok":all(v for _,v in checks),"version":VERSION,"total":len(checks),"passed":[k for k,v in checks if v],"failed":[k for k,v in checks if not v]}


def hard_avg(summary,name):
    return round(statistics.mean(summary[name]["by_difficulty"][f"L{i}"]["avg_score"] for i in (3,4,5)),2)


def run(repeats:int=3)->dict:
    out=cal.run(repeats)
    out["version"]=VERSION
    out["variants"]=VARIANTS
    out["pairs_added"]=[n for n in range(6,11)]
    s=out["summary"]
    ref=s["reference_1"]
    scale=[]
    for n in range(6,11):
        for shape,name in (("grid",f"grid_{n}x{n}"),("cube",f"cube_{n}x{n}x{n}")):
            x=s[name]
            scale.append({
                "size":n,"shape":shape,"topology":name,"node_count":x["node_count"],
                "avg_score":x["avg_score"],"hard_L3_L5":hard_avg(s,name),
                "L5":x["by_difficulty"]["L5"]["avg_score"],
                "median_ms":x["median_ms"],"p95_ms":x["p95_ms"],"avg_messages":x["avg_messages"],
                "hard_failure_runs":x["hard_failure_runs"],
                "delta_overall_vs_reference":round(x["avg_score"]-ref["avg_score"],2),
                "delta_hard_vs_reference":round(hard_avg(s,name)-hard_avg(s,"reference_1"),2),
                "speed_ratio_vs_reference":round(x["median_ms"]/max(ref["median_ms"],1e-9),2),
            })
    all_clean=all(s[t]["hard_failure_runs"]==0 for t in VARIANTS)
    best_hard=max(VARIANTS,key=lambda t:hard_avg(s,t))
    ref_h=hard_avg(s,"reference_1"); best_h=hard_avg(s,best_hard)
    maturity=4.5
    if all_clean and best_h >= ref_h+3.0: maturity=5.0
    out["scale_table"]=scale
    out["best_hard_topology"]=best_hard
    out["hard_level_average"]={t:hard_avg(s,t) for t in VARIANTS}
    out["maturity_level_10"]=maturity
    out["scaling_conclusion"]={
        "all_hard_gates_clean":all_clean,
        "reference_hard_L3_L5":ref_h,
        "best_hard_L3_L5":best_h,
        "best_hard_delta":round(best_h-ref_h,2),
        "level5_gate_delta_required":3.0,
        "level5_gate_pass":all_clean and best_h>=ref_h+3.0,
    }
    return out


def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--self-test",action="store_true"); ap.add_argument("--repeat",type=int,default=3); ap.add_argument("--pretty",action="store_true"); a=ap.parse_args()
    out=self_test() if a.self_test else run(max(1,a.repeat))
    print(json.dumps(out,ensure_ascii=False,indent=2 if a.pretty else None))
    return 0 if out.get("ok") else 1

if __name__=="__main__": raise SystemExit(main())
