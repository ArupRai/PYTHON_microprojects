import time
from os import system
print("HOUR(s):MINUTE(s):SECOND(s)_ _ _ ")
hr=int(input())
min=int(input())
sec=int(input())
while (hr < 24 ) : 
    while ( min <  60 ) :
        while ( sec < 60 ) :
            print (hr,":",min,":",sec)
            time.sleep(1)
            system('cls')
            sec+= 1
        sec = 0
        min +=1
    min = 0
    if ( hr== 23 ) : hr = 0
    else : hr+= 1