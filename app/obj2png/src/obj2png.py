# -*- coding: utf-8 -*-
from app.obj2png.src.ObjFile import ObjFile
import sys
import os
import glob

def obj2png(obj, az, el):

    if '*' in obj:
     objs = glob.glob(obj)
    azim = None
    if az is not None:
        azim = az
    elevation = None
    if el is not None:
        elevation = el

    for objfile in objs:
        if os.path.isfile(objfile) and '.obj' in objfile:
            outfile = objfile.replace('.obj','.png')
            print('Converting %s to %s' % (objfile, outfile))
            ob = ObjFile(objfile)
            ob.Plot(outfile, elevation=elevation, azim=azim)

        else:
            print('File %s not found or not file type .obj' % objfile)
            sys.exit(1)