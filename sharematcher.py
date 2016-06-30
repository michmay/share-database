import shelve
import os



os.chdir('C:\\python')


def inshares(self):                     #searches each key checking if it contains the stock 
        sharelist = shelve.open('clientshares')
        count = 0
        for i in list(sharelist.keys()):
                if str(self.upper()) in sharelist[i]:
                        print(i)
                        count+=1
                        
        print('\nCOUNTED '+str(count)+ ' CLIENTS\n')

def allclients():                       #prints all the keys
        sharelist = shelve.open('clientshares')
        for i in list(sharelist.keys()):
            print(i.upper())
        print('COUNTED '+str(len(list(sharelist.keys())))+' CLIENTS\n')

def allshares():
        sharelist = shelve.open('clientshares')
        allsharelist=[]
        for i in list(sharelist.keys()):
                clientlist = list(sharelist[i])
                for j in clientlist:
                        if j not in allsharelist:
                                allsharelist.append(j.upper())
                        
        return allsharelist
        

print('Use live share data? y/n')
live = input()
if live == 'y':
        import sharescraper
else:
        def shareprice(share):
                return 'N/A'

print('.....-----/////||||| GOLDEN GOOSE |||||\\\\\-----.....')
print('-\n-\n')
print('Prices are last ASX\n')

while True:
    print('Type \'client\' for individual client holdings mode, or \'ticker\' for share search:')
    x = input()
    if x.upper() == 'CLIENT':
        while True:
                print('\nEnter client name, or type All for a full list')
                y = input()
                if y == '':
                        break
                y = y.upper()
        
                if y == 'ALL':          #print all clients
                    print('\n')
                    allclients()
            
                else:           
                           #convert to uppercase (dict should have upper case keys)
                    try:
                        sharelist = shelve.open('clientshares')
                        clientlist = sharelist[y]       #see if theres a key by the name y
                        for i in range(len(clientlist)):
                            try:
                                iprice = sharescraper.shareprice(clientlist[i])
                            except:
                                iprice = 'NO_CONN'
                            print(clientlist[i]+':\t$'+iprice)
                        print('\nCOUNTED '+str(len(clientlist))+ ' SHARES\n')
                    
                    except:
                        print('\ndid you spell the client name wrong?\n')

    if x.upper() == 'TICKER':        #enter share selection mode
        while True:
                print('\nEnter stock ticker, eg ABC, to display clients holding that stock, or listall:\n')
                z = input()
                print('\n')
                if z == '':
                        break
                z = z.upper()
                if z == 'LISTALL':
                        print('\n')
                        allsh = allshares()
                        allsh.sort()
                        for i in allsh:
                                try:
                                        curprice = sharescraper.shareprice(i)
                                except:
                                        curprice = 'unavail'
                                print(str(i)+'\t$'+str(curprice))
                        print('\n')
                        print(str(len(allsh))+' Total')
                        print('\n\n')
                        
                elif len(z) == 3:
                    try:    
                            curprice = sharescraper.shareprice(z)
                    except:
                            curprice = 'NO_CONN'
                    print('\n'+z+':\t$'+curprice)
                    inshares(z)           #searches clients to match with input
                else:
                    print('ticker must be 3 letters, ***')
        
        
