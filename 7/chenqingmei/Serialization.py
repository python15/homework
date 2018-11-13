#!/bin/python3.6

import pickle
import json
import msgpack


class SerializationMixin:
    def to_dict(self,type = 'json'):
        '''
        serialization, give str value to type. In order to get dict type result, set type as 'json'
        :param type: serialize type, support pickle, json, msgpack at present
        :return:
        '''
        if type == 'json':
            return json.dumps(self.__dict__)
        elif type == 'msgpack':
            return msgpack.packb(self.__dict__)
        elif type == 'pickle':
            return pickle.dumps(self.__dict__)
        else:
            raise ('cannot serialize!')




class Book:
    def __init__(self, title, author, publishing, page):
        self.__title = title
        self.__author = author
        self.__publishing = publishing
        self.__page = page

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @property
    def publishing(self):
        return self.__publishing

    @publishing.setter
    def publishing(self, value):
        self.__publishing = value

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, value):
        self.__page = value



class SerializationBook(SerializationMixin, Book):
    pass

book = SerializationBook('Pride and Prejudice', 'Jane Austen', '28-01-1813', 2000)

d = book.to_dict('json')
print(d)