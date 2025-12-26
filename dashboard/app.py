from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Get path relative to script location, not current working directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_path = os.path.join(script_dir, "..", "data", "analysis", "results.json")
    results_path = os.path.normpath(results_path)
    
    if not os.path.exists(results_path):
        return "Results file not found. Please run main.py first.", 404
    
    with open(results_path) as f:
        data = json.load(f)
    return render_template("index.html", data=data)

app.run(debug=True)
