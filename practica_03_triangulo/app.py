from flask import Flask, render_template, request

app = Flask(__name__)

# Esta es la ruta principal de nuestra página web del triángulo
@app.route('/', methods=['GET', 'POST'])
def triangulo():
    # Empezamos con los resultados vacíos (en None)
    resultado_area = None
    resultado_perimetro = None
    
    # Si el usuario presionó el botón de "Calcular" en la página
    if request.method == 'POST':
        # 1 Guardamos lo que el usuario escribió en las cajas de texto
        # Usamos float() para que acepte números con punto decimal
        base_ingresada = float(request.form['caja_base'])
        altura_ingresada = float(request.form['caja_altura'])
        lado1_ingresado = float(request.form['caja_lado1'])
        lado2_ingresado = float(request.form['caja_lado2'])
        lado3_ingresado = float(request.form['caja_lado3'])
        
        # 2 Aplicamos las fórmulas matemáticas básicas que nos enseñaron
        resultado_area = (base_ingresada * altura_ingresada) / 2
        resultado_perimetro = lado1_ingresado + lado2_ingresado + lado3_ingresado
        
    # 3 Le mandamos los resultados de vuelta a la página de HTML
    return render_template('triangulo.html', area=resultado_area, perimetro=resultado_perimetro)

if __name__ == '__main__':
    app.run(debug=True)