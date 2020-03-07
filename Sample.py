# -*- coding: utf-8 -*-

import datetime
import os
import shutil

_SRC_FILE_PATH = u'D:/英孚/Book of the week'
_DST_FILE_PATH = u'E:/自定义/Book'


def copyFiles(sourceDir, targetDir):
    if sourceDir.find(".svn") > 0:
        return
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir, file)
        targetFile = os.path.join(targetDir, file)
        if os.path.isfile(sourceFile):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            if not os.path.exists(targetFile) \
                    or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                #open(targetFile, "wb").write(open(sourceFile, "rb").read())
                if sourceFile.endswith('mp3'):
                    shutil.copy(sourceFile, targetDir)
        if os.path.isdir(sourceFile):
            First_Directory = False
            copyFiles(sourceFile, targetDir)

if __name__ == '__main__':
    copyFiles(_SRC_FILE_PATH, _DST_FILE_PATH)



    print('hello')
