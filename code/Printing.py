"""
by Topaz Ben Atar
"""

"""
     prints diffrent messages in colours that helps the user in diffrent cases.
"""


from colorama import init, Fore, Back, Style
    
def printError(message):
    """
    Get: message
    prints the messeage in red and let the user know about an error. 
    """
    init(convert=True)
    print(Fore.RED + message) 
    Style.RESET_ALL
    
def printOptions(message):
    """
    Get: message
    prints the message in yellow and let the users see and chose the option they want.
    """
    init(convert=True)
    print(Fore.YELLOW + message) 
    Style.RESET_ALL
        
def printProcess(message):
    """
    Get: message
    prints the message in blue to let the user know things that happen while running the progran and about the process.
    """
    init(convert=True)
    print(Fore.BLUE + message) 
    Style.RESET_ALL
    