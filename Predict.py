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

# Here you can replace path and file with the path of your model and of the file from the RAVDESS dataset you want to use for the prediction,
# Below, I have used a neutral file: the prediction made is neutral.

pred = Predict(
    path='/Users/marcogdepinto/PycharmProjects/DogOrCat/DogCat.h5',
    file='/Users/marcogdepinto/PycharmProjects/DogOrCat/ImageToPredict/test.jpeg')

pred.load_model()
pred.makepredictions()