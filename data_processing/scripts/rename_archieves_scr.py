import os

i = 1
for file in os.listdir():
    #print(file)
    if file[:1]=='r':
        print(file)
        src = file
        dst = "retrieve" + str(i) + '.7z'
        os.rename(src, dst)
        i+=1
