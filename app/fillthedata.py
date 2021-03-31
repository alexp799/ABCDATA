from app.models import SModel
from app.obj2png.src import obj2png
from app import db
import glob
import os
# python obj2png.py -i bunny.obj -a -95 -e 100


def fill_db(objfiles):
    # TODO cюде генерацию png из obj
    obj2png.obj2png(obj=objfiles,az=-95,el=100)
    objfiles = glob.glob(objfiles)

    for file in objfiles:
        imname = os.path.relpath(file)
        index = imname.index('.')
        imname = imname[:index]


        nname = os.path.basename(file)
        index = nname.index('.')
        nname = nname[:index]
        print(nname)
        obj = SModel(name=str(nname), path=str(imname))
        db.session.add(obj)
        db.session.commit()
        obj.ReturnPath()
