from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_operation():
    token = request.headers.get('Authorization')
    if token != 'your_secret_token':
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.json
    with open('logs/operations.log', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()} - {data}\n")
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
