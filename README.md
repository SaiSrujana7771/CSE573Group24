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
We employed various evaluation metrics to assess the performance of the recommendation system. The results we obtained are represented in the following table: 

| Metricss        | User-User           | Model-Based  | Cluster-Based   | 
| -------------   |:-------------:      | -----:       | -----:          |
| RMSE            | 0.9423              | 0.6865       | 0.9475          |
| MAE             | 0.77374             | 0.5531       | 0.7325          |
| Precision       | 0.934               | 0.939        | 0.934           |
| Recall          | 0.98                | 0.98         | 0.975           |
| F-1 Score       | 0.956               | 0.959        | 0.954           |

The evaluation of three collaborative filtering algorithms—User Similarity Collaborative Filtering, Model-Based Collaborative Filtering, and Cluster-Based Collaborative Filtering—reveals diverse performances in the movie recommendation system. The Model-Based Collaborative Filtering algorithm emerges as the most accurate and effective, while the User Similarity Collaborative Filtering model portrays competitive performance, and the Cluster-Based Collaborative Filtering model maintains reliability despite moderate accuracy metrics, providing nuanced options for real-world deployment based on specific system requirements.
