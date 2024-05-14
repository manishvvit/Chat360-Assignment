from flask import Flask, request, jsonify, send_from_directory, render_template_string
import subprocess
import sys
import os

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html') as f:
        return render_template_string(f.read())

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('', path)

@app.route('/generate_logs', methods=['POST'])
def generate_logs():
    num_logs = int(request.form['num_logs'])
    result = subprocess.run([sys.executable, 'log_generator.py', str(num_logs)], capture_output=True, text=True)
    if result.returncode == 0:
        return jsonify({'status': 'success', 'output': result.stdout})
    else:
        return jsonify({'status': 'error', 'output': result.stderr})

if __name__ == "__main__":
    app.run(debug=True)
