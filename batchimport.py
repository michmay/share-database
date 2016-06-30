#! python3

import re
import openpyxl
import os
import shelve
import xim

#python program to import client data from excel workbooks (Quantitative Review)



xlsx = re.compile(r'.*\.xlsx')    
print('Working in... '+os.getcwd())


while True:

    print('Found the following .xlsx files for import:\n')
    xlsx = re.compile(r'.*\.xlsx')
    files = os.listdir()
    foundfiles=[]
    
    for e in files:
        m = xlsx.search(e)
        if m:
            foundfiles.append(m.group())
            
    for e in foundfiles:
        print(e)
    print('\n')

    
    print('Change path? y/n:')
    p = input()
    if p == 'y':
        print('Enter path (eg C:\\python\\):')
        p = input()

        try:
            os.chdir(p)
            print('Now working in... '+os.getcwd())
        
        except:
            print('Invalid path...')
    if p == 'n':
        break

print('Importing ' + str(len(foundfiles)) +'files...')
for e in foundfiles:
    x = e.split('.')
    xim.ximp(x[0].upper())

    

"""
while True:
    k=0
    sharelist=[]
    print('Enter .xlsx file name')
    v = input().upper()
    wb = openpyxl.load_workbook(v+'.xlsx')

    sheet = wb.get_sheet_by_name('Sheet1')

    sharex = re.compile(r'(\(\w{3}\))|(^.{3}$)',re.IGNORECASE) #regex finds ticker

    sharef = re.compile(r'\w{3}')           #regex cuts down to 3 letters

    for i in range(sheet.maxrow):           #1000 rows in excel
        if sheet['A'+str(i+1)].value == None:   # peaces out if end of the list
            continue
        print(sheet['A'+str(i+1)].value)        #prints the excel value
        
        match = sharex.search(str(sheet['A'+str(i+1)].value))       #tries to find (XXX) or XXX ticker

        if match != None:           # if a match is found
            
            share = sharef.search(match.group())        #strips any brackets
            
            #print(share.group())  
            sharelist.append(share.group().upper())             #adds this ticker to the share list
    print(str(len(sharelist))+' Shares found:\n')
    for i in sharelist:
        print(i.upper())
    shelveFile = shelve.open('clientshares')        
    shelveFile[v]=sharelist
    shelveFile.close()

 """

