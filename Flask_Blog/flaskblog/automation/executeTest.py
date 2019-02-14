from flaskblog import app
from jenkinsapi.jenkins import Jenkins

def run_jenkins_job(job_name):
    job = Jenkins('http://172.30.205.179:9090')
    #job = Jenkins('http://10.2.162.80:9090')
    job.build_job(job_name)

def get_job_status(job_name):
    job = Jenkins('http://172.30.205.179:9090')
    #job = Jenkins('http://10.2.162.80:9090')
    return job.get_job(job_name).get_last_build().get_status()