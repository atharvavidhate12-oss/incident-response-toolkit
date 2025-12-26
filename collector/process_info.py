import psutil

def collect_processes():
    processes = []
    for p in psutil.process_iter(['pid', 'name', 'username']):
        processes.append(p.info)
    return processes
