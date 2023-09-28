"""
Цей магічний метод отримує на вхід словник, розпакований з файлу або byte-рядка. 
Поведінка за замовчуванням — це записати отримане значення в self.__dict__. 
Доопрацюймо клас Reader так, щоб він міг після розпакування продовжити читання 
з того самого місця.
"""

import pickle


class Reader:

    def __init__(self, file: str) -> None:
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self) -> None:
        self.fh.close()

    def read(self, size: int=1) -> str:
        data = self.fh.read(size)
        self.position = self.fh.tell()

        return data
    
    def __getstate__(self) -> dict:
        attributes = {**self.__dict__}
        attributes['fh'] = None

        return attributes
    
    def __settable__(self, value: dict) -> None:
        self.__dict__ = value
        self.fh.open(value['file'])
        self.fh.seek(value['position'])
    
    