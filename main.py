from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Main")
def home():
    return render_template("home.html")

@app.route("/Upload_Data")
def upload_data():
    return render_template("upload_data.html")

@app.route("/Match_Student")
def match_student():
    return render_template("match_student.html")

@app.route("/Prepare_Email")
def prepare_email():
    return render_template("prepare_email.html")

@app.route("/Settings")
def settings():
    return render_template("settings.html")

if __name__ == '__main__':
    #host is to set the localhost IP Address, port is to set the port
    app.run(host = '127.0.0.1', port ='5221', debug = True)
