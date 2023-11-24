# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 05:54:34 2023

@author: Maxim-Nt
"""
from dataclasses import dataclass
import datetime
from cIO import ConsoleIO


@dataclass
class LodgerItem:
    id: int = 0
    fio: str = ""
    room: str = ""
    count: str = ""
    child: str = ""
    time = 0
    
    
    def __post_init__(self):
        self.time = datetime.datetime.now()
        self.io = ConsoleIO()
        
    def read(self):
        self.fio = self.io.input('fio')
        self.room = self.io.input('room')
        self.count = self.io.input('count')
        self.child = self.io.input('child')
        
    def write(self):
        self.io.output('ID', self.id)
        self.io.output('FIO', self.fio)
        self.io.output('Room', self.room)
        self.io.output('Count', self.count)
        self.io.output('Child', self.child)
        self.io.output('Time', self.time)
        