# -*- coding: utf-8 -*-
import pandas as pd 

unames=['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('c:/workpy/movies/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('c:/workpy/movies/ratings.dat', sep='::', header=None,names=rnames)

mnames=['movie_id', 'title', 'genres']
movies=pd.read_table('c:\workpy/movies/movies.dat', sep='::',header=None, names=mnames)

users[:5]

rating[:5]

movies[:5]

ratings


data = pd.merge(pd.merge(ratings, users), movies)
data

data.ix[0]

mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
mean_ratings[:5]

ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles 

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings[:10]

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[:15]
sorted_by_diff[::-1][:15]



