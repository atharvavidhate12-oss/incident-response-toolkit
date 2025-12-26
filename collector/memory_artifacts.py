import psutil

def collect_memory_artifacts():
    return {
        "total_memory": psutil.virtual_memory().total,
        "used_memory": psutil.virtual_memory().used,
        "top_processes": [
            (p.info['name'], p.info['memory_info'].rss)
            for p in psutil.process_iter(['name', 'memory_info'])
            if p.info['memory_info']
        ][:10]
    }
