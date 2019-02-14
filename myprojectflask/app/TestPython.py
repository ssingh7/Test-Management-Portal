import time
import os
from jenkinsapi.jenkins import Jenkins
import requests
import json
class Classone(object):
    count=0
    def testMethod1(self):

        for i in range(30):
            time.sleep(5)
            print(os.environ['JOB_NAME'])
            payload = {
  "Job Name": str(os.environ['JOB_NAME']),
  "Total Executed": 30,
  "Total Pass": i,
  "Total Fail": 0,
  "Total Execution Time": 2,
  "Last Report Path": "\\\\172.30.205.179\\Old Reports\\BuildNumber92\\ie\\Tests_ie_5_33_28 AM.html",
  "Test Cases": [
    {
      "Name": "Verify Error message when Feedback form is Submitted with all empty fields in 200x promo site",
      "Status": "Passed"
    },
    {
      "Name": "Verify Error message when Feedback form is Submitted with all empty fields in MPJ promo site",
      "Status": "Passed"
    },
    {
      "Name": "Verify Error message when Feedback form is Submitted with all empty fields in WPT promo site",
      "Status": "Passed"
    },
    {
      "Name": "Verify Error message when Feedback form is Submitted with all empty fields in WWGT promo site",
      "Status": "Passed"
    },
    {
      "Name": "Verify Error message when Feedback form is Submitted with Blank Comments in 200x promo site",
      "Status": "Passed"
    },
    {
      "Name": "Verify Error message when Feedback form is Submitted with Blank Comments in Mass Lottery site ",
      "Status": "Passed"
    }
  ]
}
            payload = json.dumps(payload)
            headers = {
                'content-type': "application/json",
            }

            response = requests.request("POST", "http://10.2.162.80:5000/api/v1/addresult", data=payload, headers=headers)
            print('Iteration :', i)
        
    def testMethod2(self):
        self.count = self.count+2
        print('TestMethod2 :',self.count)
        
class Classtwo(object):
    count=0
    def testMethod1(self):
        response = requests.get('http://10.2.162.80:9090//job/{0}/lastBuild/api/json'.format(os.environ['JOB_NAME']))
        response = json.loads(response.text)
        data = {
            "Job Name": os.environ['JOB_NAME'],
            "Total Executed": 26,
            "Total Pass": 26,
            "Total Fail": 0,
            "Total Execution Time": 4,
            "Job Status": response['building']}
        
    def testMethod2(self):
        self.count = self.count+2
        print('TestMethod2 :',self.count)


testPython = Classone()
testPython.testMethod1()