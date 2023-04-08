from flask import Flask, render_template, request, jsonify
import chatgpt_api_example

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    input_prompt = request.form['input_prompt']
    response_text = chatgpt_api_example.generate_response(input_prompt)
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
