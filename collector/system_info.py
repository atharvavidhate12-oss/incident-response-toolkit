import platform
import json

def collect_system_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "hostname": platform.node(),
        "architecture": platform.machine()
    }
