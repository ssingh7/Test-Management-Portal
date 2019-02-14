import time
from flask import Flask, render_template,request,redirect,url_for
from jenkinsapi.jenkins import Jenkins
import requests
import json

app = Flask(__name__)
class Classone(object):
    count=0
    def showDashboardPage(self):
        print('TestMethod1 :',self.count)
        self.count = self.count+4

        print('TestMethod1 :',self.count)
        
    def testMethod2(self):
        Classone.count+=5
        print('Counter is :',Classone.count)
        return Classone.count
        
class Classtwo(object):
    count=0
    def testMethod1(self):
        self.count = self.count+4
        for i in range(10):
            time.sleep(1)
            print('Iteration :',i)
        print('TestMethod1 :',self.count)
        
    def testMethod2(self):
        self.count = self.count+2
        print('TestMethod2 :',self.count)


@app.route('/age')
def age():
    chromeRequest = requests.get('http://10.2.162.80:9090/job/ChromeJob/lastBuild/api/json').text
    chromeRequest = json.loads(chromeRequest)
    firefoxRequest = requests.get('http://10.2.162.80:9090/job/FirefoxJob/lastBuild/api/json').text
    firefoxRequest = json.loads(firefoxRequest)
    abc = firefoxRequest.get('building')
    edgeRequest = requests.get('http://10.2.162.80:9090/job/edgejob/lastBuild/api/json').text
    edgeRequest = json.loads(edgeRequest)
    ieRequest = requests.get('http://10.2.162.80:9090/job/iejob/lastBuild/api/json').text
    ieRequest = json.loads(ieRequest)
    return render_template('age2.html',env="abc",chromeOption=chromeRequest.get('building'), firefoxOption=firefoxRequest.get('building'), ieOption=ieRequest.get('building'), edgeOption=edgeRequest.get('building'))