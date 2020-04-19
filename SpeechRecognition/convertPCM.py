import os
import filetype

curdir = os.path.abspath('.')
toolPath = os.path.join(curdir, 'ffmpeg-win\\bin\\ffmpeg.exe')

if __name__ == '__main__':
    path = input("please input base dir:")
    files = os.listdir(path)
    for file in files:
        filePath = path + '\\' + file
        kind = filetype.guess(filePath)
        if kind is None:
            continue
        elif str(kind.extension) is 'mp3':
            newfileName = str(filePath)[0:len(filePath)-4]+'.pcm'
            cmdstr = toolPath + ' -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s' % (filePath,newfileName)
            print(cmdstr)
            p = os.popen(cmdstr)
            print(p.read())

