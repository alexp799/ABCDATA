from app.models import SModel
<<<<<<< HEAD
from app.obj2png.src import obj2png
=======
>>>>>>> ea93205c0d654ed07215b6c6a639f6913685ce31
from app import db
import glob
import os
# python obj2png.py -i bunny.obj -a -95 -e 100


def fill_db(objfiles):
    # TODO cюде генерацию png из obj

    obj2png.obj2png(obj=objfiles,az=-95,el=100)
    objs = glob.glob(objfiles)

    for file in objs:
        imname = os.path.relpath(file)
        l=len(imname)
        i=l-1
        while imname[i]!='/':
            i=i-1
        imname=imname[:i]


    objfiles = glob.glob(objfiles)

    for file in objfiles:
        imname = os.path.relpath(file)
        index = imname.index('.')
        imname = imname[4:index]
        print(imname)


        nname = os.path.basename(file)
        index = nname.index('.')
        nname = nname[:index]
        obj = SModel(name=str(nname), path=str(imname))
        db.session.add(obj)
        db.session.commit()
        obj.ReturnPath()
