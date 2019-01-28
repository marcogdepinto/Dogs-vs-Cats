# Dog or Cat?

The scope of this project is to create a classifier to predict if an image represents a Dog or a Cat.

**Dataset**

For this task, I have used the [Kaggle Dogs vs Cats dataset](https://www.kaggle.com/c/dogs-vs-cats/data).

If you want to make the training on your machine, you have to use the script `MovingFiles.py` to organize the training files in two subfolders, Dogs and Cats, and then launch the script `Train.py`
(because the dataset comes splitted only in two folders, train and test): on a MacBook Air, the training required 2.5 hours to be completed.

On the other hand, if you want to skip the training part, you can use the model `DogCat.h5` as explained in the Try It! section of this readme.

**ModelStructure**

![Link do classification report](https://github.com/marcogdepinto/Dogs-vs-Cats/blob/master/model.png)

# Languages and libraries used

- Python 3.6
- Keras
- OpenCV
- Numpy

# Try it!

- `git clone https://github.com/marcogdepinto/Dogs-vs-Cats.git`

- Run the file `Predict.py` changing:
    - the `PATH` variable to he local path in which you have downloaded the model `DogCat.h5`
    - the `FILE` variable to the path to the example file `test.jpeg` (or any other file of Dog or Cat you want to use).