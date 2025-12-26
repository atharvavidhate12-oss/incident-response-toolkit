import hashlib
import os

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def collect_file_hashes(directory):
    artifacts = {}
    for root, _, files in os.walk(directory):
        for f in files:
            full = os.path.join(root, f)
            try:
                artifacts[full] = hash_file(full)
            except:
                pass
    return artifacts
