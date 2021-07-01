"""
by Topaz Ben Atar
"""

"""
this python file handle the train section
"""


import matplotlib
matplotlib.use("Agg")

from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from PIL import Image



import MyModel

import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import random
import pickle
import os

import Printing


class TrainModel():
    
  
        
    def __init__(self, dataset_path, model_path, labels_path, plot_dir):
        
        self.datasetpath = dataset_path # the data set directory
        self.modelpath = model_path    # the directory the user chose to save the trained model
        self.labelspath = labels_path #the directory the user chose to save the images labels
        self.plotdir = plot_dir        # the directory to the folder that the user chose to save the graph images
        
        self.EPOCHS = 8  #number of epochs
        self.INITLR = 1e-3  #learning rate
        self.BS = 32 #batch size
        self.IMAGEDIMS = (50, 50, 1) #image dimensions
        self.datas = []   # list of all the images as arrays
        self.labelss = []  #list labels of all the images

    def handle_train(self):
    
        """
        this public method is responsible for all the train, it calls diffrent functions to do it well.
        """
        
        self.__loading_Images()
        self.PixelsS()
        history = self.__train()
        self.__graph1(history, self.plotdir+ r"\plot1.png")
        self.__graph2(history, self.plotdir +r"\plot2.png")
    
    
    
    def __loading_Images(self):
        """
        this method load the images from the current directory. After we load the images, we load them
        as gray scale, convert it to numpy array and store it in the data list. In addition, we extract the class
        label from the image path and update the labels list.
        """
        Printing.printProcess("[INFO] Loading images...")
        imagePaths = sorted(list(paths.list_images(self.datasetpath)))
        random.seed(42)
        random.shuffle(imagePaths)


        for imagePath in imagePaths:
            image = Image.open(imagePath)           
            image = image.convert('L')
            image = image.resize((self.IMAGEDIMS[0], self.IMAGEDIMS[1]))
            image.save(imagePath)
            image = img_to_array(image)
            self.datas.append(image)

            label = imagePath.split(os.path.sep)[-2]
            self.labelss.append(label)
          
        
 
    def PixelsS(self):    
        """ 
        this method scale the images pixels from range [0, 255] to range [0, 1] 
        the data list store all the images by arrays
        by convert this list we convert all the images pixels range
        
        """
        self.datas = np.array(self.datas, dtype="float") / 255.0
        self.labelss = np.array(self.labelss)
        Printing.printProcess("[INFO] data matrix: {:.2f}MB".format(self.datas.nbytes / (1024 * 1000.0)))
    
    
    
    def __train(self):
        
        """
        Dividing the data into train, test and validition using 70% of
        the data for training and, 20% for test and 10% for validition for better performance.     
        """

        lb = LabelBinarizer() #binarize the labels
        self.labelss = lb.fit_transform(self.labelss) #Linear transformation

        (trainX, testX, trainY, testY) = train_test_split(self.datas,
        	self.labelss, test_size=0.2, random_state=42)
        (trainX, valX, trainY, valY) = train_test_split(trainX,
        	trainY, test_size=0.125, random_state=42)
     
        
        aug = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
	        height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	        horizontal_flip=True, fill_mode="nearest") # construct the image generator for data augmentation

        Printing.printProcess("[INFO] Compiling model...") # initialize the model
        model = MyModel.myModel.initbuild(width=self.IMAGEDIMS[1], height=self.IMAGEDIMS[0],
	    depth= self.IMAGEDIMS[2], classes=len(lb.classes_))
        
        opt = Adam(lr=self.INITLR, decay=self.INITLR / self.EPOCHS)
        
        model.compile(loss="categorical_crossentropy", optimizer=opt,
	        metrics=["accuracy"])
        
        model.summary()
        
        Printing.printProcess("[INFO] Training network...") # train the network
        
        H = model.fit_generator(
	    aug.flow(trainX, trainY, batch_size=self.BS),
	    validation_data=(valX, valY),
	    steps_per_epoch=len(trainX) // self.BS,
	    epochs=self.EPOCHS, verbose=2)
        

        
        Printing.printProcess('\n# Evaluate on test data') # Evaluate the model on the test data using evaluate
        results = model.evaluate(testX, testY, batch_size=32)
        print('test loss ' + str(results[0])  + ' , test acc ' + str(results[1]))        
        
        
        
        Printing.printProcess("[INFO] Serializing network...")# save the model
        model.save(self.modelpath)
    
       
        Printing.printProcess("[INFO] Serializing label binarizer...") # save the label binarizer 
        f = open(self.labelspath, "wb")
        f.write(pickle.dumps(lb))
        f.close()
        return H

    """
        Both graphs below gets the history and the path that the user chose to save the results in.
        then, they create an images that contains the graph. 
    """
    def __graph2(self, history, plot_path):
	    # plot loss
    
        plt.subplot(211)
        plt.title('Cross Entropy Loss')
        plt.plot(history.history['loss'], color='blue', label='train')
        plt.plot(history.history['val_loss'], color='orange', label='test')
	    # plot accuracy
        plt.subplot(212)
        plt.title('Classification Accuracy')
        plt.plot(history.history['accuracy'], color='blue', label='train')
        plt.plot(history.history['val_accuracy'], color='orange', label='test')
	    # save plot to file
        plt.savefig(plot_path)
        plt.close()
    
    
    
    def __graph1(self,H, plot_path):

        # plot the training loss and accuracy
        plt.style.use("ggplot")
        plt.figure()
        N = self.EPOCHS
        plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
        plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
        plt.plot(np.arange(0, N), H.history["accuracy"], label="train_acc")
        plt.plot(np.arange(0, N), H.history["val_accuracy"], label="val_acc")
        plt.title("Training Accuracy and Loss")
        plt.xlabel("Epoch #")
        plt.ylabel("Loss/Accuracy")
        plt.legend(loc="upper left")
        plt.savefig(plot_path)


    