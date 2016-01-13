import re
import os
import json
import time
from os.path import basename
from os.path import splitext

dir = os.path.dirname('__file__')

target = os.path.join(dir, 'logs-detail')
output = os.path.join(dir, 'withtag')
pretimeS = 0
j=1
preSession = 0
pretag = ''
totalTime = 0

problems = ['palindrome', 'listReverse', 'digitalRoot', 'additivePersistence', 'digits', 'digitsOfInt', 'sumList']

def parse(infile, outfile):
  hw = dict()
  with open(infile) as inf, open(outfile,'a') as of:
    
    for line in inf:
      item = eval(line)
      
      for i in problems:
        for code in item['ocaml']:
          #tag homeworks
          if item['event']['type'] == 'eval' && (i in str.split(code['in']):
            item['tag'] = i
          #tag sessions
          if time.time(item['event']['time']-pretimeS) > 31 && pretimeS != 0):
            item['session'] = ++j
          else
            item['session'] = j

          pretimeS = item['event']['time']

      json.dump(item, of)
      of.write('\n')

    for line in of:
      item = eval(line)
      
      for i in problems:
        for code in item['ocaml']:
          #initialize preSession
          if(preSession == 0):
            preSession = item['session']

          #get total time of each questions
          #when goes to the next question, give out the previous question's total time
          if (item['event']['type'] == 'eval' && item['tag'] != pretag  && pretag != 0):
            print("total time for "+ pretag + " " + totalTime + " ")
            totalTime = 0
          
          #if session unchanged, add the portion of time to total time, else just update
          #the pretimeS
          if(pretimeS != 0 && item['session'] == preSession):
            totalTime = totalTime + item['event']['time'] - pretimeS

          preSession = item['session']
          pretag = item['tag']
          pretimeS = item['event']['time']

  inf.close()
  of.close()

#infile = os.path.join(target, 'alperez.json')
#outfile = os.path.join(directory, 'test')
#parse(infile, outfile)

for i in os.listdir(target):
  if not os.path.exists(output):
    os.makedirs(output)
  print(i)
  # skip anything that is not hw1
  homework = re.search('hw1',i) 
  if homework is None:
    print('skip')
    continue
  infile = os.path.join(target, i)
  outfile = os.path.join(output, i)
  parse(infile, outfile)