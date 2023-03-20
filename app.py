from flask import Flask, render_template
from database import jobsload, jobload
from markupsafe import escape

app = Flask(__name__)
companyName = "Sairam's"




@app.route('/')
def About_Me():
  jobs = jobsload()
  return render_template('home.html', jobs=jobs, companyname = companyName)

@app.route('/job/<int:id>')
def jobapply(id):
  job = jobload(id)
  if job!=None:
    return render_template('jobApply.html', job=job)
  else:
    return "NOT FOUND : 404"

  

if(__name__)=="__main__":
  app.run("0.0.0.0",debug = True)