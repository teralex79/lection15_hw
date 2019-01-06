#!/bin/python3.6

import requests
import json
from colorama import Fore, Back, Style, init

init(autoreset=True)

url = 'http://192.168.56.103:2376/'

tupl1 = ('containers', 'images')
addstr1 = '/json?all=1'
addstr2 = '&filters='
filtr_tupl = ('running', 'paused', 'exited', 'created', 'restarting', 'removing', 'dead')

head_dic = {'containers': ('Id', 'Names', 'Image'), 'images': ('Id', 'RepoTags', 'Size')}

for item in tupl1:
  if item == 'containers':
    for stt in filtr_tupl:
      fltr = json.dumps({'status': [stt]})
      get_str = url + item + addstr1 + addstr2 + fltr
      print(get_str)
      r = requests.get(get_str)
      r_json = json.loads(r.text)
      n = len(r_json)
      print(r_json)
      w1 = item
      if n == 1:
         w1 = 'container'
      elif n == 0:
         n = 'no'
      msg = ''
      print(msg + 'You have {0} {1} {2}.'.format(n, stt, w1))
#      for nm in head_dic[item]:
#        str1 += 
#  else: 



#str1 = url + tupl1[0] + addstr 
#+ str(&filters=\{status\:\[filtr_tupl[0]\]\})
#print(str1)
#r_con = requests.get(url + tupl1[0] + addstr + str(&filters=\{status\:\[filtr_tupl[0]\]\}))
#r_con_json = json.loads(r_con.text)
#r_img = requests.get(url + '/images/json?all=1')
#r_img_json = json.loads(r_img.text)

#print(r_con_json)
#color_text = r_con_json[0]['Names']
#print(Fore.RED + str(color_text))
#print(color_text)
