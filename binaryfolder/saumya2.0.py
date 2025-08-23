import pickle
def create():
    PNR=input('enter passenger no.')
    PNAME=input('passenger name')
    BRDSTN=input('boarding stataion name')
    DESTN=input('destination station name')
    FARE=float(input('fare amount for the journey'))
    data=[PNR,PNAME,BRDSTN,DESTN,FARE]
    f=open('happy.dat','wb')
    pickle.dump(data,f)
    f.close()
create()
def searchdestn(D):
    f=open('happy.dat','rb')
    while true:
        try:
            rec=pikle.load(f)
            if data[3]==D:
                print('same desitnation',rec)
        except:
            pass
    f.close()
searchdestn('hh')

