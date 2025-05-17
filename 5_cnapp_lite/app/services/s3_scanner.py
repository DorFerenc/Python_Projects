# S3-specific misconfiguration checks
def scan_s3_buckets(s3_client):
    findings = []

    response = s3_client.list_buckets()
    for bucket in response.get('Buckets', []):
        bucket_name = bucket['Name']
        acl = s3_client.get_bucket_acl(Bucket=bucket_name)

        is_public = any(grant.get('Grantee', {}).get('URI') ==
                        'http://acs.amazonaws.com/groups/global/AllUsers'
                        for grant in acl.get('Grants', []))

        finding = {
            'resource_type': 'S3',
            'bucket_name': bucket_name,
            'public': is_public,
            'risk_level': 'High' if is_public else 'None',
            'misconfiguration_type': 'Public S3 Bucket' if is_public else None,
            'recommendation': 'Remove public access' if is_public else None
        }
        findings.append(finding)

    return findings
