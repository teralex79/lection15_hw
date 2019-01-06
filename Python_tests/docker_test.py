#!/bin/python3.6

import requests
import json
#from colorama import Fore, Back, Style, init

white = '\033[' + str(0) + 'm'
red = '\033[' + str(31) + 'm'
green = '\033[' + str(32) + 'm'
yellow = '\033[' + str(33) + 'm'
grey = '\033[' + str(90) + 'm'

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
      r = requests.get(get_str)
      r_json = json.loads(r.text)
      n = len(r_json)
      clr = grey
      if len(r_json) > 0:
        clr = yellow
        if stt == 'running':
          clr = green
        elif stt == 'dead':
          clr = red

      w1 = item
      if n == 1:
        w1 = 'container'
      elif n == 0:
        n = 'no'
      msg = ''
 
      print(clr + 'You have {0} \"{1}\" {2}.'.format(n, stt, w1) + white)
      hd_str = ''
      for nm in head_dic[item]:
        hd_str += '{0:<15s}'.format(nm.upper())
      if len(r_json) > 0:
        print(hd_str)
        for cont in r_json:
          cont_str = '' 
          for nm in head_dic[item]:
            if nm == 'Id': 
              cont[nm] = cont[nm][:12]
            elif nm == 'Names':
              cont[nm] = cont[nm][0][1:]  
            cont_str += '{0:<15s}'.format(cont[nm])
          print(cont_str)
  else:
    get_str = url + item + addstr1 + addstr2
    r = requests.get(get_str)
    r_json = json.loads(r.text)
    n = len(r_json)
    w1 = item
    if n == 1:
      w1 = 'image'
    elif n == 0:
      n = 'no'
    print(yellow + 'You have {0} {1}.'.format(n, w1) + white)
    hd_str = ''
    for nm in head_dic[item]:
      if nm == 'RepoTags': nm = nm[4:-1]
      hd_str += '{0:<15s}'.format(nm.upper())
    if len(r_json) > 0:
      print(hd_str)
      for img in r_json:
        img_str = ''
        for nm in head_dic[item]:
          if nm == 'Id': 
             img[nm] = img[nm].split(':')[1][:12]
          img_str += '{0:>15s}'.format(str(img[nm]))
        print(img_str)
 
