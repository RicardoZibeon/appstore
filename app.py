from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)

@app.route('/about')
def about():
    current_year = datetime.datetime.now().year
    return render_template("about.html", year=current_year)

@app.route('/contact')
def contact():
    current_year = datetime.datetime.now().year
    return render_template("contact.html", year=current_year)


@app.route('/sale')
def sale():
    current_year = datetime.datetime.now().year
    return render_template("sale.html", year=current_year)



if __name__ == "__main__":
    app.run(debug=True)
