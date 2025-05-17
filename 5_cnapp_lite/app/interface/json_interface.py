 # Creates output compatible with frontendimport json
from datetime import datetime

def generate_report(s3_findings):
    report = {
        "projectID": "proj-cnapp-lite-001",
        "details": {
            "color": "blue",
            "type": "cloud",
            "name": "CNAPP-lite Scan",
            "team": "Student"
        },
        "assets": [],
        "alerts": []
    }

    for f in s3_findings:
        report["assets"].append({
            "ip": "N/A",
            "name": f["bucket_name"],
            "memory": "N/A",
            "category": "storage",
            "type": "S3 Bucket"
        })

        if f["risk_level"] == "High":
            report["alerts"].append({
                "ip": "N/A",
                "port": 443,
                "host": f["bucket_name"],
                "alert_name": f["misconfiguration_type"],
                "mitre_tactic": "Initial Access",
                "mitre_technique": "Expose Storage to Internet (T1530)",
                "time": datetime.utcnow().isoformat() + "Z"
            })

    with open("scan_result.json", "w") as f:
        json.dump(report, f, indent=4)

    print("[+] Report written to scan_result.json")
