import os
destpath="C:/Users/DELL/Desktop/serverrx"
destpath=destpath.replace('\\','/')


print(destpath)
filepath= os.path.join(destpath,'star.txt')
filepath=filepath.replace('\\','/')
print(filepath)

filepath='C:/Users/DELL/Desktop/serverrx/settings/28esf3/star.txt'
print(filepath)
newdir=os.path.split(filepath)
ndir=newdir[0]
nfile=newdir[1]

print(newdir)
print(ndir)
print(nfile)

if not os.path.exists(ndir):
    os.makedirs(ndir)

cdir=os.path.join(ndir,'test')


if not os.path.exists(cdir):
    os.makedirs(cdir)
# f= open(filepath,'w')
# f.write("this is test file")
# f.close