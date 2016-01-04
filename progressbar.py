from time import sleep
import sys

print "Start downloading..."

progress = 0
while progress <= 100:
    print "\r" , str(progress) +"%" , "downloaded" , "|"+"#"*(progress/10)+"|" , "/-\|."[progress/3%5] ,
    sys.stdout.flush()
    progress += 1
    sleep(0.1)

print "\b\b \nDownload finished."
