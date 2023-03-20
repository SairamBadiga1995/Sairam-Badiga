from sqlalchemy import create_engine, text


import os
 
url = os.environ['CONNECTIONSTRING']


engine = create_engine(url,connect_args={
                      "ssl":{
                          "ssl_ca":"/etc/ssl/cert.pem"  
                      }
                        
                      })




def jobsload():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = result.all()
    # for job in result.all():
    #   jobs.append(dict(job))
    return jobs

def jobload(id):
  with engine.connect() as conn:
    if id ==1:
      command = text('SELECT * FROM jobs WHERE id=1')
    elif id ==2:
      command = text('SELECT * FROM jobs WHERE id=2')
    elif id ==3:
      command = text('SELECT * FROM jobs WHERE id=3')
    elif id ==4:
      command = text('SELECT * FROM jobs WHERE id=4')
    else:
      return None
    result= conn.execute(command)
    job = result.all()
    if len(job)>0:
      return job
    else:
      return None

r = jobload(1)
print(len(r))
print(r[0][1])
print(type(r))

