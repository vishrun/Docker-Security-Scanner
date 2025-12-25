import yaml
from rules.compose_rules import RULES
from grype_runner import run_grype
from report_writer import write_section, write_line

def scan_dockercompose(filepath: str, report):
    write_section(report, f"Docker Compose Scan: {filepath}")

    try:
        with open(filepath, encoding="utf-8", errors="replace") as f:
            compose = yaml.safe_load(f)
    except Exception as e:
        write_line(report, f"ERROR: Cannot read compose file ({e})")
        return

    services = compose.get("services", {})
    findings = []
    images = []

    for service, config in services.items():
        for rule in RULES:
            result = rule(service, config)
            if result:
                findings.append(result)

        if "image" in config:
            images.append(config["image"])

    if not findings:
        write_line(report, "No Docker Compose issues found")
    else:
        for svc, msg in findings:
            write_line(report, f"[Service {svc}] {msg}")

    if images:
        print("Running Grype scan")
        run_grype(images, report)
        print("Grype scan completed")
