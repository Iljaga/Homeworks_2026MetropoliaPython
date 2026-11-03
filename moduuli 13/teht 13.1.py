
from flask import Flask, jsonify

app = Flask(__name__)

# Alkuluvun tarkistusfunktio
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Flask-reitti
@app.route('/alkuluku/<int:number>', methods=['GET'])
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }

    return jsonify(result)


# Käynnistetään palvelin portissa 3000
if __name__ == '__main__':
    app.run(port=3000)
