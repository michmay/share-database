import os
import shelve
import re
import openpyxl


#function for importing into the shelve module


def ximp(file):
    sharelist=[]
    file = file.upper()
    
    wb = openpyxl.load_workbook(file+'.xlsx')
    sheet = wb.active

    sharex = re.compile(r'(\((.*)?\w{3}(.*)?\))|(^.{3}$)',re.IGNORECASE) #regex finds ticker
    sharef = re.compile(r'\w{3}')           #regex cuts down to 3 letters

    upperbound = sheet.get_highest_row()
    for i in range(upperbound):      #max row in excel

        match = sharex.search(str(sheet['A'+str(i+1)].value))       #tries to find (XXX) or XXX ticker
        
        if match != None:
            share = sharef.search(match.group())
            sharelist.append(share.group().upper())

    print(str(len(sharelist))+' Shares found:\n')
    for i in sharelist:
        print(i.upper())

    
    shelveFile = shelve.open('clientshares')        
    shelveFile[file]=sharelist
    shelveFile.close()
