from flask import Flask, render_template, request, jsonify
from flask_mysql_connector import MySQL
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pw'
app.config['MYSQL_DB'] = 'scrap'

mysql = MySQL(app)

# @app.route('/')
# def index():
#     return render_template('index.html')
@app.route('/Equipe')
def Team():
    eq1 = request.args.get("equipe")
    cur = mysql.connection.cursor()
    cur.execute("use scrap;")
    cur.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs WHERE Equipe1 LIKE %s OR Equipe2 LIKE %s;", (eq1, eq1))
    result = cur.fetchall()
    cur.close()
    return jsonify(result)

@app.route('/Date')
def Date():
    d1 = request.args.get("date1")
    d2 = request.args.get("date2")
    cur = mysql.connection.cursor()
    cur.execute("use scrap;")
    cur.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs WHERE Date(Date_num)>=Date(%s) AND Date(Date_num)<=Date(%s);", (d1, d2))
    date = cur.fetchall()
    cur.close()
    return jsonify(date)

@app.route('/Affiche')
def Affiche():
    list_equipe = ["Real Madrid", "Barcelone", "Liverpool", "Atlético", "Chelsea", "Manchester C.", "Manchester U.", "Milan", "Leceister", "Marseille OM", "Lyon OL", "Naples", "Tottenham", "Inter", "Arsenal", "Paris PSG", "Dortmund", "Bayern", "Benfica", "Juventus"]
    req = "SELECT Nom, Date_text, Time, Chaine FROM Matchs WHERE Equipe1 in ("
    for ii, i in enumerate(list_equipe):
        if ii == len(list_equipe) - 1:
            req = req + "'" + i + "') AND Equipe2 in ("
        else:
            req = req + "'" + i + "', "
    for jj, j in enumerate(list_equipe):
        if jj == len(list_equipe) - 1:
            req = req + "'" + j + "');"
        else:
            req = req + "'" + j + "', "
    
    cur = mysql.connection.cursor()
    cur.execute("use scrap;")
    cur.execute(req)
    affiche = cur.fetchall()
    cur.close()
    return jsonify(affiche)


if __name__== "__main__":
    app.run(host="localhost", port=5200, debug=True)