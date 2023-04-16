import os

path ="C:/Users/DELL/Desktop/servertx"

filelist = []

for root, dirs, files in os.walk(path):
    for file in files:
        # print(root)
        filelist.append(os.path.join(root,file))

newList=[]
for name in filelist:
    print(name.replace('\\','/'))
    newList.append(name.replace('\\','/'))

with open('mergedfile','w') as mf:
    for file in newList:
        f = open(file,'r')
        mf.write(f"\nstart_{file}\n")
        mf.write(f.read())
        mf.write(f"\nend_{file}\n")
        f.close()

mf.close()