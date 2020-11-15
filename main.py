from flask import Flask, request

app = Flask(__name__)

INDEX = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Imagine number between 0 and 1000</h1>
<form action="" method="POST">

I will try to guess it in max. 10 attempts. 
<p>If You are ready press the button.</p>
    <input type="hidden" name="min" value="{}">
    <input type="hidden" name="max" value="{}">
    <input type="submit" value="START">
</form>
</body>
</html>
'''

MAIN_GAME = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
    <title>Guess The Number</title>
</head>
<body>
<h1>It is number {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="too big">
    <input type="submit" name="user_answer" value="too small">
    <input type="submit" name="user_answer" value="you win">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</form>
</body>
</html>
'''

RESULT = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Hurray! I guess! Your number is {guess}</h1>

</body>
</html>'''


@app.route("/", methods=['GET', 'POST'])
def guess_the_number():
    if request.method == 'GET':
        return INDEX.format(0, 1000)
    else:
        minimum = int(request.form.get("min"))
        maximum = int(request.form.get("max"))
        answer = request.form.get('user_answer')
        guess = int(request.form.get('guess', 500))

        if answer == "too big":
            maximum = guess
        elif answer == "too small":
            minimum = guess
        elif answer == "you win":
            return RESULT.format(guess=guess)

        guess = int((maximum - minimum) / 2) + minimum

        return MAIN_GAME.format(guess=guess, min=minimum, max=maximum)


if __name__ == '__main__':
    app.run(debug=True)
