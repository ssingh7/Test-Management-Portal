import requests
import jenkinsapi
from jenkinsapi.jenkins import Jenkins
class Utility(object):
    
    def postRequest(self,url,headers,data):
        response = requests.post(url)
        return request
        
    def getRequest(self,url,headers,data):
        response = requests.get(url)
        return response
    
    def buildJob(self,baseUrl,jobName,parameter=None):
        job = Jenkins(baseUrl)
        job.build_job(jobname, params)
    
    def populateDashboard(self):
        if request.method == 'POST':
            job = Jenkins('http://10.2.162.80:9090')
            env = request.form.get('sel1')
            chromeChecked = request.form.get("chrome") != None            
            firefoxChecked = request.form.get("firefox") != None
            ieChecked = request.form.get("ie") != None
            edgeChecked = request.form.get("edge") != None
            
            if chromeChecked :
                job.build_job('ChromeJob')
            if firefoxChecked :
                job.build_job('FirefoxJob')
            if edgeChecked :
                job.build_job('EdgeJob')
            if ieChecked :
                job.build_job('IEJob')
    
            return redirect(url_for('age')) 
    
                       
        return render_template('index.html')       