import numpy as np
import pandas as pd
import json
class WishList():
    def __init__(self):
        self.common = json.load("CommonFrame.json") #example data
        self.wishlist = json.load("WishlistFrame.json") #example data


    def add(self, id, name):

        row = self.common.loc[self.common['product_id'] == id]

        if row.empty:
            print('Cannot find this product')
            return
        check = self.wishlist.isin({'product_id': [id]})

        if check['product_id'].any(axis=None) == False:
            temp = pd.DataFrame([[id, name]], columns=['product_id','product_name'])
            self.wishlist = self.wishlist.append(temp, ignore_index=True)
        else:
            print('already add')


    def dispaly(self):
        print(self.wishList)

    def remove(self):
        name = str(input('Enter remove name:'))
        self.wishList = self.wishList[self.wishList.names != name]

    def save(self):
        self.wishlist.to_json('WishlistFrame.json')
        self.common.to_json('CommonFrame.json')