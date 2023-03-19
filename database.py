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