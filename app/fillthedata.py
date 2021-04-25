from app.models import SModel,ModStat

from app.obj2png.src import obj2png

from app import db
import glob
import os
# python obj2png.py -i bunny.obj -a -95 -e 100
from config import Config
def fill_db(pathtoall):
    objfiles=pathtoall+'/obj/*/*.obj'
    statfiles=pathtoall+'/stat/*/*.yml'
    obj2png.obj2png(obj=objfiles,az=-95,el=100)
    objs = glob.glob(objfiles)
    stats=glob.glob(statfiles)


    for file in objs:


            imname =file
            l = len(imname)
            imname=imname[:l-13]
            nname = os.path.basename(file)

            index = nname.index('.')
            nname = nname[:index]
            obj = SModel(name=str(nname), path=str(imname))
            print(obj)
            db.session.add(obj)
            db.session.commit()
            obj.ReturnPath()


    for stat in stats:

           sroute = stat
           l = len(sroute)
           sroute = sroute[:l - 13]
           print(sroute)
           sl=len(stat)
           sname=stat[sl-12:sl-4]
           print(sname)
           f=open(stat)
           text=f.read()
           info=ModStat(model_name=sname, body=text, stat_path=sroute, object=SModel.query.filter_by(name=sname).first_or_404())
           db.session.add(info)
           db.session.commit()


