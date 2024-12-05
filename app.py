from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/antworten/download')
def generate_file():
    def generate():
        chunk_size = 1024 * 1024
        total_size = 10 * 1024 * 1024 * 1024 * 1024
        sent = 0
        
        while sent < total_size:
            yield b'0' * chunk_size
            sent += chunk_size

    total_size = 10 * 1024 * 1024 * 1024 * 1024
    return Response(generate(), mimetype='application/octet-stream', headers={
        "Content-Disposition": "attachment; filename=Ultimate_Answers_Studienkolleg_1TB.zip", "Content-Length": str(total_size),
    })

if __name__ == '__main__':
    app.run(debug=True, port=5500)
