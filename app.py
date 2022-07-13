from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/taewoo')
def taewoo():

    con = sql.connect("database.db")
    cur = con.cursor()
    cur.row_factory = sql.Row
    cur.execute("SELECT * FROM portfolio WHERE name=\"김태우\"")
    rows = cur.fetchall()
    return render_template('taewoo.html', rows=rows)


@app.route('/seokju')
def seokju():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.row_factory = sql.Row
    cur.execute("SELECT * FROM portfolio WHERE name=\"김석주\"")
    rows = cur.fetchall()
    return render_template('seokju.html', rows=rows)


@app.route('/mod')
def new_student():
    return render_template('modify.html')


@app.route('/mod_tae')
def modify_taewoo():

    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM portfolio WHERE name=\"김태우\"")
    rows = cur.fetchall()

    return render_template('modify.html', rows=rows)


@app.route('/mod_seok')
def modify_seokju():

    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM portfolio WHERE name=\"김석주\"")
    rows = cur.fetchall()

    return render_template('modify.html', rows=rows)


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:

            git = request.form['git']
            info = request.form['info']
            name = request.form['name']

            con = sql.connect('database.db')

            cur = con.cursor()

            cur.execute(
                "update portfolio SET info = ?, git = ? where name= ? ", (info, git, name))

            con.commit()
            mesg = "Record successfully added"
            con.close()
        except:
            con.rollback()
            mesg = "error in insert operation"

        finally:
            return render_template("sqlite_result.html", mesg=mesg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("select * from portfolio ")

    rows = cur.fetchall()
    return render_template("sqlite_list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
