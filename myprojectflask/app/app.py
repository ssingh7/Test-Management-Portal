from flask import Flask, render_template,request,redirect,url_for
from jenkinsapi.jenkins import Jenkins
import requests
import json
import time
from main.TestPython import Classone

class Application:    
    testcaseDuration = 0
    app = Flask(__name__)
    @app.route('/send', methods=['GET', 'POST'])
    def dashboard():
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
        
    @app.route('/age')
    def age():
        counter = Classone().testMethod2()
        chromeRequest = requests.get('http://10.2.162.80:9090/job/ChromeJob/lastBuild/api/json').text
        chromeRequest = json.loads(chromeRequest)
        firefoxRequest = requests.get('http://10.2.162.80:9090/job/FirefoxJob/lastBuild/api/json').text
        firefoxRequest = json.loads(firefoxRequest)
        abc = firefoxRequest.get('building')
        edgeRequest = requests.get('http://10.2.162.80:9090/job/edgejob/lastBuild/api/json').text
        edgeRequest = json.loads(edgeRequest)
        ieRequest = requests.get('http://10.2.162.80:9090/job/iejob/lastBuild/api/json').text
        ieRequest = json.loads(ieRequest)
        return render_template('age2.html',env=counter,chromeOption=chromeRequest.get('building'), firefoxOption=firefoxRequest.get('building'), ieOption=ieRequest.get('building'), edgeOption=edgeRequest.get('building'))    
    
application = Application()
application.app.run()
