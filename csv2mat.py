# -*- coding:utf-8 -*-
#Zhang Jiayun, Feb. 2018

import generateVisits
import selectDisease
import csv
import numpy as np
import scipy.io as sio
import datetime

visits = generateVisits.getVisitDic('E1[0-4]')
#print visits[8]
#selectDisease.writeDisease('I6[0-4]')
Patient = []
Elapsed = []
Labels = []
for i in visits.keys():
    visitFreq = []
    ElapsedFreq = []
    labelFreq = []

    for j in visits[i].keys():
        visitPerPatient = []
        timePerPatient = []
        ElapsedPerPatient = []

        for k in range(len(visits[i][j])-1):
            '''
            if k == 0:
                timePerPatient.append(0)
            else:
                now = datetime.datetime.strptime(visits[i][j][k][0], "%Y%m%d")
                last = datetime.datetime.strptime(visits[i][j][k-1][0], "%Y%m%d")
                timePerPatient.append((now - last).days)
                #timePerPatient.append(((now - last).days)/30.0)
                #timePerPatient.append(rrule.rrule(rrule.MONTHLY, dtstart=last, until=now).count())
            '''
            now = datetime.datetime.strptime(visits[i][j][k][0], "%Y%m%d")
            nxt = datetime.datetime.strptime(visits[i][j][k + 1][0], "%Y%m%d")
            timePerPatient.append((nxt-now).days)
            #visits[i][j][k][1].append((nxt-now).days)
            visitPerPatient.append(visits[i][j][k][1])
        ElapsedPerPatient.append(timePerPatient)
        visitFreq.append(visitPerPatient)
        ElapsedFreq.append(ElapsedPerPatient)
        labelFreq.append(visits[i][j][len(visits[i][j])-1][1])
    visitFreq = np.array(visitFreq)
    ElapsedFreq = np.array(ElapsedFreq)
    labelFreq = np.array(labelFreq)
    #print visitFreq
    Patient.append(visitFreq)
    Elapsed.append(ElapsedFreq)
    Labels.append(labelFreq)
#print Patient
#sio.savemat('data.mat', {'General_Patient': Patient, 'General_Elapsed': Elapsed, 'General_Labels': Labels})
sio.savemat('Contrast/LSTM/data.mat', {'General_Patient': Patient, 'General_Elapsed': Elapsed, 'General_Labels': Labels})

#S1 = 'data_selected.mat'
S1 = 'data.mat'
m = sio.loadmat(S1)
General_Patient = m['General_Patient']
General_Elapsed = m['General_Elapsed']
General_Labels = m['General_Labels']
#print General_Patient
#print General_Elapsed
#print General_Labels
