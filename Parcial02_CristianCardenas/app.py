from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>')
def factorial(num):
    try:
        result = math.factorial(num)
        message = f"El factorial de {num} es: {result}"
    except ValueError:
        message = "El número debe ser un entero positivo."

    return render_template('factorial.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)