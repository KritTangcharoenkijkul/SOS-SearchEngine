import numpy as np
import pandas as pd


common_column = ['product_id','product_name', 'num_vote', 'vote']
temp = pd.DataFrame([['1', 'a', 0, 0], ['1', 'b', 0, 0], ['1', 'c', 0, 0], ['1', 'd', 0, 0]], columns=common_column)
common = pd.DataFrame(columns=common_column)
common = common.append(temp, ignore_index=True)
common.to_json ('CommonFrame.json')


wishlist_column = ['product_id','product_name']
wishlist = pd.DataFrame(columns=wishlist_column)
wishlist = wishlist.append(temp, ignore_index=True)
wishlist.to_json ('WishlistFrame.json')

review_column = ['user_name', 'user_id', 'star', 'comment', 'product_id', 'product_name']
review = pd.DataFrame(columns=review_column)
review = review.append(temp, ignore_index=True)
review.to_json ('ReviewFrame.json')