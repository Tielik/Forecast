from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        country = request.form;
        print(country)
        return render_template('index.html', country=country)
    return render_template('chooseCity.html')


if __name__ == '__main__':
    app.run(debug=True)