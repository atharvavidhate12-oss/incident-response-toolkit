import psutil

def collect_network():
    conns = []
    for c in psutil.net_connections(kind='inet'):
        conns.append({
            "local": f"{c.laddr.ip}:{c.laddr.port}" if c.laddr else "",
            "remote": f"{c.raddr.ip}:{c.raddr.port}" if c.raddr else "",
            "status": c.status
        })
    return conns
