#!/bin/python3.6

from flask import Flask, request, redirect, url_for
import json
import logging
# from logging.handlers import RotatingFileHandler

app = Flask(__name__)

def valid_login(uname, ps, msg, rm_ip):

  answ = 'Received!'
#  print(rm_ip)

  with open('./test.json', 'r') as of:
    dic_un = json.load(of)
    of.close
  if  uname in dic_un:
    if dic_un[uname] == ps:
      pass
    else:
      answ = 'Wrong password!'
  else:
    answ = 'Unknown user!' 
#  print(answ)
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
#    app.logger.warning('A warning occurred (%d apples)', 42)
#    app.logger.info('Info', rm_ip)
    return answ
  else:
#    rm_ip1 = request.remote_addr
#    rm_ip2 = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
#    rm_ip3 = request.environ['REMOTE_ADDR'] 
#    print(rm_ip1, rm_ip2, rm_ip3)
    return redirect(url_for('index'))
#    return 'Hello!'
#    print(request.remote_addr)

if __name__ == '__main__':
#  handler = logging.basicConfig(filemode="w", filename="login.log", level=logging.INFO)
#RotatingFileHandler('login.log', maxBytes=10000, backupCount=1)
#  handler.setLevel(logging.INFO)
#  app.logger.addHandler(handler)
  app.run(port='8080')
