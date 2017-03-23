from urllib import urlopen
import time

#Using Mr. Schlichting's Website as a test
myurl = raw_input("Enter URL needs HTTP/HTTPS: ")

#while loop that includes the whole repeating program
sec = raw_input("Interval between checking seconds ie 60 = 1 minute: ")
while True:
    #check website
    str1 = urlopen(myurl).read()
    #every second
    time.sleep(float(sec))
    #check it again
    str2 = urlopen(myurl).read()

    if str1 == str2:
        print("No Change")

    else:
        print("There is a disturbance in the dark web...")
