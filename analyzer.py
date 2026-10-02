"""Correlate normalized IPv4 routes, public IPs and security group ingress."""

import ipaddress

def analyze(data):
    out = []
    for asset in data.get("assets", []):
        internet_route = any(r.get("cidr") == "0.0.0.0/0" and str(r.get("gateway", "")).startswith("igw-") and r.get("state", "active") == "active" for r in asset.get("routes", []))
        if not asset.get("public_ip") or not internet_route:
            continue
        for rule in asset.get("ingress", []):
            if ipaddress.ip_network(rule["cidr"], strict=False).prefixlen != 0:
                continue
            out.append(finding(asset["id"], "HIGH", "CANDIDATE_INTERNET_PATH", "Public IP, active Internet Gateway default route and public ingress coexist. NACL, host firewall and service state are not evaluated.", "Restrict ingress sources or remove unnecessary public addressing.", {"public_ip": asset["public_ip"], "rule": rule}))
    return out

import argparse
import json
import sys
from pathlib import Path

def finding(resource, severity, check, detail, remediation, evidence):
    return dict(resource=resource, severity=severity, check=check, detail=detail, remediation=remediation, evidence=evidence)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--output", type=Path)
    p.add_argument("--fail-on-high", action="store_true")
    args = p.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        if not isinstance(data, dict):
            raise ValueError("Expected JSON object")
        results = analyze(data)
        text = json.dumps({"results": results, "count": len(results), "scope": __doc__}, indent=2)
        if args.output:
            args.output.write_text(text + "\n", encoding="utf-8")
        else:
            print(text)
        return int(args.fail_on_high and any(r["severity"] == "HIGH" for r in results))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as e:
        print(f"Input/report error: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())

