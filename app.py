#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:37:28 2021

@author: joachim
"""


from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests

load_dotenv() #read .env!

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-post', methods=['POST'])
def send_post():
    form = request.form
    uid = form.get('uid')
    trees = form.get('trees')
    testmode = form.get('testmode', False)
    testmode = True if testmode else False
    
    url = 'https://member-status.herokuapp.com/add-impact?localEnv=true' if testmode else 'https://member-status.herokuapp.com/add-impact'
    
    payload = {'uid': uid,
               'impact': {
                   'trees': int(trees),
                   'co2e': 0,
                   'reason': 'ambassador signup gift'
                   }
               }    

    r = requests.post(url, json=payload)

    if r.status_code == 200:     
        return 'Trees added and group is synced'
    else:
        return f'something went wrong ):\n\n{r.text}'