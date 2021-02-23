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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['eq1']
        lastName = details['eq2']
        cur = mysql.connection.cursor()
        cur.execute("use scrap;")
        cur.execute("SELECT Nom, Date_num, Time FROM Matchs WHERE Equipe1 LIKE %s OR Equipe2 LIKE %s;", (firstName, lastName))
        result = cur.fetchall()
        cur.close()
        return jsonify(result)
    return render_template('about.html')

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5200, debug=True)