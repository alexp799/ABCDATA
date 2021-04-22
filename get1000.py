import glob
import json
import random 
NUMBER=1000
def give1000(statpath,modelpath=''):
    models=glob.glob(modelpath)
    stats=glob.glob(statpath)
    numbmodels=[]
    count=0
    fw=open('listofmodels.txt','w')
    while count != 1000:
      partsnum=random.randint(1,20)
      print('random number is ',partsnum)
      for stat in stats:
            f=open(stat,'r')
            text=f.read()
            ind=text.find(r'#parts')
            #ind+7
            i=ind+8
            numb=''
            while text[i]!='\n':
                numb=numb+text[i]
                i=i+1
            numb=int(numb)
            if  numb==partsnum:
                index=stat.rfind('/')
                numbmodel=stat[index-8:index]
                numbmodels.append(numbmodel)
                count=count+1
            if count==1000:
                    break
            f.close()
      partsnum=partsnum+2
      print(count)
    json.dump(numbmodels,fw)
    print('writing complete!')
