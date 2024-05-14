from flask import Flask, request, jsonify
import datetime
import re
import random
import uuid

app = Flask(__name__)

# In-memory log storage
logs = []

# Helper functions
def generate_random_log():
    def get_random_log_message():
        messages = [
            "Application started successfully.",
            "Request received and processing initiated.",
            "Task completed successfully.",
            "User logged in.",
            "Disk space running low.",
            "Unusual activity detected.",
            "Invalid input received.",
            "Configuration file not found.",
            "Database connection failed.",
            "File not found.",
            "Unexpected server error.",
            "Authentication failed.",
            "Entering function X.",
            "Value of variable Y: 42.",
            "Debugging information for troubleshooting.",
            "API request received: /api/v1/resource.",
            "Security violation detected.",
            "Unauthorized access attempt.",
            "SSL/TLS handshake failed.",
            "Invalid token received.",
            "User A modified record B.",
            "Configuration settings updated.",
            "Access control list changed.",
            "Critical operation performed.",
            "Database query execution time: 50ms.",
            "Memory usage exceeds threshold.",
            "High CPU usage detected.",
            "Slow response time for request.",
            "Network connection established.",
            "DNS resolution failed.",
            "Packet loss detected.",
            "Firewall rule updated.",
            "External service unreachable.",
            "Dependency version mismatch.",
            "Library X not found.",
            "Failed to connect to third-party API.",
            "Order placed successfully.",
            "Message sent to queue.",
            "Workflow step completed.",
            "Sensor data received."
        ]
        return random.choice(messages)

    def get_random_timestamp():
        start_date = datetime.datetime.strptime("2023-09-10T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
        end_date = datetime.datetime.utcnow()
        time_difference = end_date - start_date
        random_days_offset = random.uniform(0, time_difference.days)
        timestamp = (start_date + datetime.timedelta(days=random_days_offset)).replace(microsecond=0).isoformat() + 'Z'
        return timestamp

    def get_random_level():
        log_levels = ['info', 'warning', 'error']
        return random.choice(log_levels)

    def get_id(n=6):
        return str(uuid.uuid4())[:n]

    metadata = {
        'parentResourceId': get_id()
    }
    log = {
        'level': get_random_level(),
        'message': get_random_log_message(),
        'resourceId': f'server-{random.randint(1000, 9999)}',
        'timestamp': get_random_timestamp(),
        'traceId': get_id(),
        'spanId': get_id(),
        'commit': get_id(),
        'metadata': metadata
    }
    return log

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/generate_logs', methods=['POST'])
def generate_logs():
    num_logs = int(request.form.get('num_logs'))
    generated_logs = [generate_random_log() for _ in range(num_logs)]
    logs.extend(generated_logs)
    return jsonify(generated_logs)

@app.route('/search_logs', methods=['GET'])
def search_logs():
    level = request.args.get('level')
    message = request.args.get('message')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    filtered_logs = logs
    
    if level:
        filtered_logs = [log for log in filtered_logs if log['level'] == level]
    
    if message:
        pattern = re.compile(message)
        filtered_logs = [log for log in filtered_logs if pattern.search(log['message'])]
    
    if start_date:
        start_date = datetime.datetime.fromisoformat(start_date)
        filtered_logs = [log for log in filtered_logs if datetime.datetime.fromisoformat(log['timestamp']) >= start_date]
    
    if end_date:
        end_date = datetime.datetime.fromisoformat(end_date)
        filtered_logs = [log for log in filtered_logs if datetime.datetime.fromisoformat(log['timestamp']) <= end_date]
    
    return jsonify(filtered_logs)

if __name__ == "__main__":
    app.run(debug=True)
