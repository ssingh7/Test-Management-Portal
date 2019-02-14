from flask import Blueprint
from flask import render_template, url_for, redirect, request,jsonify,send_file
from flaskblog.automation.forms import PlatformSelectionForm
from flaskblog.automation.executeTest import run_jenkins_job,get_job_status
from flaskblog.models import Result
from flaskblog import db
from flask_login import login_required,current_user
import sqlite3
import sys
import json
from urllib.parse import urljoin
from urllib.request import pathname2url

automation = Blueprint('automation',__name__)


@automation.route("/choose",methods=['GET', 'POST'])
@login_required
def choose_test_platform():
    form = PlatformSelectionForm()
    jobs = []
    if form.validate_on_submit():
        if form.chrome_checkbox.data : jobs.append('ChromeJob')
        if form.firefox_checkbox.data : jobs.append('MA Lottery Regression Firefox')
        #if form.firefox_checkbox.data : jobs.append('FirefoxJob')
        if form.edge_checkbox.data : jobs.append('EdgeJob')
        if form.ie_checkbox.data : jobs.append('IEJob')

        for job in jobs:
            run_jenkins_job(job)
            result = Result(job_name=job, job_status='Not Started', release_name=form.release_name.data, username=current_user.username)
            db.session.add(result)
            db.session.commit()
        return redirect(url_for('automation.display_test_execution_progress'))
    
    return render_template('choose_test_platform.html',title='Choose Platform', form = form)


@automation.route("/teststatus",methods=['GET', 'POST'])
def display_test_execution_progress():
    conn = sqlite3.connect('E:\\Flask_Blog\\flaskblog\\site.db')
    cur = conn.cursor()
    recent_release_name = cur.execute('select release_name from Result where date_posted = (select max(date_posted) from Result)').fetchall()
    recent_release_name = recent_release_name[0][0]
    query = 'select job_name from Result where release_name="{0}"'.format(recent_release_name)
    running_jobs = cur.execute(query).fetchall()
    running_job_list = []
    for running_job in running_jobs:
        running_job_list.append(running_job[0])

    data = []
    for jobName in running_job_list:
        if 'firefox' in jobName.lower():
            job = 'Firefox'
        elif 'chrome' in jobName.lower():
                job = 'Chrome'
        elif 'edge' in jobName.lower():
            job = 'Edge'
        elif 'ie' in jobName.lower():
            job = 'Internet Explorer'

        cur.execute('select job_status from Result WHERE job_name = "{0}" AND release_name = "{1}"'.format(jobName,recent_release_name))
        tableData = cur.fetchall()
        print('Database Result :', tableData[0][0], file=sys.stderr)
        reportPath='#'
        if len(tableData[0][0])<20:
            data.append((job,0,'Not Started',''))
        else:
            result = (tableData[0][0]).replace("'", '"')
            result = json.loads(result)
            totalTestCase = result['Total Executed']
            totalPass = result['Total Pass']
            totalFail = result['Total Fail']
            reportPath = result['Last Report Path']
            #reportPath = "\\\\172.30.205.179\\Old Reports\\BuildNumber92\\ie\\Tests_ie_5_33_28 AM.html"
            progressPercentage = (totalPass + totalFail) * 100 // totalTestCase
            if get_job_status(jobName) is None:
                data.append((job, progressPercentage,'In Progress',reportPath,totalTestCase,totalPass,totalFail))
            else:
                data.append((job, 100, 'Completed',reportPath,))

        print('Result :',data,file = sys.stderr)
    return render_template('display_test_execution_progress.html',title='Test Execution Progress',dataList = data)


@automation.route("/api/v1/addresult",methods=['POST'])
def add_test_result():
    conn = sqlite3.connect('E:\\Flask_Blog\\flaskblog\\site.db')
    cur = conn.cursor()
    recent_release_name = cur.execute('select release_name from Result where date_posted = (select max(date_posted) from Result)').fetchall()
    recent_release_name = recent_release_name[0][0]
    if request.method == 'POST':
        current_job_name = request.get_json()['Job Name']
        query = 'UPDATE Result SET job_status = "{0}" WHERE job_name = "{1}" AND release_name = "{2}"'.format(request.get_json(),current_job_name,recent_release_name)
        cur.execute(query)
        conn.commit()
        return jsonify({'result': 'successful','data':request.get_json()})


@automation.route("/teststatus/details",methods=['GET', 'POST'])
def show_detail_result():
    conn = sqlite3.connect('E:\\Flask_Blog\\flaskblog\\site.db')
    cur = conn.cursor()
    recent_release_name = cur.execute('select release_name from Result where date_posted = (select max(date_posted) from Result)').fetchall()
    recent_release_name = recent_release_name[0][0]
    query = 'select job_status from Result WHERE job_name = "{0}" AND release_name = "{1}"'.format('ChromeJob',
                                                                                                       recent_release_name)
    job_result = cur.execute(query).fetchall()
    job_result = (job_result[0][0]).replace("'", '"')
    job_result = json.loads(job_result)
    datail_test_result = job_result['Test Cases']
    # running_job_list = []
    return render_template('detail_test_result.html',title='Test Execution Progress',dataList = datail_test_result)

@automation.route("/loadhtml/<file_path>")
def load_html(file_path):
    return send_file(file_path, mimetype='text/html')





