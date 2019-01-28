# Dog or Cat?

The scope of this project is to create a classifier to predict if an image represents a Dog or a Cat.

**Dataset**

For this task, I have used the [Kaggle Dogs vs Cats dataset](https://www.kaggle.com/c/dogs-vs-cats/data).

The dataset comes in two folders, train and test.

If you want to make the training on your machine, you have to use the script `MovingFiles.py` to organize the training files in two subfolders, Dogs and Cats, and then launch the script `Train.py`

On a MacBook Air, the training required 2.5 hours to be completed.

On the other hand, you can use the model `DogCat.h5` already trained as explained in the Try It! section of this readme.

**ModelStructure**

![Link do classification report](https://github.com/marcogdepinto/Dogs-vs-Cats/blob/master/model.png)

# Languages and libraries used

- [Python 3.6](https://www.python.org/downloads/release/python-370/)
- Keras
- OpenCV
- Numpy

# Try it!

- `git clone https://github.com/marcogdepinto/Dogs-vs-Cats.git`

- Run the file `Predict.py` changing the `PATH` and `FILE` to the local path in which you have downloaded the model `DogCat.h5` and the example file `test.jpeg` (or any other file you want to use).