# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 05:55:04 2023

@author: Maxim-Nt
"""

import pickle

class PickleStorage:
    def __init__(self, lodger):
        self.lodger = lodger
    
    def store(self):
        pickle.dump((self.lodger.maxID, self.lodger.items), open("data.dat", "wb"))
        
    def load(self):
        (self.lodger.maxID, self.lodger.items) = pickle.load(open("data.dat", "rb"))