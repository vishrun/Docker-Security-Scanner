def rule_avoid_latest(line, line_number):
    if line.startswith("FROM") and ":latest" in line.lower():
        return "Avoid using ':latest' tag"
    return None

def rule_root_user(line, line_number):
    if line.startswith("USER") and "root" in line.lower():
        return "Running container as root is risky"
    return None

def rule_add_instruction(line, line_number):
    if line.startswith("ADD "):
        return "Use COPY instead of ADD"
    return None

def rule_privileged_port(line, line_number):
    if line.startswith("EXPOSE"):
        for port in line.split()[1:]:
            try:
                if int(port) < 1024:
                    return "Exposing privileged port (<1024)"
            except ValueError:
                pass
    return None

def rule_version_finding(line, line_number):
    if not line.startswith("FROM"):
        return None

    image = line.split()[1]
    if ":" not in image:
        return f"{image}:missing"
    return image

RULES = [
    rule_avoid_latest,
    rule_root_user,
    rule_add_instruction,
    rule_privileged_port,
    rule_version_finding
]
