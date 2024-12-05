from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def generate_file():
    def generate():
        chunk_size = 1024 * 1024
        total_size = 1 * 1024 * 1024 * 1024 * 1024
        sent = 0
        
        while sent < total_size:
            yield b'0' * chunk_size
            sent += chunk_size

    return Response(generate(), mimetype='application/octet-stream', headers={
        "Content-Disposition": "attachment; filename=Ultimate_Answers_Studienkolleg_1TB.zip"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5500)
