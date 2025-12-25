from pathlib import Path
from rules.dockerfile_rules import RULES
from grype_runner import run_grype
from report_writer import write_section, write_line

def scan_dockerfile(filepath: str, report):
    dockerfile = Path(filepath)

    write_section(report, f"Dockerfile Scan: {filepath}")

    try:
        content = dockerfile.read_text(
            encoding="utf-8",
            errors="replace"
        )
    except Exception as e:
        write_line(report, f"ERROR: Cannot read file ({e})")
        return

    lines = content.splitlines()
    findings = []
    images = []

    for i, raw in enumerate(lines, start=1):
        line = raw.strip()

        if not line or line.startswith("#"):
            continue

        for rule in RULES:
            result = rule(line, i)

            if isinstance(result, str):
                findings.append((i, result, line))

            if line.startswith("FROM") and isinstance(result, str):
                images.append(result)

    if not findings:
        write_line(report, "No Dockerfile issues found")
    else:
        for ln, msg, code in findings:
            write_line(report, f"[Line {ln}] {msg} | {code}")

    if images:
        print("Running Grype scan")
        run_grype(images, report)
        print("Grype scan completed")