'''
Created on 19 feb 2015

@author: Åke
'''
from abc import abstractmethod, ABCMeta

class DataSource():
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta
    @abstractmethod
    def getName(self):
        return str

    @abstractmethod
    def getUnit(self):
        return str

    @abstractmethod
    def getData(self):
        return dict