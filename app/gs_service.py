from flask import Flask, request, jsonify, send_file
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>gs_service UP!</p>"

@app.route('/reduce', methods=['POST'])
def reduce_resolution():
    print('Request received in Reduce')
    file = request.files['file']
    resolution = request.form['resolution']
    filename = file.filename
    file.save(filename)
    
    output_filename = f"reduced_{filename}"
    subprocess.run(['gs', '-sDEVICE=pdfwrite', f'-dPDFSETTINGS=/{resolution}', '-dNOPAUSE', '-dBATCH', f'-sOutputFile={output_filename}', filename])
    
    return jsonify({'file_url': f'/download/{output_filename}'})

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
