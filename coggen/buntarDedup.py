#! /home/tony/anaconda3/bin/python
import subprocess
import os.path
from pprint import pprint
import time
import sys
import os
import hashlib

bucketIn = 's3://ga-odc-eros-ard-west/'
bucketOut = 's3://ga-odc-eros-un3-west'

homeDir='/data'

Bigcnt=0
Bigtime1 = 0;
Bigtime0 = time.time()


def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
 
 
# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
 
 
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
                if ('/QA/' not in subresult):
                     print ("Nuking\t %s" % subresult)
                     os.remove(subresult)
                     print('___________________')
 
    else:
        print('No duplicate files found.')
 
 
def dedupThem(folders):
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dups
                joinDicts(dups, findDup(i))
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        printResults(dups)


def subprocess_cmd(command):
    print ("+++"*20)
    print ("CMD is -- %s" % command)
    print ("+++"*20)
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    stupidBytesObject = proc_stdout
    outStr = (stupidBytesObject.decode("utf-8"))
    print(outStr)
    return(outStr)

def dfdu(dir):
    print("ooo"*25)
    cmd = "du -hd 2 %s" % dir
    subprocess_cmd(cmd)
    print("ooo"*25)
    cmd = "df -h %s" % dir
    subprocess_cmd(cmd)
    print("ooo"*25)

def s3get(fromfile, tofile):
	print ("hello from s3get copying file " + fromfile)
	infile = fromfile
	outfile = tofile
	pushcmd = "aws s3 cp %s %s" % (infile, outfile)
	print (pushcmd)
	subprocess_cmd(pushcmd)

def s3sync(fname):
	print ("hello from s3sync copying file " + fname)
	infile = fname
	outfile = bucketOut
	pushcmd = "aws s3 sync %s %s" % (infile, outfile)
	print (pushcmd)
	subprocess_cmd(pushcmd)

def untarFile(fname):
	print ("hello from untarFile decompressing file " + fname)
	infile = fname
	pushcmd = "tar -xvf %s" % infile
	print (pushcmd)
	subprocess_cmd(pushcmd)
        #RM TAR FILE NOW
	pushcmd = "rm %s" % infile
	print (pushcmd)
	subprocess_cmd(pushcmd)

def mkTmpDir(filename, prefix):
   a = filename.split('/')
   cell = a[0]
   file = a[1]
   dir = file.split('.xml')[0]
   subdirs =  "%s/%s/%s/" % (cell,dir,prefix)
   print (subdirs)
   root= homeDir + '/exptop/exp/'
   fullDir=root + subdirs
   pushcmd = "mkdir -p " + fullDir
   subprocess_cmd(pushcmd)
   print (fullDir)
   return(fullDir)

def tarFileName(xmlFile, extension):
   file = xmlFile.split('.xml')[0] + extension
   return(file)


def rmTmpDir(dir):
   pushcmd = "rm -fr " + dir
   subprocess_cmd(pushcmd)

# get the file list

dups={}

def bunde(xml):
    """ This subroutine untars and dedups a ARD tile/scene"""

    Bigtime0 = time.time()

    md5FileExtensions = ['_QA.md5', '_SR.md5', '_BT.md5', '_TA.md5']
    tarExtensions = ['_QA.tar', '_SR.tar', '_BT.tar', '_TA.tar']
    fileExtensions = ['.tif', '.xml']

    allExtensions = fileExtensions + md5FileExtensions + tarExtensions


    print (xml)
    print (type(xml))
    id = xml[0]
    print (id)
    for ext in tarExtensions:
       print(ext)
       tarfile = tarFileName(xmlFile=id, extension=ext)
       pre = ext[1:3]
       fullDir = mkTmpDir(filename=id, prefix=pre)
       getFile=bucketIn + tarfile
       baseFile=os.path.basename(tarfile)
       toFile = fullDir + baseFile
       print (">>>"*30)
       print (fullDir)
       print (">>>"*30)
       print (getFile)
       print (toFile)
       print (">>>"*30)
       s3get(fromfile=getFile, tofile=toFile)
       os.chdir(fullDir)
       untarFile(toFile)
       os.chdir(homeDir)
       theDir = homeDir + '/exptop'

    duDir = fullDir[:-4]
    dfdu(duDir)
    dups={}
    paths=[]
    paths.append(theDir)
    dedupThem(paths)
    dfdu(duDir)
    ##s3sync(fname=theDir)
    ##rmTmpDir(dir=theDir)

    Bigtime1 = time.time()
    elapsed = Bigtime1 - Bigtime0
    print ("==="*25)
    print ("TOTAL Bucket loading time for these files took %.2f seconds" % elapsed)
    print ("==="*25)

