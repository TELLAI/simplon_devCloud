from flask import Flask, render_template, request
from flask_mysql_connector import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'ms2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pw'
app.config['MYSQL_DB'] = 'scrap'
app.config['AUTH_PLUGIN'] = 'mysql_native_password'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        equipe1 = details['eq1']
        equipe2 = details['eq2']
        cur = mysql.connection.cursor()
        cur.execute("use scrap;")
        cur.execute("SELECT * FROM Matchs WHERE Equipe1=(%s) AND Equipe2=(%s);", (equipe1, equipe2))
        result = cur.fetchall()
        cur.close()
    return render_template('.html', data = result)

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5200, debug=True)