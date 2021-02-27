from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_mysql_connector import MySQL
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pw'
app.config['MYSQL_DB'] = 'scrap'

mysql = MySQL(app)

@app.route('/home', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        equipe = request.form['eq1']
        d1 = request.form['d1']
        d2 = request.form['d2']
        if request.form['eq1'] == "":
            return redirect(url_for('Date', d1=d1, d2=d2))
        else:
            return redirect(url_for('Team', equipe=equipe))
    else:
        return render_template('home.html')

@app.route('/Date/<d1>/<d2>', methods=['GET', 'POST'])
def Date(d1, d2):
    cur = mysql.connection.cursor()
    cur.execute("use scrap;")
    cur.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs_t WHERE Date(Date_num)>=Date(%s) AND Date(Date_num)<=Date(%s);", (d1, d2))
    result = cur.fetchall()
    return render_template("equipe.html", result=result)

@app.route('/Equipe/<equipe>', methods=['GET', 'POST'])
def Team(equipe):
    cur = mysql.connection.cursor()
    cur.execute("use scrap;")
    cur.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs_t WHERE Equipe1 LIKE %s OR Equipe2 LIKE %s;", (equipe, equipe))
    result = cur.fetchall()
    return render_template("equipe.html", result=result)


if __name__== "__main__":
    app.run(host="0.0.0.0", port=5200, debug=True)