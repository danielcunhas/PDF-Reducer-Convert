from flask import Flask, request, jsonify, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>pdftotext_service UP!</p>"

@app.route('/convert', methods=['POST'])
def convert_pdf_to_txt():
    print('Request received in convert')
    file = request.files['file']
    filename = file.filename
    file.save(filename)
    
    output_filename = filename.replace('.pdf', '.txt')
    subprocess.run(['pdftotext', filename, output_filename])
    
    return jsonify({'file_url': f'/download/{output_filename}'})

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
