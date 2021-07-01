"""
by Topaz Ben Atar
"""
"""
this file contain a class with a static method
this method declared the model layers
"""
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K
from keras.utils.vis_utils import plot_model

class myModel:
    @staticmethod
    def initbuild(width, height, depth, classes, finalAct="softmax"):
        """
        Get: the imaged dims, the categories, the final activation function - by defual "softmax"
        it first,  initialize the model along with the input shape to be
		"channels last" and the channels dimension itself
        """
        chanDim = -1
        model = Sequential()
        inputShape = (height, width, depth)

		# if we are using "channels first", update the input shape
		# and channels dimension
        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)
            chanDim = 1

		# CONV => RELU => POOL
        model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(3, 3)))
        model.add(Dropout(0.25))

		# (CONV => RELU) * 2 => POOL
        model.add(Conv2D(64, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(64, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

		# (CONV => RELU) * 2 => POOL
        model.add(Conv2D(128, (3, 3), padding="same"))
        
        #model.add(Dropout(0.25))

        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(Conv2D(128, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(BatchNormalization(axis=chanDim))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
        

		# first (and only) set of FC => RELU layers
        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Activation("relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.5))

		# softmax classifier
        model.add(Dense(classes))
        model.add(Activation(finalAct))
#        plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

		# return the constructed network architecture
        return model