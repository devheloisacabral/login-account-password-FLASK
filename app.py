from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina():
    return render_template('index.html')

@app.route('/senha')
def senha():
    return render_template('senha.html')

@app.route('/conta')
def conta():
    return render_template('conta.html')

if __name__ == '__main__':
    app.run(debug=True)