def rule_latest_image(service, config):
    image = config.get("image", "")
    if ":latest" in image:
        return (service, "Avoid using :latest image tag")

def rule_privileged(service, config):
    if config.get("privileged") is True:
        return (service, "Privileged container detected")

def rule_host_network(service, config):
    if config.get("network_mode") == "host":
        return (service, "Host network mode detected")

def rule_no_limits(service, config):
    has_swarm_limits = (
        "deploy" in config and
        "resources" in config["deploy"] and
        "limits" in config["deploy"]["resources"]
    )

    has_local_limits = (
        "mem_limit" in config or
        "cpus" in config
    )

    if not has_swarm_limits and not has_local_limits:
        return (service, "No CPU/memory limits defined")

RULES = [
    rule_latest_image,
    rule_privileged,
    rule_host_network,
    rule_no_limits
]
