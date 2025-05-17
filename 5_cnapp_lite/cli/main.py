# Entry point to run the scan
from app.data.sample_env import setup_mock_s3_environment
from app.core.aws_connector import get_s3_client
from app.services.s3_scanner import scan_s3_buckets
from app.interface.json_interface import generate_report

def main():
    print("[*] Setting up simulated environment...")
    mock = setup_mock_s3_environment()

    print("[*] Connecting to fake AWS...")
    s3_client = get_s3_client()

    print("[*] Scanning S3 buckets...")
    s3_findings = scan_s3_buckets(s3_client)

    print("[*] Generating report...")
    generate_report(s3_findings)

    print("[*] Done.")

    mock.stop()

if __name__ == "__main__":
    main()
