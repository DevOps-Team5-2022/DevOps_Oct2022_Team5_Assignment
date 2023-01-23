from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Main")

def hello_world():
    return render_template("home.html")

if __name__ == '__main__':
    #host is to set the localhost IP Address, port is to set the port
    app.run(host = '127.0.0.1', port ='5221', debug = True)
