"""
Магічний метод __getstate__ викликається, коли pickle намагається отримати 
представлення об'єкта у вигляді byte-рядка. 

У звичайній реалізації __getstate__ повертає __dict__ словник, де 
зберігаються всі атрибути класу. Але ви можете змінити цей метод.
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
        attributes = self.__dict__.copy()
        attributes['fh'] = None

        return attributes
    
    