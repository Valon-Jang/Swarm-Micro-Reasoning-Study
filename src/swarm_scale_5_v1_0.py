#!/usr/bin/env python3
"""Scale-5 paired benchmark v1.0.0.

Extends calibrated v0.9 without changing the L1-L5 cases, scoring rubric,
partitioning, node engine, message budget, or timing method.
Adds only grid_5x5 and cube_5x5x5 so the 5-structure pair is evaluated on
exactly the same benchmark as all earlier topologies.
"""
from __future__ import annotations
import argparse, json, statistics
import swarm_fair_scale_v0_8 as base
import swarm_calibrated_L1_L5_v0_9 as cal

VERSION = "1.0.0"
VARIANTS = [
    "reference_1",
    "grid_2x2", "cube_2x2x2",
    "grid_3x3", "cube_3x3x3",
    "grid_4x4", "cube_4x4x4",
    "grid_5x5", "cube_5x5x5",
]

cal.VARIANTS = VARIANTS
base.VARIANTS = VARIANTS


def self_test() -> dict:
    checks=[]
    checks.append(("25_calibrated_cases", len(cal.RUBRICS)==25 and all(k in base.CASES for k in cal.RUBRICS)))
    checks.append(("five_difficulty_levels", set(base.CASES[k]["difficulty"] for k in cal.RUBRICS)=={1,2,3,4,5}))
    expected_counts={
        "reference_1":1,
        "grid_2x2":4,"cube_2x2x2":8,
        "grid_3x3":9,"cube_3x3x3":27,
        "grid_4x4":16,"cube_4x4x4":64,
        "grid_5x5":25,"cube_5x5x5":125,
    }
    for name,count in expected_counts.items():
        t=base.topology(name)
        checks.append((f"{name}_count",len(t["nodes"])==count))
        checks.append((f"{name}_neighbor_symmetry",all(n in t["neighbors"][m] for n,ns in t["neighbors"].items() for m in ns)))
        checks.append((f"{name}_readout_exists",t["readout"] in t["nodes"]))
    sample=base.CASES["L5_noise1200_versioned"]
    atoms=base.flatten_input(sample["full_input"])
    target=sorted(base.compact(a) for a in atoms)
    for name in ("grid_5x5","cube_5x5x5"):
        parts=base.partition_atoms(sample,base.topology(name))
        flat=sorted(base.compact(a) for xs in parts.values() for a in xs)
        checks.append((f"{name}_lossless_partition",flat==target))
    checks.append(("negative_delete_readonly",base.classify_risk(base.CASES["L2_negative_delete"]["task"],base.CASES["L2_negative_delete"]["full_input"])["risk_level"]=="read_only"))
    checks.append(("quoted_side_effect_readonly",base.classify_risk(base.CASES["L4_quoted_side_effect"]["task"],base.CASES["L4_quoted_side_effect"]["full_input"])["risk_level"]=="read_only"))
    return {"ok":all(v for _,v in checks),"version":VERSION,"total":len(checks),"passed":[k for k,v in checks if v],"failed":[k for k,v in checks if not v]}


def run(repeats:int=7) -> dict:
    out=cal.run(repeats)
    out["version"]=VERSION
    out["variants"]=VARIANTS
    out["pair_added"]=["grid_5x5","cube_5x5x5"]
    s=out["summary"]
    def hard_avg(name):
        return round(statistics.mean(s[name]["by_difficulty"][f"L{i}"]["avg_score"] for i in (3,4,5)),2)
    ref=s["reference_1"]
    g=s["grid_5x5"]; c=s["cube_5x5x5"]
    out["scale5_assessment"]={
        "grid_5x5":{
            "delta_overall_vs_reference":round(g["avg_score"]-ref["avg_score"],2),
            "delta_hard_L3_L5_vs_reference":round(hard_avg("grid_5x5")-hard_avg("reference_1"),2),
            "speed_ratio_vs_reference":round(g["median_ms"]/max(ref["median_ms"],1e-9),2),
            "message_ratio_vs_grid_4x4":round(g["avg_messages"]/max(s["grid_4x4"]["avg_messages"],1e-9),2),
        },
        "cube_5x5x5":{
            "delta_overall_vs_reference":round(c["avg_score"]-ref["avg_score"],2),
            "delta_hard_L3_L5_vs_reference":round(hard_avg("cube_5x5x5")-hard_avg("reference_1"),2),
            "speed_ratio_vs_reference":round(c["median_ms"]/max(ref["median_ms"],1e-9),2),
            "message_ratio_vs_cube_4x4x4":round(c["avg_messages"]/max(s["cube_4x4x4"]["avg_messages"],1e-9),2),
        },
    }
    best_hard_name=max(VARIANTS,key=hard_avg)
    best_hard=hard_avg(best_hard_name); ref_h=hard_avg("reference_1")
    maturity=4.5
    if best_hard >= ref_h+3.0 and all(s[t]["hard_failure_runs"]==0 for t in VARIANTS): maturity=5.0
    out["best_hard_topology"]=best_hard_name
    out["hard_level_average"]={t:hard_avg(t) for t in VARIANTS}
    out["maturity_level_10"]=maturity
    return out


def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--self-test",action="store_true"); ap.add_argument("--benchmark",action="store_true"); ap.add_argument("--repeat",type=int,default=7); ap.add_argument("--pretty",action="store_true"); a=ap.parse_args()
    out=self_test() if a.self_test else run(max(1,a.repeat))
    print(json.dumps(out,ensure_ascii=False,indent=2 if a.pretty else None))
    return 0 if out.get("ok") else 1

if __name__=="__main__": raise SystemExit(main())
