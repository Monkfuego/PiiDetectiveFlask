from flask import Flask, request, jsonify
from pii_detective import pii_detect_layer1, pii_detect_layer2
import os
import tempfile

app = Flask(__name__)

def detector_main(file):
    ext = os.path.splitext(file.filename)[1].lower()
    
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as temp_file:
        file.save(temp_file.name)
        temp_file_path = temp_file.name
    
    if ext in ['.jpg', '.jpeg', '.png']:
        result = pii_detect_layer2(temp_file_path)
    elif ext in ['.txt', '.docx', '.pdf', '.html', '.htm', '.csv', '.xml', '.json', '.xlsx']:
        result = pii_detect_layer1(temp_file_path) + pii_detect_layer2(temp_file_path)
    else:
        result = f"Unsupported file extension: {ext}"
    
    # Clean up the temp file
    os.remove(temp_file_path)
    
    return result

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        output = detector_main(file)
        return jsonify({'output': output}), 200

if __name__ == '__main__':
    app.run(debug=True)
