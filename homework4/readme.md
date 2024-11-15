# Homework 4
This homework has been assigned in date 8th of November 2024.
We have been required to complete a series of tasks on a *basket-item* kind dataset:
1. Construct the matrix where one axis represents customers ( rows ) and one axis represents products ( columns ), each cells (i,j) holds the number of times a customer buys a product.
2. Normalize between integer 1 to 5.
3. Compute many customers clusters based on their normalized frequencies rows using either k-means or hierarchical, pick the one model with better quality.
4. Try to describe each cluster based on products or product categories the customers buy.

We have been offered a dataset of transactions owned by a third party, as I have no rights over it, I assume we are not allowed to share, please reach out our professors of *Introduction to Data Mining* at [this link](https://web.dmi.unict.it/courses/l-31/course-units/?seuid=8EAB2D3A-4281-40F4-83A0-C6B007577BA2) if interested.

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