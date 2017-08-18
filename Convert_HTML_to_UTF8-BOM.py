import os;
import sys;
filePathSrc="C:\\Projects\\Project 1"
for root, dirs, files in os.walk(filePathSrc):
    for fn in files:
      if fn[-5:] == '.html':
        notepad.open(root + "\\" + fn)
        notepad.runMenuCommand("Encoding", "Convert to UTF-8-BOM")
        notepad.save()  #overwrite current files.
        #newFilename = notepad.getCurrentFilename()[:-5] + "_updated.html"    #rename files 
        #notepad.saveAs(newFilename)                                          #rename files 
        notepad.close()