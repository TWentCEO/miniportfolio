from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('./index.html')

@app.route('/mod')
def new_student():
   return render_template('modify.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:

            git = request.form['git']
            portfolio_text = request.form['portfolio_text']
            about_me = request.form['about_me']
         
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (git,portfolio_text,about_me) VALUES (?,?,?,?)",(git,portfolio_text,about_me) )
            
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
      
        finally:
            return render_template("sqlite_result.html")
            con.close()


if __name__ == '__main__':
    app.run(debug=True)