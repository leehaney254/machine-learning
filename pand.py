import pandas as pd
import cv2
dict ={
    'Country':['Brazil','Russia', 'Inda', 'China', 'South Africa'],
    'Capital':['Brasilia', 'Moscow', 'New Delhi', 'Beijing','Pretoria'],
    'Area':[8.516, 17.10, 3.286,9.597, 1.221],
    'Population':[200.4, 143.5, 1252, 1357, 52.98]
}
brics = pd.DataFrame(dict)# turning it into a pandas table
brics.index('Br','Ru','In','Ch','Sa')
print(brics)