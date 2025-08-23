import pickle
def information():
    f=open('abc.dat','ab')
    n=int(input('enter number of can.'))
    for i in range(1,n+1):
        idc=int(input('enter id of person'))
        name=input('enter name of student')
        designation=input('enter designation')
        experience=float(input('enter experience'))
        data=[idc,name,designation,experience]
        pickle.dump(data,f)
    f.close()
information()
        
