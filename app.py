from flask import Flask , render_template, request
import sqlite3 as sql

app = Flask(__name__)



@app.route('/')
def home():
   return  render_template('home.html')

@app.route('/judge_return', methods=['POST', 'GET'])
def judge_return():
      # index.html, name=judge_name 
   judge = request.form['judge_name']
   con = sql.connect('judge.db')
   c = con.cursor()
   c.execute("SELECT * FROM judge_statute_total WHERE judge = (?)", (judge))
   con.commit()
   display = c.fetchall()
   return render_template('judge_return.html', display=display)
    
