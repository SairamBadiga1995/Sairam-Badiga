from flask import Flask, render_template

app = Flask(__name__)
companyName = "Sairam's"
JOBS = [
        {
          'id':1,
          'title': 'Data Analyst',
          'location':'Bangalore, India',
          'salary': 'Rs 1000000'    
        },
        {
          'id':2,
          'title': 'Data Scientist',
          'location':'Delhi, India',
          'salary': 'Rs 1000000'    
        },
        {
          'id':3,
          'title': 'Data Engineer',
          'location':'Remote',
          'salary': 'Rs 1000000'    
        },
        {
          'id':4,
          'title': 'Frontend Engineer',
          'location':'San fransico, usa',
          'salary': '$ 100000'    
        },
]

@app.route('/')
def About_Me():
  return render_template('home.html', jobs=JOBS, companyname = companyName)

if(__name__)=="__main__":
  app.run("0.0.0.0",debug = True)