from flask import Flask, request, redirect, url_for, render_template
import psycopg2 as pg

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello</h1>"

@app.route("/<nam>")
def welcome(nam):
    return f"<h1>Welcome {nam}</h1>"

@app.route("/login" , methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        
        conn = pg.connect(database = 'login')
        cur = conn.cursor()
        cur.execute("insert into details(name,password) values (%s,%s)", (name, password))
        conn.commit()
        cur.close()
        conn.close()
        
        return redirect(url_for('login'))
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
