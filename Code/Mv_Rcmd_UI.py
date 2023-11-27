import tkinter as tk
import pandas as pd
import pickle
mv_list=["new_1","new_2","new_3"]
df=pd.read_csv('data.csv', low_memory=False)
movie_titles=pd.read_csv('movie_titles.csv',encoding = 'ISO-8859-1', header = None, names = ['Id', 'Year', 'Name']).set_index('Id')

def get_recommendations(data, user_id, top_n, algo):
        recommendations = []
        user_item_interactions_matrix = data.pivot_table(index='userID', columns='itemID', values='rating')
        non_interacted_products = user_item_interactions_matrix.loc[user_id][user_item_interactions_matrix.loc[user_id].isnull()].index.tolist()
        for item_id in non_interacted_products:
            est = algo.predict(user_id, item_id).est
            recommendations.append((item_id, est))
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return get_movie_names(recommendations[:top_n])

def get_movie_names(recommendations):
        item_id_to_title = movie_titles['Name'].to_dict()
        recommended_movies = [item_id_to_title[item_id] for item_id, rating in recommendations]
        return recommended_movies

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Movie Recommender system")
        self.geometry("400x400")
        tk.Label(self, text="Movie Recommendation system").grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.user_id = tk.IntVar(value="0")
        tk.Entry(self, textvariable=self.user_id, width=12, justify=tk.RIGHT).grid(row=1, column=2, padx=5, pady=5)
        tk.Label(self, text="Enter the User ID: ").grid(row=1, column=1, sticky="w")
        tk.Button(self, text="Get Recommendation", command=self.disp_rcmd).grid(row=3, column=2, padx=5, pady=5)
        self.mv_lst = tk.Variable(value=mv_list)
        tk.Listbox(self,listvariable=self.mv_lst, height=10).grid(row=6, column=2, padx=5, pady=5)
 
    def disp_rcmd(self):
        mv_list.append(self.user_id.get())
        with open('svd_model.pkl','rb') as file:
            clf = pickle.load(file)
        new_list=get_recommendations(df, self.user_id.get(), 10, clf)
        self.mv_lst = tk.Variable(value=new_list)
        tk.Listbox(self,listvariable=self.mv_lst, height=10,width=50).grid(row=6, column=2, padx=5, pady=5)
        
MainWindow().mainloop()
