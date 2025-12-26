import os
from pathlib import Path

try:
    import yara  # type: ignore[import-untyped]
    YARA_AVAILABLE = True
except ImportError:
    YARA_AVAILABLE = False
    yara = None

def scan_with_yara(directory_path):
    """
    Scan files in the given directory using YARA rules.
    
    Args:
        directory_path: Path to directory to scan
        
    Returns:
        Dictionary containing scan results with file path and matches
    """
    if not YARA_AVAILABLE:
        return {
            "error": "yara-python module not available. Install Microsoft Visual C++ Build Tools and run: pip install yara-python",
            "matches": [],
            "scanned_files": 0
        }
    
    # Path to YARA rules directory
    rules_dir = Path(__file__).parent.parent / "yara_rules"
    
    try:
        # Compile all YARA rules
        rules = {}
        for rule_file in rules_dir.glob("*.yar"):
            rules[rule_file.stem] = yara.compile(str(rule_file))
        
        if not rules:
            return {"error": "No YARA rules found", "matches": []}
        
        # Scan files in the directory
        scanned_files = 0
        matches_found = []
        
        for root, dirs, files in os.walk(directory_path):
            # Skip virtual environment and other common directories
            dirs[:] = [d for d in dirs if d not in ['venv', '__pycache__', '.git', 'node_modules']]
            
            for file in files:
                file_path = os.path.join(root, file)
                
                # Skip binary files and large files (optional optimization)
                if file_path.endswith(('.exe', '.dll', '.so', '.pyd')) or os.path.getsize(file_path) > 10 * 1024 * 1024:  # 10MB limit
                    continue
                
                try:
                    # Match against all rules
                    for rule_name, rule in rules.items():
                        rule_matches = rule.match(file_path)
                        if rule_matches:
                            matches_found.append({
                                "file": file_path,
                                "rule": rule_name,
                                "matches": [str(match) for match in rule_matches]
                            })
                    scanned_files += 1
                except Exception as e:
                    # Skip files that can't be scanned (permissions, encoding issues, etc.)
                    continue
        
        return {
            "scanned_files": scanned_files,
            "matches": matches_found
        }
        
    except Exception as e:
        if YARA_AVAILABLE and yara and hasattr(yara, 'Error') and isinstance(e, yara.Error):
            return {"error": f"YARA compilation error: {str(e)}", "matches": [], "scanned_files": 0}
        return {"error": f"Scan error: {str(e)}", "matches": [], "scanned_files": 0}

