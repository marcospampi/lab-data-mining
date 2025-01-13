# Homework 5
# Sixth Classwork/Homework
We have been tasked to use Convolutional Neural Networks to procduce a celebrity recognition model.  
There are a total of two tasks:
1. Split the dataset in train test and test set.
2. Implement a Convolutional Neural Network (CNN), that make a classification of the celebrity. Therefore, you need to use the train set to do the training operation, and the test setto check if the neural network is able to correctly classify the picture given in input.

The dataset is downloadable from [here](https://drive.google.com/drive/folders/1TmwPJGLYzYuLXhfKoewPJooNVMZunJXq?usp=sharing).

Most of the work's been made by folling [PyTorch's own tutorial](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html), ChatGPT has been used to better explain most of the stuff left to faith there.
### Notes
We have been required to follow an object-oriented approach, my work doesn't stricly follow this requirements as a jupyter notebook is provided.

I did my best not to put any verbose or annoying code in this notebook.

### Prerequisites
Install requirements fro requirements.txt
```sh
pip install -r requirements.txt
```
Create `.env` file:
```
TASK_DATASET_FILE_PATH = <path_to_your_dataset_file>
```