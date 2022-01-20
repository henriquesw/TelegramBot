import time
import os

full_path = os.path.realpath(__file__)
PATH = os.path.dirname(full_path) + './Videos/'
DAY = 24*3600

def deletevideos():
    videos = getfiles(PATH)
    print(videos)
    if videos != []:
        for video in videos:
            os.remove(os.path.join(PATH,video))

def getfiles(dirpath):
    a = []
    for s in os.listdir(dirpath):
        if time.time() - DAY > os.path.getmtime(os.path.join(dirpath, s)):
            a.append(s)
    return a

while True:
    deletevideos()
    time.sleep(3600)