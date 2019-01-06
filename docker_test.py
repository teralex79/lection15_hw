#!/bin/python3.6

import requests
import json

# colors for strings
white = '\033[' + str(0) + 'm'
red = '\033[' + str(31) + 'm'
green = '\033[' + str(32) + 'm'
yellow = '\033[' + str(33) + 'm'
grey = '\033[' + str(90) + 'm'


def frmt_img_size(sz, cnt=0):
  
  dim_tupl = ('B', 'KB', 'MB', 'GB', 'TB')
  frmt_tupl = ('{0:.0f}', '{0:.1f}', '{0:.2f}')

  sz = sz/1000.
  cnt += 1
  if sz >= 1000.:
    f_str = frmt_img_size(sz, cnt)    
  else:
    if sz >= 100.:
      frmt = frmt_tupl[0]
    elif sz >= 10.:
      frmt = frmt_tupl[1]
    else:
      frmt = frmt_tupl[2]
    f_str = frmt.format(sz) + dim_tupl[cnt]
  return f_str


url = 'http://192.168.56.103:2376/'
#url = 'http://192.168.56.101:2376/'

tupl1 = ('containers', 'images')
addstr1 = '/json?all=1'
addstr2 = '&filters='
filtr_tupl = ('running', 'paused', 'exited', 'created', 'restarting', 'removing', 'dead')

head_dic = {'containers': ('Id', 'Names', 'Image'), 'images': ('Id', 'RepoTags', 'Size')}

for item in tupl1:
  if item == 'containers':
# Containers info  
    for stt in filtr_tupl:
      fltr = json.dumps({'status': [stt]})
# Collecting request string for containers, filtered by status.        
      get_str = url + item + addstr1 + addstr2 + fltr
      r = requests.get(get_str)
      r_json = json.loads(r.text)
# Counting filtered containers
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

# Printing colored string with count of filtered containers.
      print(clr + 'You have {0} \"{1}\" {2}.'.format(n, stt, w1) + white)
      hd_str = ''
      if len(r_json) > 0:
# Printing head string.
        for nm in head_dic[item]:
          hd_str += '{0:<15s}'.format(nm.upper())
        print(hd_str)
# Collecting and printing containers info strings
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
# Images info    
    get_str = url + item + addstr1 + addstr2
    r = requests.get(get_str)
    r_json = json.loads(r.text)

# Cointing images    
    n = len(r_json)
# Printing colored string with count of images.  
    w1 = item
    if n == 1:
      w1 = 'image'
    elif n == 0:
      n = 'no'
    print(yellow + 'You have {0} {1}.'.format(n, w1) + white)
    
    if len(r_json) > 0:
      id_list = ['ID']
      tag_list = ['TAG']
      size_list = ['SIZE']

# Collecting and printing formatted strings with images info. 
      max_id = 15
      max_tag = 0 
      max_size = 0
      
      for img in r_json:
        for tags in img['RepoTags']:
          id_list.append(img['Id'].split(':')[1][:12])
 
          tag = tags.split(':')[1]
          l_tag = len(tag)
          if l_tag > max_tag: max_tag = l_tag + 3 
          tag_list.append(tag)

          sz = frmt_img_size(img['Size'])
          l_size = len(sz)  
          if l_size > max_size: max_size = l_size + 3
          size_list.append(sz)
      
      for i in range(0,n+1):
        frmt_id = '{0:<' + str(max_id) + '} '
        frmt_tag = '{1:<' + str(max_tag) + '} '
        frmt_size = '{2:<' + str(max_size) + '}'
        frmt = frmt_id + frmt_tag + frmt_size
        print(frmt.format(id_list[i], tag_list[i], size_list[i]))      
