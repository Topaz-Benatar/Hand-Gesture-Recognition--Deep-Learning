"""
by Topaz Ben Atar
"""


"""
Userchose file that manages the program by diffrent buttons that pressed by the user.
"""
import tkinter as tk
from PIL import ImageTk, Image
import os
import Extractt
import train_model
import PredictImage
import CheckDirectory
import Printing


class userchose():
    
    def __init__(self):
        """
        defult directories: modelpath and lables path, changes due the user activities
        sorteddatapath is consider as an input that we get either in function casee one or case three.
        """   
        self.sorted_data_path = None
        #self.sorted_data_path = r"C:\Users\Topaz\OneDrive\שולחן העבודה\newdata1"
        self.model_path=R"C:\Users\Topaz\OneDrive\שולחן העבודה\Model3456.model"
        self.labels_path=r"C:\Users\Topaz\OneDrive\שולחן העבודה\lb332.pickle"

        
    
    def case_One(self):
        """
        Get: none
        return: the model path which contains the trained model 
        and the labels path which contains the lables for each images
        this function responsible for the traning model, the most important thing in our program.
        this function call to the handle_train() fanction that locaited in train_model.py file
        """
        if (self.sorted_data_path==None):
            self.sorted_data_path = CheckDirectory.GetDirectory.is_Exsists("Please enter the Dateset path:")
            """
            checks if sorteddatapath is none or got earlier as an input from either case one function or 
            case three function.
            """        
        self.model_path = CheckDirectory.GetDirectory.get_New_Dir("Enter the full path (with the name) to output model: ")
        self.labels_path = CheckDirectory.GetDirectory.get_New_Dir("Enter the full path (with the name) to output label binarizer: ")
        
        while self.model_path == self.labels_path:
            Printing.printError("Error - file will be override")
            self.labels_path = CheckDirectory.GetDirectory.get_New_Dir("Enter the full path (with the name) to output label binarizer: ")
                
        plot_dir = CheckDirectory.GetDirectory.get_New_Dir("Enter the folder directory to output accuracy/loss plot: ")
        
        while self.model_path == plot_dir or self.labels_path == plot_dir:
           Printing.printError("Error - file will be override")
           plot_dir = CheckDirectory.GetDirectory.get_New_Dir("Enter the folder directory to output accuracy/loss plot: ")
    
        os.mkdir(plot_dir)
    
        train_obj = train_model.TrainModel(self.sorted_data_path, self.model_path,self.labels_path, plot_dir)
        
        train_obj.handle_train() 
        
        

    
    def case_Two(self):
        """
        Get: None
        return:None
        this function responsible for the prediciton
        this function call to the handle_classify() fanction that locaited in PredictImage.py file
        """
        
        image_path = CheckDirectory.GetDirectory.is_Exsists("Please enter the image path:")
        predict_obj = PredictImage.ImagePredictor(self.model_path, self.labels_path)  
        predict_obj.handle_classify(image_path)
        
    def case_Three(self):
         """
         Get: None
         return: None
         this function responsible for unzipping files and extract them to a orginal file.
         this functionn call to extract_Zip() that locaited inExtractt.py file
         """
         if (self.sorted_data_path==None):
            self.sorted_data_path = CheckDirectory.GetDirectory.is_Exsists("Please enter the Dateset path:")
         self.sorted_data_path =Extractt.extract_Zip(self.sorted_data_path) # return the folder path after extract (if it was a zip file at first)     
    
    def options(self):  
        """
        Get: none
        Return: None
        This function responsible for each button we see on our option's wall using Tkinter.
        by that important function each button call to its function when pressed. 
        Buttons that exsits are: training the model, predict images, extract zip and exit.
        """
        root=tk.Toplevel()
        root.title ("TOPAZ DL PROJECT")
        e=tk.Entry(root, width=50)
        e.pack()
        
        def MyClick():
            MyLabel=tk.Label(root, text="Hello "+e.get()+ " please chose an option from above", fg="green", font=("Times", 9, "bold italic"))
            MyLabel.pack()
        
        myButton= tk.Button (root,text= "Please enter your name and click me", command=MyClick, bg="green", fg="white", font=("helvetica", 9, "bold"))
        myButton.pack()
        
        
        train_photo= Image.open(r"C:\Users\Topaz\OneDrive\שולחן העבודה\photos\training.png")
        train_photo=train_photo.resize((200, 100),Image.ANTIALIAS)
        train_photo=ImageTk.PhotoImage(train_photo)
        buttontrain= tk.Button (root,image=train_photo, command=lambda:self.case_One()).pack(pady=10)
        
        
        predict_photo= Image.open(r"C:\Users\Topaz\OneDrive\שולחן העבודה\photos\predict11.PNG")
        predict_photo=predict_photo.resize((200, 100),Image.ANTIALIAS)
        predict_photo=ImageTk.PhotoImage(predict_photo)
        buttonpredict= tk.Button (root,image=predict_photo, command=lambda: self.case_Two()).pack(pady=10)
        
         
        extract_photo= Image.open(r"C:\Users\Topaz\OneDrive\שולחן העבודה\photos\zipp.png")
        extract_photo=extract_photo.resize((200, 100),Image.ANTIALIAS)
        extract_photo=ImageTk.PhotoImage(extract_photo)
        extractButton= tk.Button (root, image=extract_photo, command=lambda: self.case_Three()).pack(pady=10)
        
        
        exit_photo= Image.open(r"C:\Users\Topaz\OneDrive\שולחן העבודה\photos\exit.jpeg")
        exit_photo=exit_photo.resize((200, 100),Image.ANTIALIAS)
        exit_photo=ImageTk.PhotoImage(exit_photo)
        exitButton= tk.Button (root, image=exit_photo, command=lambda: self.Needstoquit(root)).pack(pady=10)
  
        root.mainloop()
        
    def Needstoquit(self,root):
        """
        exit the program.
        """
        Printing.printProcess("[INFO] Exiting...")
        root.destroy()
        
