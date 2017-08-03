from flask import (Flask, render_template, request, url_for, app)
from flaskext.mysql import MySQL
app = Flask(__name__)
app.debug = True
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Lavina@123456'
app.config['MYSQL_DATABASE_DB'] = 'sys'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def main():
    return render_template('launch_page.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from users where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

if __name__ == "__main__":
    app.run()
