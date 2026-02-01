import flask

app = flask.Flask(__name__)

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.get("/prime_number/<int:number>")
def is_prime_handler(number: int):
    number_is_prime = is_prime(number)
    return {"number":number, "isPrime": number_is_prime}


if __name__ == "__main__":
    app.run("0.0.0.0", 3000)
