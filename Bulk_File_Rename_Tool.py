                                               # Bulk File Rename To
import os  #to access files from system
from os import system , name  
def clear(): #for simple output ,user friendly observation, 
    # for windows
    if os.name == 'nt':
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear') 
def extention(org) :  #generating extention of a file returns extentions only eg. txt,jpg,none not .jpg or .txt
    temp = org.split(".")
    ext = temp[(len(temp)-1)]
    return ext
def renamer(filepath) : #renames a given bunch or chunk of file according to our input here its single input designed
    count = 0
    new = input("Rename this files as : ")
    for file in os.listdir(filepath) : #traversing through each file in given folder
      
      if count == 0 :
              os.rename(filepath+'\\'+ file , filepath+'\\'+new+'.'+str(extention(file))) #chnaging name
              print("File processed: "+str(count+1)+" ("+file+" ---> "+new+"."+str(extention(file))+")")
      else :
              os.rename(filepath+'\\'+ file , filepath+'\\'+new+'('+str(count)+').'+str(extention(file))) #changing name
              print("File processed: "+str(count+1)+" ("+file+" ---> "+new+"("+str(count)+")"+"."+str(extention(file))+")")
      count = count + 1
              # main funtion
print("   ------------- WELCOME -------------")
while 1 :
  print ("                  MENU\n1. ----- Rename Files\n2. ----- Exit Utility") #M.M
  menu_toggle = int(input("Enter your choise here :  ")) # repeating the function of tool or not
  if menu_toggle == 1 :
    clear()
    path = (input("[NOTE: Replace \\ by \\""\\ in path(Windows generally)]\nEnter location/path of Folder : ")) # input new name ,locations of chunk file to rename
    renamer(path) # calling function
    print("RENAMED ALL")
    menu=int(input("Press 0 to continue : "))
    clear()
  elif menu_toggle == 2 :
    clear()
    print("HARE KRISHNA")
    break
  else : # unwanted inputs like 3,4 or e
    clear()
    raise Exception("Keyboard Interupts :/")
    break