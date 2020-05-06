# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:58:15 2020

@author: NeoSixMan
"""

import numpy as np
import pandas as pd

insurance = pd.read_csv("insurance.csv") #all data
insurance['product_id'] = [str(i) for i in range(1, insurance.shape[0]+1)] #int
insurance['product_id'] = insurance['product_id'].astype(str) #str
insurance['vote'] = [0 for i in range(1, insurance.shape[0]+1)]
insurance['num_votes'] = [0 for i in range(1, insurance.shape[0]+1)]
#wishList = pd.DataFrame(columns=insurance.columns)
wishList = pd.read_csv("wish_list.csv") #last my wish lish

command = ''

while(command != 'q'):
        command = input('add (a), see (s), remove (r), exit (q) :')        
        if command == 'a':
            name = str(input('Enter product name:'))
            row = insurance.loc[insurance['product_id'] == name]
            check = wishList.isin({'product_id': [name]})
            if check['product_id'].any(axis=None) == False:
                wishList = wishList.append(row)
            else:
                print('already add')
        elif command == 's':
            print(wishList)
        elif command == 'r':
            name = str(input('Enter remove name:'))
            wishList = wishList[wishList.names != name]
        else:
            print('...')
            
wishList.to_csv('wish_list.csv',index = False)