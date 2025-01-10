# Homework 5
It's been tasked to accomplish the following tasks, about classification, on a medical dataset about children's intellectual disabilities test:
1. Draw a 2D scatter plot of the dataset.
2. Split the dataset in train and test set.
3. Implement a proxy class that can accept any given classification algorithm and its parameters to be fed to a GridSearchCV object so to find the best hyperparameters for the best model.
    - Use Decision Tree, Random Forest, SVC and K-NN as classification algorithms.
4. Experiment with Boosting and Bagging ideas.

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