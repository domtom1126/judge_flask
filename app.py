from flask import Flask , render_template, request
import sqlite3 as sql

app = Flask(__name__)



@app.route('/')
def home():
   return  render_template('home.html')

@app.route('/judge_return', methods=['POST', 'GET'])
def judge_return(judge=None, statute=None):
      # index.html, name=judge_name 
   judge = request.form['judge_name']
   statute = request.form['statute']
   con = sql.connect('judge.db')
   c = con.cursor()
   total_cases_for_judge =  c.execute("SELECT judge_total FROM judge_statute_total WHERE judge=? AND statute=?",(judge,statute))
   display_judge_total = total_cases_for_judge.fetchall()
   total_cases_for_database = c.execute("SELECT stat_totals FROM judge_statute_total WHERE judge=? AND statute=?",(judge,statute))
   display_total_cases_for_database = total_cases_for_database.fetchone()   
   return render_template('judge_return.html',display_judge_total=display_judge_total, display_total_cases_for_database=display_total_cases_for_database,judge=judge, statute=statute)
    
