#A python code for function def practice
import numpy as np
import pandas as pd
import sys
print('\033[1m' +'COVID REPORT ANALYSIS' + '\033[0m')
extreme = {}
rec = pd.read_csv('D:\python\covid19.csv')
#x = sys.argv[1]
rep = pd.read_csv('D:\python\p1.csv')
print('--Analysing Report--\n--Please Wait--')
partpcr = int(rep.iloc[0:1,1])
pct = int(rep.iloc[1:2,1])
pspo = int(rep.iloc[2:3,1])
pbrth = int(rep.iloc[3:4,1])
rtpcr = int(rec.RTPCR.mean())
ct = int(rec.CTSCORE.mean())
spo = int(rec.SPO2.mode())
brth = int(rec.BREATH.mean())
#print(partpcr,pct,pspo,pbrth,rtpcr,ct,spo,brth)
def sevrlvl():
    if partpcr > rtpcr:
        nscr = 1
    if pct > ct:
        nscr += 1
    if pspo < spo:
        nscr += 1
    if pbrth < brth:
        nscr += 1
    return nscr
fscore = sevrlvl()
print('\033[1m' +'YOUR TEST SCORE OUT OF 4 :' + '\033[0m',fscore)
def monitor():
    if fscore <=2:
        print('Monitoring Not required')
    elif fscore == 3:
        print('Self quarantine must be done')
    else:
        print('Intense Monitoring Required')
monitor()
def fatality():
    if fscore > 3:
        print('*Fataly infected*')
        ano = input('Enter Aadhar Number\n')
        extreme[ano] = input('Enter Name\n')
        extreme['Rtpcr'] = partpcr
        extreme['CT'] = pct
        extreme['SPO'] = pspo
        extreme['BREATH'] = pbrth
        print(extreme)
    else:
        print('Infection is non fatal\nVisit nearby Doctor for safety concern')
fatality()
        
