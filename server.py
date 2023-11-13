from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', fila=4, columna=4,color1='red',color2='black')

@app.route ('/<int:x>')
def x_filas(x):
    return render_template("index.html", fila=x, columna=4,color1='red',color2='black')

@app.route ('/<int:x>/<int:y>')
def xy_filas(x,y):
    return render_template("index.html", fila=x, columna=y,color1='red',color2='black')

@app.route ('/<int:x>/<int:y>/<string:color_1>/<string:color_2>')
def cambio_color(x,y,color_1,color_2):
    return render_template("index.html", fila=x, columna=y,color1=color_1,color2=color_2)


if __name__=="__main__":
    app.run(debug=True)