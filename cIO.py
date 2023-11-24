# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 05:55:37 2023

@author: Maxim-Nt
"""

class ConsoleIO:
    def input(self, field, defvalue=None):
        return input(f"{field}: ")
    
    def output(self, fio, field):
        print(f"{fio}: {field}")