import os
import json
import csv
#import numpy as np
#import matplotlib.pyplot as plt

def build_dict(infile, problems):
    student = dict()
    with open(infile) as inf:
        for line in inf:
            item = eval(line)

            if item['tag'] == 0 or item['time'] == 0:
                continue

            current = item['time']


            problemID = problems[item['tag']]

            if problemID not in student:
                student[problemID] = {'duration': 0, 'lastcheck': current}

            if item['time'] - student[problemID]['lastcheck'] <= 62:
                student[problemID]['duration'] += current - student[problemID]['lastcheck']

            student[problemID]['lastcheck'] = current

    return student

################################################################################################### Main

dir = os.path.dirname('__file__')
infile = os.path.join(dir, 'homework3-withtag')

# homework 1 problems
problems = ['???','bigMul','mulByDigit','bigAdd','removeZero', 'padZero', 'clone', 'stringOfList', 'sepConcat', 'pipe', 'sqsum']

hw3 = list()
for i in os.listdir(infile):
    hw3.append(build_dict(os.path.join(infile,i), problems))

#print hw1


summary = dict()
for i in problems:
    if i == '???': continue
    summary[i] = sum(item[i]['duration'] for item in hw3 if (i in item))
print (summary)


summary = dict()
for i in problems:
    if i == '???': continue
    summary[i] = [int(item[i]['duration']/60) for item in hw3 if (i in item)]

print (summary)
#print (int(max(summary['sumList'])))
#print int(min(summary['sumList']))

#for i in summary['bigMul']:
#    print(i)

problems_2 = ['bigMul','mulByDigit','bigAdd','removeZero', 'padZero', 'clone', 'stringOfList', 'sepConcat', 'pipe', 'sqsumc']

for q in problems_2:
    stdnum = []
    with open('test.csv','a') as csvfile:
        writer = csv.writer(csvfile)
        for c in range(1, 1500):

            stdnum.append(sum(i < c for i in summary[q]))
            c += 30

    #print (stdnum)
        print(q)
        writer.writerow(q)
        writer.writerow(stdnum)
