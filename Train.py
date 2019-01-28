from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.callbacks import EarlyStopping
import os

callback = [EarlyStopping(monitor='loss', patience=0, verbose=1)]

classifier = Sequential()

classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Conv2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Flatten())

classifier.add(Dense(128, activation='relu'))
classifier.add(Dense(1, activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Printing model

from keras.utils import plot_model
plot_model(classifier, to_file='model.png', show_shapes=True)

# Processing images

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,
 shear_range=0.2,
 zoom_range=0.2,
 horizontal_flip=True)

train_data_dir = '/Users/marcogdepinto/PycharmProjects/DogOrCat/data/train/'
test_data_dir = '/Users/marcogdepinto/PycharmProjects/DogOrCat/data/test/'

test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(train_data_dir,
 target_size=(64, 64),
 batch_size=32,
 class_mode='binary')
test_set = test_datagen.flow_from_directory(test_data_dir,
 target_size=(64, 64),
 batch_size=32,
 class_mode='binary')

classifier.fit_generator(training_set,
 steps_per_epoch=4000,
 epochs=5,
 validation_data=test_set,
 validation_steps=1000,
 callbacks=callback)

model_name = 'DogCat.h5'
save_dir = '/Users/marcogdepinto/PycharmProjects/DogOrCat/'
# Save model and weights
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
model_path = os.path.join(save_dir, model_name)
classifier.save(model_path)
print('Saved trained model at %s ' % model_path)