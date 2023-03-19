from flask import Flask, render_template
from database import jobsload

app = Flask(__name__)
companyName = "Sairam's"




@app.route('/')
def About_Me():
  jobs = jobsload()
  return render_template('home.html', jobs=jobs, companyname = companyName)

if(__name__)=="__main__":
  app.run("0.0.0.0",debug = True)