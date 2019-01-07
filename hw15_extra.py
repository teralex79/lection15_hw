#!/bin/python3.6

from flask import Flask, request
import json

app = Flask(__name__)

def valid_login(uname, ps, msg):

  answ = 'Received!'

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
  print(answ)
  return answ 


@app.route('/login', methods=['POST'])
def login():
  un = request.json['user']
  ps = request.json['password']
  msg = request.json['message']
  answ = valid_login(un, ps, msg)
  return answ 

if __name__ == '__main__':
    app.run(port='8080')
