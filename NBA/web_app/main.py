
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template
from processing import do_calculation
from datetime import date

app = Flask(__name__)


@app.route('/')
def hello_world():
	today = date.today().strftime('%m-%d-%y')
	return render_template('homepage.html', date=today)


@app.route('/add', methods=["GET", "POST"])
def add():
	errors = ""
	if request.method == "POST":
		number1 = None
		number2 = None
		try:
			number1 = float(request.form["number1"])
		except ValueError:
			errors += "{!r} is not a number.\n".format(request.form["number1"])
		try:
			number2 = float(request.form["number2"])
		except ValueError:
			errors += "{!r} is not a number.\n".format(request.form["number2"])

		if number1 is not None and number2 is not None:
			result = do_calculation(number1, number2)
			return render_template('results.html', result=result)

	return render_template('add.html', errors=errors)


if __name__ == '__main__':
	app.run()
