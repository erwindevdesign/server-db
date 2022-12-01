from flask import Flask, request, url_for, redirect, abort, render_template

app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = 'root',
    database = 'prueba'
)

cursor = mydb.cursor(dictionary=True)

@app.route('/')
def index():
    return '<h1>:: Successful ::</h1>'

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def second(post_id):
    if request.method == 'GET':
        return':: Successful :: El id del metodo POST es: ' + post_id
    else:
        return 'El methodo solicitado no es == GET'

@app.route('/third', methods=['POST', 'GET'])  
def third():
    cursor.execute('SELECT * FROM usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    # abort(401)
    # return redirect(url_for('second', post_id=2))
    # print(request.form)
    # print(request.form['key1'])
    # print(request.form['key2']) 
    # return render_template('index.html')

    # return{
    #     "username": 'Lola',
    #     "email": 'lola@latrailera.com'
    # }

    return render_template('index.html', usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hi bitch!')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        username = request.form['full_name']
        email = request.form['email']
        age = request.form['birth_day']
        sql = "INSERT INTO usuario (full_name, email, birth_day) values (%s, %s, %s)"
        values = (username, email, age)
        cursor.execute(sql, values)
        mydb.commit()
        
        return redirect(url_for('third'))
    return render_template('create.html')

if __name__=='__main__':
    app.run(debug=True)