from urllib.request import urlopen
import time

#Using Mr. Schlichting's Website as a test
my_url = 'http://rschlichting.weebly.com/hl-physics-3-4.html'

#while loop that includes the whole repeating program
#check website
str1 = urlopen(my_url).read()

while True:
    #every second
    time.sleep(1)
    #check it again
    str2 = urlopen(my_url).read()

    if str1 == str2:
        print("no change")

    else:
        print("change")

