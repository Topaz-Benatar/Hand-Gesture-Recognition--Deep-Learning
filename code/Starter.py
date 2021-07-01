
"""
@author: Topaz
"""
import Userchose
#import CheckDirectory
#import os
#import Printing

def main():
    """
    This function is the first and the main function that starts the all program
    """
    #z=0
    #RenamingFolders(z)
    A=Userchose.userchose()
    A.options() 
    
"""
def RenamingFolders(z):
     #this function changes the name and the number of each image in diffrents files by its name and number  
    while z<5:
        if z==0:
            whichgesture= "palmm"
        if z==1:
            whichgesture= "LL" 
        if z==2:
            whichgesture= "Fistt"
        if z==3:
            whichgesture="OKK"
        if z==4:
            whichgesture="CC"
        path= CheckDirectory.GetDirectory.is_Exsists("Enter the full path (with the name) to a folder with "+ whichgesture)
       Printing.printProcess("[INFO] changing names")
        os.chdir(path)
        i=1
        for file in os.listdir():           
            src=file
            dst=whichgesture +str(i)+".png"
            os.rename(src,dst)
            i+=1
        z=z+1
"""                
        
if __name__ == "__main__":
    main()
    
    
    


   

