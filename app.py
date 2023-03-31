from flask import Flask
from flask import render_template
from flask import send_file

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/eventbridge")
def eventbridge():
    return render_template("eventbridge.html")


@app.route("/pipeline")
def pipeline():
    return render_template("pipeline.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route('/download')
def download_file():
    path = './samples/sample_dashboard_devgua.pdf'
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run()
