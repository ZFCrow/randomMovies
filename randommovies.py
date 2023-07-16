import os 
import shutil
import random

#description of script 
#* movie roulette
#* When you cannot decide what to watch, this script will help you decide
#* moves 10 random video files from each folder to a random folder

normDirectory= 'E:\\Normal'
Directory="E:\\Normal\\VIDS"



#* sets the directory to the video parent folder, VIDS
os.chdir(Directory)
count=0 
jpCount=0


#? moving files to the random folder
randomCount=0


for i in os.listdir():
    path=os.path.join(Directory,i)
    #* sets the directory to the folder under parent folder
    print(path)

    #* checks if the endresult is a directory and continues if it is
    if os.path.isdir(path):
        os.chdir(path)

    #* you can set the count to any amount of videos you want to move
    #* 
    while randomCount<10:
        randomFile1=random.choices(os.listdir())
        #print(randomFile1)
        
        randomFile=str(randomFile1[0])
        sourcePath=os.path.join(path,randomFile)


        #* sets the destination folder to the random folder, you can change this to any folder you want, but make sure the folder exists
        destinationFolder=os.path.join(normDirectory,'Random')

        #* sets the destination path to the random folder
        destinationPath=os.path.join(destinationFolder,randomFile)
        print(sourcePath)
        print(destinationPath)
        
        shutil.move(sourcePath,destinationPath)
        randomCount+=1

        count+=1
    randomCount=0



print(count)
#print(randomCount)



