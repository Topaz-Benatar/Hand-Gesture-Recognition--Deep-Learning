"""
by Topaz Ben Atar
"""


"""
 handle Case two that predict images
"""

from IPython.display import display
from keras.preprocessing.image import img_to_array
from PIL import Image, ImageDraw, ImageFont
from keras.models import load_model
import numpy as np
import pickle

import Printing

IMAGE_SIZE = (50,50)


class ImagePredictor():
    
    def __init__(self, model_path, labels_path):
        self.__model_path = model_path
        self.__labels_path = labels_path
        self.__image_path = ""
        self.__model = None
        self.__lb = None
        
    def handle_classify(self,image_path):
    
        """
        Get: the path of the image we want to predict
        this function manage the prediction
        """
        
        self.__load_Model()
        self.__image_path = image_path
        image_arr, output,imagesize  = self.__load_Image()
        self.__predict_Image(image_arr, output, imagesize)


    def __load_Model(self):
        """
        load the trained convolutional neural network and the label binarizer
        """
        Printing.printProcess("[INFO] Loading network...")
        
        self.__model = load_model(self.__model_path)
        self.__lb = pickle.loads(open(self.__labels_path, "rb").read())
    
    
    def __load_Image(self):
        """
        Get: None
        this function load the image that the user pass its path as a parameter
        return:  the image numpy array after fitting the image colors, dims, pixels scale also, 
        copy of the image as gray scale and size of the given image.
        """
        image = Image.open(self.__image_path)
        imagesize=image.size
        output = image.copy()
        image = image.convert('L')
        image = image.resize((50,50))
        print (IMAGE_SIZE[1])
        image.save(self.__image_path)
        image = np.asarray(image, 'float32')/255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        
        return image, output, imagesize


    def __predict_Image(self,image_arr, output, imagesize):
        """
        Get: the image as array, copy of the image and the size of the given image
        Return: None
        this function predict the image and also  bulid the label and draw the label on the image.
        The copy of the image with the draw on it will be saved on 
        """
        Printing.printProcess("[INFO] Classifying image...")
        proba = self.__model.predict(image_arr)[0]
        idx = np.argmax(proba)
        label = self.__lb.classes_[idx]
        
        label = "{}: {:.2f}% ".format(label, proba[idx] * 100)
        output = output.resize((imagesize))
        d=ImageDraw.Draw(output)
        d.text((10,10), label, fill= "red")
        copypath= r"C:\Users\Topaz\OneDrive\שולחן העבודה\clone.png"
        output.save (copypath)
    
        Printing.printProcess("[INFO] {}".format(label))
        output.show()
        display (output)
  



    