# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:48:25 2020

@author: NeoSixMan
"""

import numpy as np
import pandas as pd

wishList = pd.read_csv("wish_list.csv") #example data
wishList['product_id'] = wishList['product_id'].astype(str)
#wishList = wishList.set_index(['product_id'])
review_column = ['user_id','product_id', 'comment', 'vote']
#review = pd.DataFrame(columns=review_column)
review = pd.read_csv("reviews.csv") #last my reviews

def compute_vote(data, v):
    new_vote = (data['vote']*data['num_votes'] + v) / (data['num_votes'] + 1)
    #print(v, new_vote)
    return new_vote

command = ''

while(command != 'q'):
        command = input('add review(a), see review(r), see product(s), exit(q) :')        
        if command == 'a':
            name = str(input('Enter product name:'))
            data = wishList.loc[wishList['product_id'] == name]
            if data.empty:
                print('Can not find this product')
                continue

            comment = str(input('Enter comment: (Enter for blank) ' ))
            vote = str(input('Enter vote (1 - 5): (Enter for blank) '))
            try:
                vote = int(vote)
                if vote in [1, 2, 3, 4, 5]:
                    temp = pd.DataFrame([['1', name, comment, vote]], columns=review_column)
                    nv = compute_vote(data, vote)
                    wishList.loc[wishList['product_id'] == name, 'vote'] = nv
                    wishList.loc[wishList['product_id'] == name, 'num_votes'] = data['num_votes'] + 1
                else:
                    print('unpredicted vote => no vote')
                    #-1 for data prep
                    temp = pd.DataFrame([['1', name, comment, -1]], columns=review_column)
            except ValueError:
                print('no vote')
                #-1 for data prep
                temp = pd.DataFrame([['1', name, comment, -1]], columns=review_column)
            review = review.append(temp, ignore_index=True)
        elif command == 'r':
            print(review)
        elif command == 's':
            print(wishList)
        else:
            print('...')

review.to_csv('reviews.csv',index = False)
wishList.to_csv('wish_list.csv',index = False)
