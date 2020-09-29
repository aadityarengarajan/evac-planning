import pickle,random, csv
from os import remove,rename
from datetime import datetime, timedelta


with open('flights.csv','r') as details:
    data=csv.reader(details)
    c=0
    flights=[]
    for rec in data:
        if c==0:
            c+=1
            pass
        else:
            flights.append(rec)


def adddata():
   with open('passengers.dat','ab') as f:
    name=input("Name : ")
    while 1:
        try:
            age=int(input("Age : "))
        except:
            continue
        break
    while 1:
        try:
            contact=int(input("Contact # : "))
        except:
            continue
        break
    while 1:
        try:
            civilid=int(input("Civil ID # : "))
        except:
            continue
        break
    while 1:
        try:
            passport=int(input("Passport # : "))
        except:
            continue
        break
    validreasons={1:'Medical',2:'Lost job',3:'Visa expired',4:'Medical emergency'}
    reasonvalidation=False
    while reasonvalidation==False:
        try:
            reason=int(input('''
(1) Medical
(2) Lost job
(3) Visa Expired
(4) Medical Emergency


Reason :'''))
            if reason>=1 and reason<=5:
                reasonvalidation=True
                reason=validreasons[reason]
        except:
            continue
    state=input("State : ").upper()
    airport=input("Airport : ").capitalize()
    passenger={
    'name':name,
    'age':age,
    'contact':contact,
    'civilid':civilid,
    'passport':passport,
    'reason':reason,
    'state':state,
    'airport':airport
    }
    print(passenger)
    print(f.name)

    pickle.dump(passenger,f)
    details='''
Name '''+name+'''
Age '''+str(age)+'''
Contact No. '''+str(contact)+'''
Civil ID No. '''+str(civilid)+'''
Passport No. '''+str(passport)+'''
Reason '''+reason+'''
State '''+state+'''
Airport '''+airport+'''

Added to database.
'''
    print(details)

def passengers():
   with open('passengers.dat','rb') as f:
    lst=[] 
    while 1:
        try:    
            
            guest=pickle.load(f)
            lst.append(guest)
        except:
            break
          
    return lst

def searchbyname(name):
    for i in passengers():
        if name.lower()==i['name'].lower():
            print ('''
Name '''+i['name']+'''
Age '''+str(i['age'])+'''
Contact No. '''+str(i['contact'])+'''
Civil ID No. '''+str(i['civilid'])+'''
Passport No. '''+str(i['passport'])+'''
Reason '''+i['reason']+'''
State '''+i['state']+'''
Airport '''+i['airport']+'''
            ''')
            deletebycivilid(i['civilid'])

def searchbycivilid(civilid):
    for i in passengers():
        if civilid==i['civilid']:
            print ('''
Name '''+i['name']+'''
Age '''+str(i['age'])+'''
Contact No. '''+str(i['contact'])+'''
Civil ID No. '''+str(i['civilid'])+'''
Passport No. '''+str(i['passport'])+'''
Reason '''+i['reason']+'''
State '''+i['state']+'''
Airport '''+i['airport']+'''
            ''')
            deletebycivilid(i['civilid'])

def searchbypassport(passport):
    for i in passengers():
        if passport==i['passport']:
            print( '''
Name '''+i['name']+'''
Age '''+str(i['age'])+'''
Contact No. '''+str(i['contact'])+'''
Civil ID No. '''+str(i['civilid'])+'''
Passport No. '''+str(i['passport'])+'''
Reason '''+i['reason']+'''
State '''+i['state']+'''
Airport '''+i['airport']+'''
            ''')
            deletebycivilid(i['civilid'])

def searchbycontact(contact):
    for i in passengers():
        if contact==i['contact']:
            print( '''
Name '''+i['name']+'''
Age '''+str(i['age'])+'''
Contact No. '''+str(i['contact'])+'''
Civil ID No. '''+str(i['civilid'])+'''
Passport No. '''+str(i['passport'])+'''
Reason '''+i['reason']+'''
State '''+i['state']+'''
Airport '''+i['airport']+'''
            ''')
            deletebycivilid(i['civilid'])

def searchbydate(date):
    for i in flights:
        if str(date).replace(' ','')==str(i[3]).replace(' ',''):
            print ('''
Flight # '''+i[0]+'''
Destination '''+str(i[1])+'''
No. of passengers '''+str(i[2])+'''
Date '''+str(i[3])+'''
Confirmation '''+str(i[4])+'''
            ''')

def searchbydestination(destination):
    for i in flights:
        if destination.replace(' ','')==str(i[1]).replace(' ',''):
            print ('''
Flight # '''+i[0]+'''
Destination '''+str(i[1])+'''
No. of passengers '''+str(i[2])+'''
Date '''+str(i[3])+'''
Confirmation '''+str(i[4])+'''
            ''')

def searchbyreason(reason):
    for i in passengers():
        if reason==i['reason']:
            print( '''
Name '''+i['name']+'''
Age '''+str(i['age'])+'''
Contact No. '''+str(i['contact'])+'''
Civil ID No. '''+str(i['civilid'])+'''
Passport No. '''+str(i['passport'])+'''
Reason '''+i['reason']+'''
State '''+i['state']+'''
Airport '''+i['airport']+'''
            ''')
            deletebycivilid(i['civilid'])

def searchbyairport(airport):
    for i in passengers():
        if airport==i['airport']:
            print( '''
Name '''+i['name']+'''
Age '''+str(i['age'])+'''
Contact No. '''+str(i['contact'])+'''
Civil ID No. '''+str(i['civilid'])+'''
Passport No. '''+str(i['passport'])+'''
Reason '''+i['reason']+'''
State '''+i['state']+'''
Airport '''+i['airport']+'''
            ''')
            deletebycivilid(i['civilid'])

def searchfordeletion(civilid):
    for i in passengers():
        if civilid==i['civilid']:
            return i

def deletebycivilid(civilid):
    choice=input("DELETE? (Y/N) : ")
    if choice in 'Yy':
        with open('temp.dat','wb') as f:
            for i in passengers():
                if i!=searchfordeletion(civilid):
                    pickle.dump(i,'temp.dat')
        remove('passengers.dat')
        rename('temp.dat','passengers.dat')

    else:
        pass

def allpassengers():
    for i in passengers():
            print( '''
====================================

Name '''+i['name']+'''
Age '''+str(i['age'])+'''
Contact No. '''+str(i['contact'])+'''
Civil ID No. '''+str(i['civilid'])+'''
Passport No. '''+str(i['passport'])+'''
Reason '''+i['reason']+'''
State '''+i['state']+'''
Airport '''+i['airport']+'''
          
====================================
            ''')

def allflights():
    for i in flights:
            print ('''
====================================

Flight # '''+i[0]+'''
Destination '''+str(i[1])+'''
No. of passengers '''+str(i[2])+'''
Date '''+str(i[3])+'''
Confirmation '''+str(i[4])+'''

====================================
            ''')


menu='''
PASSENGER PRIORITISATION FOR EVACUATION DURING PANDEMIC

0) Add Details
- Searching for passenger details 
    1) Search by name
    2) Search by civilid number
    3) Search by passport number
    4) Search by contact number
- Searching for flight details
    5) Search by date
    6) Search by destination
- Searching details of a group of passengers
    7) Search by Reason
    8) Search by Airport
- View All Details
    9) View all passengers
    10) View all flights
'''
exit=False
while exit==False:
    while 1:
        try:
            print(menu)
            choice=int(input("Choice : "))
        except:
            continue
        break
    if choice==1:
        searchbyname(input("Name : "))
    elif choice==2:
        while True:
            try:
                civilid=int(input("Civil ID No. : "))
            except:
                continue
            break
        searchbycivilid(civilid)
    elif choice==3:
        while True:
            try:
                pasportno=int(input("Passport No. : "))
            except:
                continue
            break
        searchbypassport(pasportno)
    elif choice==4:
        while True:
            try:
                contact=int(input("Contact No. : "))
            except:
                continue
            break
        searchbycontact(contact)
    elif choice==5:
        searchbydate(input("Date : "))
    elif choice==6:
        searchbydestination(input("Destination : "))
    elif choice==7:
        searchbyreason(input("Reason : "))
    elif choice==8:
        searchbyairport(input("Airport : "))
    elif choice==0:
        adddata()
    elif choice==9:
        allpassengers()
    elif choice==10:
        allflights()
    else:
        exit=True