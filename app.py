from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/quienessomos") 
def quienes():
    return render_template("quienessomos.html")

@app.route("/servicios") 
def servicios():
    return render_template("servicios.html")

@app.route("/noticias") 
def noticias():
    return render_template("noticias.html")

@app.route('/contactos', methods=['GET', 'POST'])
def contactos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        return redirect('/')
    return render_template('contactos.html')

if __name__ == "__main__":
    app.run(debug=True)