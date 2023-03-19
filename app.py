from flask import Flask, render_template,jsonify


app = Flask(__name__)

#create list of open positions
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location':'Irvington, New Jersey',
    'salary': '$80,000'
  },
  {
      'id':2,
    'title': 'Data Scientist',
    'location':'Irvington, New Jersey',
    'salary': '$110,000'
  },
  {
      'id': 3,
    'title': 'Software Engineer',
    'location':'Remote',
    'salary': '$130,000'
  },
  {
    'id':4,
    'title': 'Project Manager',
    'location':'Irvington, New Jersey',
    'salary': '$95,000'
  }
    
]

@app.route("/")

def jovian_career():
  return render_template('home.html',jobs = JOBS, company_name = 'Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)
