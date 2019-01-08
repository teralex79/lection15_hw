#!/bin/python3.6

from flask import Flask, request, redirect, url_for
import json
import logging
# from logging.handlers import RotatingFileHandler

app = Flask(__name__)

def valid_login(uname, ps, msg, rm_ip):
  import hashlib
  
  answ = 'Received!'
  with open('./login.json', 'r') as of:
    dic_un = json.load(of)
    of.close
  if  uname in dic_un:
    bt = bytes(ps, encoding = 'utf-8')
    h = hashlib.sha1(bt)
    if dic_un[uname] == h.hexdigest():
      app.logger.info('{0} {1}'.format(uname, msg))
    else:
      answ = 'Wrong password!'
      app.logger.warning(rm_ip)
  else:
    answ = 'Unknown user!' 
    app.logger.warning(rm_ip)
  print(answ)
  return answ 

@app.route('/')
def index():
  return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    un = request.json['user']
    ps = request.json['password']
    msg = request.json['message']
    rm_ip = request.environ['REMOTE_ADDR']
    answ = valid_login(un, ps, msg, rm_ip)
#    rm_ip1 = request.remote_addr
#    rm_ip2 = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
#    rm_ip3 = request.environ['REMOTE_ADDR'] 
    return answ
  else:
    return redirect(url_for('index'))

if __name__ == '__main__':
  fh = logging.FileHandler('login.log')
#RotatingFileHandler('login.log', maxBytes=10000, backupCount=1)
  formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s', datefmt = '%Y.%m.%d %H:%M:%S')
  fh.setFormatter(formatter)
  fh.setLevel(logging.INFO)
  app.logger.setLevel(logging.INFO)
  app.logger.addHandler(fh)
  app.run(port='8080')
