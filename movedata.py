import argparse

from app.models import SModel,ModStat

from app.obj2png.src import obj2png

from app import db
import glob
import os
import json
# python obj2png.py -i bunny.obj -a -95 -e 100


def fill_1000(pathtolist,pathtoall,pathtonew):
    f=open(pathtolist,'r')
    modlist=json.load(f)
    for modnum in modlist:
        objfile=pathtoall+'/obj/'+modnum+'/'+modnum+'.obj'
        newobj=pathtonew+'/obj/'+modnum+'/'+modnum+'.obj'
        statfile = pathtoall + '/stat/' + modnum + '/' + modnum + '.yml'
        newstat = pathtonew + '/stat/' + modnum + '/' + modnum + '.yml'

        pnewobj=pathtonew+'/images/'+modnum
        pnewstat=pathtonew+'/stat/'+modnum
        os.makedirs(pnewobj)
        os.makedirs(pnewstat)
        os.replace(objfile,newobj)
        os.replace(statfile, newstat)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='write data')

    parser.add_argument("-l", "--plist",
              dest='plist',
              help="path to list of files")

    parser.add_argument("-p", "--pall",
              dest='pall',
              help="path to files")
    parser.add_argument("-n", "--pnew",
                        dest='pnew',
                        help="path to new files")

    args = parser.parse_args()

    fill_1000(pathtolist=args.plist, pathtoall=args.pall,pathtonew=args.pnew)
