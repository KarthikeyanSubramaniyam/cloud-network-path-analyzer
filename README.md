# Cloud Network Ingress & Path Exposure Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Security-Defensive_Auditor-blue?style=flat" alt="Type">
  <img src="https://img.shields.io/badge/Status-Architectural_Showcase-success?style=flat" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
</p>

> 🔒 **Technical Showcase & Architecture Specification**  
> *This repository provides public architectural documentation, system specifications, and implementation summaries. Full production source code, internal test suites, and proprietary algorithms are maintained in a secure private repository.*

---

## 📌 Executive Summary

**Category**: Network Security & Cloud Architecture  
**Tech Stack**: `Python 3.10+ · VPC Networking · Security Groups · Path Analysis`  

Defensive analyzer evaluating VPC routing tables, Internet Gateways, and Security Groups to detect unintended public network exposure paths.

---

## 🎯 The Problem It Solves

Complex VPC peering, routing tables, and layered security group rules can accidentally expose internal administrative interfaces (SSH, RDP, databases) to the entire public internet (`0.0.0.0/0`).

---

## ⚙️ How the Engine Works

1. **Topology Graph Construction**: Builds a connectivity model linking subnets, Route Tables, Internet Gateways (IGW), and NAT Gateways.
2. **Security Group Matrix Evaluation**: Parses inbound and outbound Security Group and NACL rules, resolving CIDR blocks and port ranges.
3. **Ingress Reachability Calculation**: Evaluates whether an internal resource sits in a public subnet with a direct route to an IGW and an open ingress rule.
4. **Critical Service Detection**: Flags unrestricted public exposure on administrative and database ports (22, 3389, 3306, 5432, 27017, 6379).
5. **Remediation Plan**: Emits precise Least-Privilege CIDR tightening recommendations and Security Group diffs.

---

## 🚀 Key Capabilities

- Detects 0.0.0.0/0 open ingress on sensitive ports
- Traces route table internet paths to distinguish truly public vs private subnets
- Identifies overly permissive inter-subnet Security Group configurations
- Provides automated remediation rules for Network Access Control Lists

---

## 🏗️ System Data Flow & Architecture

```
+-----------------------------------+
|  Target Input / Configuration    |
|  (JSON Snapshots / Policies)      |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  1. Schema Normalization Engine   |
|  Validates types & formats        |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  2. Core Analytical Pipeline      |
|  Heuristic rule evaluation,       |
|  invariant checks & drift diffs   |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  3. Risk Classification           |
|  Assigns severity: INFO / HIGH    |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  4. Structured Findings & Report  |
|  Root cause, evidence &           |
|  actionable remediation steps     |
+-----------------------------------+
```

---

## 📄 Findings Output Structure

The engine generates structured, machine-parsable JSON reports adhering to this standard audit schema:

```json
{
  "results": [
    {
      "resource": "resource-identifier",
      "severity": "HIGH",
      "check": "CHECK_IDENTIFIER",
      "detail": "Descriptive analysis of the identified security posture issue.",
      "remediation": "Actionable step-by-step guidance to restore compliant state.",
      "evidence": {
        "observed_field": "value",
        "required_policy": "enforced_policy"
      }
    }
  ],
  "count": 1,
  "scope": "Comprehensive defensive security audit"
}
```

---

## 🔒 Source Code & Enterprise Inquiries

To protect proprietary intellectual property and client operational security:
* **Public Repository**: Contains comprehensive architecture specifications, schemas, and design overviews.
* **Private Repository**: Contains the complete production implementation, continuous integration pipelines, and full regression test suites.

For architectural questions or enterprise inquiries, connect via [LinkedIn](https://www.linkedin.com/in/karthikeyansubramaniam04/) or visit the [Portfolio Site](https://karthikeyansubramaniyam.github.io).
