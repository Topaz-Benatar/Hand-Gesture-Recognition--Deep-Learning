"""
by Topaz Ben Atar
"""

"""
this python file handle the input section and ask to fix it when needed.
"""

import os
import Printing


class GetDirectory():
    
    @staticmethod
    def is_Exsists(massage):
        """
        Get: A message to desplay for the user
        Return: an exsistent path.
            this function requset an exsisting directory and therefore checks if this directory is exsist by using __cheak_Exsists_Dir() function. In addition,
            this function keeps request a directory until this directory will be exsistent.
            """
        Printing.printOptions(massage)
        path = input("Enter: ")

        while not GetDirectory.__cheak_Exsists_Dir(path):
            Printing.printOptions(massage)
            path = input("Enter: ")
            
        return path

    
    @staticmethod
    def __cheak_Exsists_Dir(path):
        """
        Get: path
        return: True or False depends if the path is exsistent or not.
        this function requset an exsistent directory from the user and return True if the current directory exsists
        and False if not       
        """

        if not os.path.exists(path):
            Printing.printError("Error - no such file or directory")
            return False
    
        return True
    
    @staticmethod
    def get_New_Dir(massage):
        """
        Get: A message to desplay for the user
        Return: a new path that was not exsist before 
        this function requset a non exsistent directory and therefore checks if this directory is not exsist by using __cheak_New_Dir() function. In addition,
        this function keeps request a directory until this directory will be non exsistent.
        """
    
        path = ""
    
        while not GetDirectory.__cheak_New_Dir(path):
            Printing.printOptions(massage)
            path = input("Enter: ")
        return path 
   
    
    @staticmethod
    def __cheak_New_Dir(path):
        """
        Get: path
        return: True or False depends if the path is exsistent or not and also if valid
        this function requset a non exsistent directory from the user and return True if the current directory not exsists
        and False if exsist  
        """
       
        if(os.path.exists(path)):
            """
            cheak that the path is not allready exsist, if it is return False
            """
            Printing.printError("Error - this directory is allready exsists")
            return False
    
        try:
            """
            try to make a folder in this path, if it works, the path is valid. But if not, the path is not valid 
            and returning False.
            """
            os.mkdir(path)
            os.rmdir(path)
            return True
         
        except:
            if(path != ""):
                Printing.printError("Error - directory is not valid")            
                return False
            