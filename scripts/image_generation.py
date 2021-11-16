import sys

f = open("demofile2.txt", "a")
f.write(str(sys.argv))
f.close()
