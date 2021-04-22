import argparse

from app.models import SModel,ModStat

from app.obj2png.src import obj2png

from app import db
import glob
import os
import json
# python obj2png.py -i bunny.obj -a -95 -e 100


def fill_1000(pathtolist,pathtoall):
    f=open(pathtolist,'r')
    modlist=json.load(f)
    #objfiles=pathtoall+'/images/*/*.obj'
    #statfiles=pathtoall+'/stat/*/*.yml'
    for modnum in modlist:
        objfile=pathtoall+'/images/'+modnum+'/'+modnum+'.obj'
        #obj2png.obj2png(obj=objfile,az=-95,el=100)
        imname = os.path.relpath(objfile)
        l = len(imname)
        imname=imname[:l-13]
        nname = os.path.basename(objfile)
        index = nname.index('.')
        nname = nname[:index]
        obj = SModel(name=str(nname), path=str(imname))
        print(objfile)
        db.session.add(obj)
        db.session.commit()
        obj.ReturnPath()
        statfile=pathtoall+'/stat/'+modnum+'/'+modnum+'.yml'
        sroute = os.path.relpath(statfile)
        l = len(sroute)
        sroute = sroute[:l - 13]
        print(sroute)
        sl=len(statfile)
        sname=statfile[sl-12:sl-4]
        print(sname)
        f=open(statfile)
        text=f.read()
        info=ModStat(model_name=sname, body=text, stat_path=sroute, object=SModel.query.filter_by(name=sname).first_or_404())
        db.session.add(info)
        db.session.commit()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='write data')

    parser.add_argument("-l", "--plist",
              dest='plist',        
              help="path to list of files")

    parser.add_argument("-p", "--pall",
              dest='pall',
              help="path to files")

    args = parser.parse_args()

    fill_1000(pathtolist=args.plist, pathtoall=args.pall)
