## 🧠 Teaching: Cyber Concepts Behind Phase 1
Here’s what you’re actually learning (and demonstrating) in Phase 1:

### 🔨 PHASE 1: Base Framework for CNAPP-lite
* Set up a modular project structure
* Create a simulated AWS environment (with moto)
* Build an S3 scanner
* Export results in frontend-compatible JSON
* Add a Dockerfile for easy local execution



||Concept|What It Means|Why It Matters||
|---|---|---|---|---|
|| `S3 (Simple Storage Service)` | AWS’s cloud storage — like folders in the cloud   | Misconfigured buckets can expose sensitive data||
|| `ACL (Access Control List)`   | Old-school permission model on S3 buckets| Allows public access if not configured carefully||
|| `Public buckets`| Buckets readable by “everyone” on the internet| Often the source of data breaches (e.g., Verizon 2017)||
|| `moto`| Python library that mocks AWS services| Lets you simulate AWS environments without a real cloud account ||
|| `boto3`| Official AWS Python SDK| You’ll use this to talk to real AWS later||
|| `Risk Findings`| Identified vulnerabilities or misconfigurations| Help prioritize what to fix first||
|| `JSON Reports`| Machine-readable output that can be shown in a UI | Makes the results visual and reusable||
|| `MITRE ATT&CK mapping`| Security tactics and techniques| Adds professionalism and clarity to each finding||
|| `Docker`| Lightweight containers to run apps consistently| Makes deployment easy anywhere later (cloud, laptops, CI/CD)||
