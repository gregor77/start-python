# -*- coding: utf-8 -*-
import pandas as pd 
names1880 = pd.read_csv('c:\workPy\yob1880.txt', names=['names','sex','births'])
names1880

names1880.groupby('sex').births.sum()

#하나로 합치는 작업을 한다.
years = range(1880, 2011)

pieces = []
columns = ['name','sex','births']

for year in years:
    path='c:\workPy\yob%d.txt' % year
    frame=pd.read_csv(path, names=columns)
    
    frame['year'] = year
    pieces.append(frame)
    
names = pd.concat(pieces, ignore_index=True)

names 

#이제 이 데이터에 groupby나 pivot_table을 이용해서 연도나 성별에 따른 데이터를 수집한다. 
total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
total_births.tail()

total_births.plot(title='Total births by sex and year')


def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year','sex']).apply(add_prop)

names

np.allclose(names.groupby(['year', 'sex']).prop.sum(),1)

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]
    
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

top1000

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births', rows='year', cols='name', aggfunc=sum)
total_births
subset = total_births[['John', 'Harry', "Mary', "Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")
