from flask import Flask, render_template, request
import sqlite3

app = Flask(
    __name__,
    template_folder="templates", static_folder="static", static_url_path=''
)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("lovers.sqlite")
    except sqlite3.error as e:
        print(e)
    return e

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        uname = request.form['username']
        pword = request.form['password']
        conn = sqlite3.connect('lovers.sqlite')
        c = conn.cursor()
        if uname == "sadsingle":
            statement = f"SELECT * FROM lovers WHERE uname='{uname}' AND pword='{pword}';"  
            c.execute(statement)
            if not c.fetchone():
                return "Incorrect password"
            else:
                return render_template("/you_did_the_thing.html")
        else:
            return "Incorrect username or password"
    else: 
        return render_template("index.html")   

#dwWegotYou
@app.route("/ilookinteresting")
def wow():
    return render_template("wow.html") 

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
