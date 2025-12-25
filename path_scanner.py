from pathlib import Path
from dockerfile_scanner import scan_dockerfile
from compose_scanner import scan_dockercompose

IGNORE_DIRS = {
    ".git", ".venv", "venv", "__pycache__", "node_modules"
}

def scan_path(root_path: str, report):
    root = Path(root_path)

    for file in root.rglob("*"):
        if not file.is_file():
            continue

        if any(part in IGNORE_DIRS for part in file.parts):
            continue

        name = file.name.lower()

        if name.startswith("dockerfile"):
            scan_dockerfile(str(file), report)

        elif name in {"docker-compose.yml", "docker-compose.yaml"}:
            scan_dockercompose(str(file), report)
