# Movie Recommendation Systen

# Required Libraries
Surprise - Suprise is a python library created for predicting the ratings for movies. Install the Library using
pip install Surprise

# Code
train.ipynb contains the code for training the models
1. User User Similarity - Calculating the cosine similarity between the users and using KNN to cluster similar users toghether

2. Matrix Factorization - Model based collabrative filtering using SVD Matrix Factorization

3. CoClustering - Clustering based on users and movies to find relationship between them

The trained model .pkl files have been uploaded https://drive.google.com/drive/folders/1d9itRYdyaLPf4iIRUKZIoYVJT_lWNpbr?usp=drive_link since they are of a large size

# Data
The model has been trained upon Netflix Prize Dataset which can be found on https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data.
Data Preprocessing - within the dataset movie_titles.csv requires preprocessing since some of the movie names have "," within the name and also aas the delimiter. The pre processed movie_titles.csv can be found within the Data Folder. The dataset has also been uploaded to drive which can be found here https://drive.google.com/drive/folders/1d9itRYdyaLPf4iIRUKZIoYVJT_lWNpbr?usp=drive_link

# Evaluations
