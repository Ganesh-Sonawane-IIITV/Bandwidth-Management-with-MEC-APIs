from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/manage_bandwidth', methods=['POST'])
def manage_bandwidth():
    data = request.json
    device = data.get('device')  # Network interface (e.g., eth0)
    bandwidth = data.get('bandwidth')  # Bandwidth limit (e.g., 1mbit)

    try:
        # Apply bandwidth limits using `tc` (traffic control)
        os.system(f"sudo tc qdisc add dev {device} root tbf rate {bandwidth} burst 32kbit latency 400ms")
        return jsonify({"message": f"Bandwidth set to {bandwidth} for {device}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
