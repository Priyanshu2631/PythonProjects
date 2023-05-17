#*******************************************PYTHON PROJECT ON EMPLOYEE DATABASE********************************************************************

print('\t\t\t\t\t\t\tWELCOME TO THE DATABASE')
print('********************************************************************************************************************************************')
def Menu():
    print('\n')
    print('\t\t\t\tMAIN MENU')
    print('1.Create Record')
    print('2.Enter New Record')
    print('3.Display Record')
    print('4.Search Record')
    print('5.Update Record')
    print('6.Delete Record')
    print('7.Exit')

Menu()

import pickle,os,sys
#*********************************************Consent Of The User***********************************************************************************

def Consent():
    k=input('Want To Continue Working With File(Y/y):')
    if k in 'Yy':
        Choice()
    else:
        print('Thanks For Working')
        sys.exit()

#*********************************Creating the Database and Entering the 1st Record*******************************************************************

def Create():
    f=open('Employee.dat','wb')
    a=int(input('Enter Employee ID:'))
    b=input('Enter name:')
    c=input('Enter Department:')
    d=input('Enter Designation:')
    L=[a,b,c,d]
    pickle.dump(L,f)
    print('Database Created Successfully and Written The Record')
    f.close()
    Consent()

#*******************************Entering Record To The Database*****************************************************************************************

def Append():
    f=open('Employee.dat','ab')
    while True:
        a=int(input('Enter Employee ID:'))
        b=input('Enter name:')
        c=input('Enter Department:')
        d=input('Enter Designation:')
        L=[a,b,c,d]
        pickle.dump(L,f)
        print('Data Entered Successfully')
        v=input('Want to input more data(Y/N):')
        if v in 'Yy':
            continue
        else:
            break
            f.close()
    Consent()
    
#******************************Displaying Record To User******************************************************************************************************
def Display():
    try:
        f=open('Employee.dat','rb')
    except:
        print('File not found')
        return
    try:
        while True:
            r=pickle.load(f)
            print(r)
    except:
        f.close()
    Consent()

#****************************Searching A Particular Record*****************************************************************************************************

def Search():
    try:
        f=open('Employee.dat','rb')
    except:
        print('File not Found')
        return

    try:
        x=int(input('Enter Employee ID To Search:'))
        fl=0
        while True:
            r=pickle.load(f)
            if r[0]==x:
                fl=1
                print(r)
                break
            
    except:
        pass
    f.close()
    if fl==0:
        print('Record Not Found')
    Consent()

#*********************************Modifying a Record***********************************************************************************************************

def Modify():
    try:
        f=open('Employee.dat','rb+')
    except:
        print('File not found')
        return

    x=int(input('Employee ID for modifying:'))
    p,fl=0,0
    try:
        while True:
            r=pickle.load(f)
            if r[0]==x:
                print('Enter the previous data if no change in the respective field')
                r[1]=input(' Enter Name:')
                r[2]=input('Enter Department:')
                r[3]=input('Enter Designation:')
                f.seek(p)
                pickle.dump(r,f)
                print('Record updated')
                fl=1
            p=f.tell()
    except:
        f.close()
    if fl==0:
        print('Record not found')
    Consent()

#********************************Deleting A Particular Record*************************************************************************************************

def Delete():
    try:
        f=open('Employee.dat','rb')
    except:
        print('No file')
        return

    f1=open('New.dat','wb')
    x=int(input('Enter EmpID to delete:'))
    fl=0
    try:
        while True:
            r=pickle.load(f)
            if r[0]==x:
                fl=1
                continue
            pickle.dump(r,f1)
    except:
        f.close()
        f1.close()

    os.remove('Employee.dat')
    os.rename('New.dat','Employee.dat')

    if fl==0:
        print('Record not found')
    else:
        print('Record Deleted')
    Consent()

#**************************Choices For The User*****************************************************************************************************************

def Choice():
    ch=int(input('Enter your choice between 1 to 7:'))

    if ch==1:
        Create()
    elif ch==2:
        Append()

    elif ch==3:
        Display()

    elif ch==4:
        Search()

    elif ch==5:
        Modify()

    elif ch==6:
        Delete()

    elif ch==7:
        print('Thank You')
        sys.exit()
    else:
        print('Invalid Input')
        sys.exit()

Choice()

#*************************************************************************END OF PROJECT***************************************************************************











