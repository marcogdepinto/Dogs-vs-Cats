import keras
import cv2
import numpy as np

class Predict:

    def __init__(self, path, file):

        self.path = path
        self.file = file

    def load_model(self):
        '''
        I am here to load you model.
        '''
        self.loaded_model = keras.models.load_model(self.path)
        return self.loaded_model

    def makepredictions(self):
        '''
        I am here to process the files, create your features and make predictions
        '''

        img = cv2.imread(self.file)
        img = cv2.resize(img, (64, 64))
        img = np.reshape(img, [1, 64, 64, 3])
        print("File loaded and reshaped. The new shape is ", img.shape)
        print("Start predicting...")
        predictions = self.loaded_model.predict_classes(img)

        # Converting output to human readable labels

        if predictions == 0:
            predictions = 'Cat'
        elif predictions == 1:
            predictions = 'Dog'

        print( "Prediction completed: this is a", predictions)

# Below you should change the variable as follows:
# the `PATH` variable should be the local path in which you have downloaded the model `DogCat.h5`
# the `FILE` variable should be the path to the example file `test.jpeg` (or any other file of Dog or Cat you want to use).

pred = Predict(
    path='/Users/marcogdepinto/PycharmProjects/DogOrCat/DogCat.h5',
    file='/Users/marcogdepinto/PycharmProjects/DogOrCat/ImageToPredict/test.jpeg')

pred.load_model()
pred.makepredictions()