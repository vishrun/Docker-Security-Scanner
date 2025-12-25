import subprocess
from report_writer import write_section, write_line
GRYPE_PATH = r"C:\Tools\Grype\grype.exe"

def run_grype(images, report):
    write_section(report, "Grype Vulnerability Scan")

    for img in set(images):
        write_line(report, f"Scanning image: {img}")

        process = subprocess.run(
            [GRYPE_PATH, img, "-o", "json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        write_line(report, process.stdout)
