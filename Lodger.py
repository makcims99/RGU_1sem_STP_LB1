# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 05:55:58 2023

@author: Maxim-Nt
"""

from PS import PickleStorage
from LodgerItem import LodgerItem

class Lodger:
    def __init__(self):
        self.items = dict()
        self.storage = PickleStorage(self)
        self.maxID = 0
        
    def add(self):
        self.maxID += 1
        item = LodgerItem(id=self.maxID)
        item.read()
        self.items[item.id] = item

    def write(self):
        for id, item in self.items.items():
            item.write()

    def store(self):
        self.storage.store()

    def load(self):
        self.storage.load()

    def delete(self):
        id = int(input("id: "))
        del self.items[id]