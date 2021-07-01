"""
by Topaz Ben Atar
"""

"""
Extract zip files.
"""

from zipfile import ZipFile
import CheckDirectory
import Printing


    
def extract_Zip(zip_path): 
    """
    Get: zip path (or orginial one)
    Return: ordinary file.
    this function checks either the path is zip path or ordinary path. if the path was an ordinary one, 
    the function calls printProcess that locaited in Printing.py() file to let the user know it was an ordinary file
    and return it. if the path was a zip path it extract the images from the zippath into the path that the function
    gets as an input.
    """
    path = zip_path
    ls = zip_path.split(".")

    if ls[len(ls)-1] == "zip":
        Printing.printProcess("[INFO] Got a zip file...")
        path = CheckDirectory.GetDirectory.get_New_Dir("Choose the path to extract the files")          
        with ZipFile(zip_path, 'r') as zipObj:
            # Extract all the contents of zip file in different directory
            Printing.printProcess("[INFO] Extracting the images from the zip file...")
            zipObj.extractall(path)
        
        Printing.printProcess("[INFO] Finished extracting process...")

    else:
        Printing.printProcess("[INFO] Got ordinary file...")
    return path
            
            