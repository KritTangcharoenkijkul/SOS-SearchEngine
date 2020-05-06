import numpy as np
import pandas as pd

class Review():
    def __init__(self):
        self.data = pd.read_csv("insurance.csv") #example data
        self.data['product_id'] = self.data['product_id'].astype(str)
        #wishList = wishList.set_index(['product_id'])
        self.review_column = ['user_id','product_id', 'comment', 'vote']
        #review = pd.DataFrame(columns=review_column)
        self.review = pd.read_csv("reviews.csv") #last my reviews

    def add(self):
        name = str(input('Enter product name:'))
        data = self.data.loc[self.data['product_id'] == name]
        if data.empty:
            print('Can not find this product')
            return

        comment = str(input('Enter comment: (Enter for blank) ' ))
        vote = str(input('Enter vote (1 - 5): (Enter for blank) '))
        try:
            vote = int(vote)
            if vote in [1, 2, 3, 4, 5]:
                temp = pd.DataFrame([['1', name, comment, vote]], columns=self.review_column)
                nv = self.compute_vote(data, vote)
                self.data.loc[self.data['product_id'] == name, 'vote'] = nv
                self.data.loc[self.data['product_id'] == name, 'num_votes'] = data['num_votes'] + 1
            else:
                print('unpredicted vote => no vote')
                #-1 for data prep
                temp = pd.DataFrame([['1', name, comment, -1]], columns=self.review_column)
        except ValueError:
            print('no vote')
            #-1 for data prep
            temp = pd.DataFrame([['1', name, comment, -1]], columns=self.review_column)
        self.review = self.review.append(temp, ignore_index=True)

    def dispaly_review(self):
        print(self.review)

    def dispaly_data(self):
        print(self.data)

    def save(self):
        self.review.to_csv('reviews.csv',index = False)
        self.data.to_csv('insurance.csv',index = False)

    def compute_vote(self, data, v):
        new_vote = (data['vote']*data['num_votes'] + v) / (data['num_votes'] + 1)
        #print(v, new_vote)
        return new_vote

r = Review()
r.dispaly_review()
r.save()