import requests
import argparse


def give_me(name, ext, dest=''):
    ourl = 'http://0.0.0.0:3300/abc/api/'+name+'/'+ext
    print(ourl)
    response = requests.get(ourl)
    if dest:
        outfile = dest+'/'+name+'.'+ext
    else:
        outfile = name+'.'+ext
    localfile = open(outfile, 'wb')
    localfile.write(response.content)
    response.close()
    localfile.close()


def give_many(names, ext, dest=''):
    for name in names:
        give_me(name, ext, dest)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='files to be returned')

    parser.add_argument("-n", "--names",
              dest='name',
              nargs='+',         
              help="name of file to be  returned")

    parser.add_argument("-e", "--ext",
              dest='ext',
              help="Extension of file")
    parser.add_argument("-d", "--dest",
              dest='dest',
              help="Root to directory of saved files")
    args = parser.parse_args()
  
    print(args)
    for mname in args.name:
        form = str(args.ext)
        if args.dest:
            dest = args.dest
            give_me(name=mname, ext=form, dest=dest)
        else:
            give_me(name=mname, ext=form)


def give_info(name, dest=''):
    ourl = 'http://0.0.0.0:3300/abc/api/'+name+'/info'
    print(ourl)
    response = requests.get(ourl)
    if dest:
        outfile = dest+'/info_'+name+'.txt'
    else:
        outfile = 'info_'+name+'.txt'
    localfile = open(outfile, 'wb')
    localfile.write(response.content)
    response.close()
    localfile.close()
def give_stat(name,dest=''):
    ourl = 'http://0.0.0.0:3300/abc/api/' + name + '/stat'
    response = requests.get(ourl)
    if dest:
        outfile = dest + '/statistics_' + name + '.txt'
    else:
        outfile = 'statistics_' + name + '.txt'
    localfile = open(outfile, 'wb')
    localfile.write(response.content)
    response.close()
    localfile.close()
