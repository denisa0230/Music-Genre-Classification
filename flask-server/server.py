from flask import Flask, render_template, request, jsonify
import os
import classify

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

# Home page
@app.route('/')
def index():
    return render_template('home.html')

# Personalized result page
@app.route('/result/<genre>')
def result(genre):

    return render_template('result.html', genre=genre)

# Save song and render the evaluation template
@app.route('/evaluate', methods=['POST'])
def evaluate():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
        
    if not os.path.isdir(app.config['UPLOAD_FOLDER']):
        os.mkdir(app.config['UPLOAD_FOLDER'])
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return render_template("evaluate.html", file_path=file_path)

   

# Process file and transmit results
@app.route('/process_file', methods=['POST'])
def process_file():
    data = request.json
    file_path = data.get('file_path', '')  # Extract the file_path from the JSON data
    
    # Run the model
    result = classify.find_genre(file_path)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)