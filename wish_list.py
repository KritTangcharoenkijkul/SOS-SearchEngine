import numpy as np
import pandas as pd

class WishList():
    def __init__(self):
        self.insurance = pd.read_csv("insurance.csv") #example data
        self.insurance['product_id'] = [str(i) for i in range(1, self.insurance.shape[0]+1)] #int
        self.insurance['product_id'] = self.insurance['product_id'].astype(str) #str
        self.insurance['vote'] = [0 for i in range(1, self.insurance.shape[0]+1)]
        self.insurance['num_votes'] = [0 for i in range(1, self.insurance.shape[0]+1)]
        #wishList = pd.DataFrame(columns=insurance.columns)
        self.wishList = pd.read_csv("wish_list.csv") #last my wish lish

    def add(self):
        name = str(input('Enter product name:'))
        row = self.insurance.loc[self.insurance['product_id'] == name]
        if row.empty:
            print('Can not find this product')
            return
        check = self.wishList.isin({'product_id': [name]})
        if check['product_id'].any(axis=None) == False:
            self.wishList = self.wishList.append(row)
        else:
            print('already add')

    def dispaly(self):
        print(self.wishList)

    def remove(self):
        name = str(input('Enter remove name:'))
        self.wishList = self.wishList[self.wishList.names != name]

    def save(self):
        self.wishList.to_csv('wish_list.csv',index = False)

w = WishList()
w.dispaly()