from flask import Flask
import random

app = Flask(__name__)

# print(__name__)


random_number = random.randint(0, 9)
print(random_number)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


@app.route("/")
def index():
    # random_number = random.randint(0, 9)
    # print(random_number)
    return "<h1> Guess a number between 0 and 9</h1>" \
           "<img src = 'https://media4.giphy.com/media/v1" \
           ".Y2lkPTc5MGI3NjExbXBwNG94MGZqOWd6NnVwdnJ2c3k0cmVpM212Z3Y3cGwxN3NjZGptZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQm" \
           "Y3Q9Zw/xRCASav6bgz9m/giphy.webp' width=400>"


@app.route("/<int:guess>")
def check_guess(guess):
    if guess < random_number:
        return "<h1>Too Low, try again!</h1>" \
               "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width = 400>"
    elif guess > random_number:
        return "<h1>Too High, try again!</h1>" \
               "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width = 400>"
    else:
        return "<h1>You found me!</h1>" \
               "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width = 400>"
    # if guess == random_number:
    #     result = "Congratulations! You guessed the correct number."
    # else:
    #     result = f"Sorry, the correct number was {random_number}. Try again!"
    # return f"<h1 style='text-align: center'>{result}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
