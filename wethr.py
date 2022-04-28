#A python code using dataframes and functions
import numpy as np
import pandas as pd
import sys as s
whist = pd.read_csv('D:\python\weatherHistory.csv')
whist ['month'] = pd.to_datetime(whist['Formatted Date']).dt.month
whist.set_index('month')
#print(whist)
df2 = whist.groupby('month').mean(['Temperature (C)','Precip Type','Humidity']).apply(list).reset_index() #NEW_DF
#print(df2)
w = int(input('Enter 1 for On Season(JAN to JUN)\nEnter 2 for Off Season(JUL to DEC)\n'))
x = int(input('Enter Month\n(1-6 FOR ON SEASON||7-12 FOR OFF SEASON)\n'))
if w==1 and x<=6:
    ans = df2.loc[x-1] #SERIES_OBJECT
elif w==2 and x>=7:
    ans = df2.loc[x-1] #SAME_SERIES_OBJECT
else:
    s.exit('***INVALID INPUT***')
class seasons:
    def __init__(self):
        pass
    def onseas(self):
        print('Month : ',ans[0])
        print('Approx Temperature :',ans[1])
        print('Approx Precipitate Value :',ans[2])
        print('Approx Humidity Value :',ans[3])
        if ans[2] >= 80:
            print('\033[1m' + 'FORECAST FOR THE MONTH' + '\033[0m'+'\nFoggy starting overnight continuing until morning Partly cloudy until evening.')
        elif ans[2] >= 60 and ans[2] < 80:
            print('\033[1m' + 'FORECAST FOR THE MONTH' + '\033[0m'+'\nOvercast throughout the day\nRainy in the evening\nSnowfall at night.')
        else:
            print('\033[1m' + 'FORECAST FOR THE MONTH' + '\033[0m'+'\nPartly cloudy until night\nbreezy starting in the morning continuing until afternoon.')
    def offseas(self):
        print('Month : ',ans[0])
        print('Approx Temperature :',ans[1])
        print('Approx Precipitate Value :',ans[2])
        print('Approx Humidity Value :',ans[3])
        if ans[2] >= 80:
            print('\033[1m' + 'FORECAST FOR THE MONTH' + '\033[0m'+'\nRain throughout the day\nCloudy at night.')
        elif ans[2] >= 60 and ans[2] < 80:
            print('\033[1m' + 'FORECAST FOR THE MONTH' + '\033[0m'+'\nMild Snowfall during the day\nWindy in the afternoon\nHeavy Cold breeze and snowfall at night.')
        else:
            print('\033[1m' + 'FORECAST FOR THE MONTH' + '\033[0m'+'\nOvercast throughout the day and breezy overnight.')
chill = seasons()
if w==1:
    chill.offseas()
else:
    chill.onseas()
