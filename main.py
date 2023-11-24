# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 05:53:08 2023

@author: Maxim-Nt
"""

from Lodger import Lodger

def main():
    lodger = Lodger()
    
    menu = [
        ["Добавить", lodger.add],
        ["Удалить", lodger.delete],
        ["Показать", lodger.write],
        ["Сохранить", lodger.store],
        ["Загрузить", lodger.load],
    ]

    while True:
        for i,menuItem in enumerate(menu, 1):
            print(f"{i}. {menuItem[0]}")
        m = int(input())
        menu[m-1][1]()

main()