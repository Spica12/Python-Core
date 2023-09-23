from collections import deque, UserList
from datetime import datetime

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Doctor(Person):

    def __init__(self, name, surname, position):
        super.__init__(name, surname)
        self.position = position

    def add(self, patient, desiese_name):
        des = Desiese(desiese_name, ' '.join((self.name, self.surname)))
        patient.story.__Story__add(des)

    def treat(self, patient, desiese_name, treatment):
        patient.story[desiese_name].treat(treatment)


class Patient(Person):

    def __init__(self, name, surname, polis):
        super.__init__(name, surname)
        self.polis = polis
        self.story = None #TODO class Story

    def healthy(self):
        return self.story.healthy
    
class NoRight:
    pass

class Story(UserList):
    story_size = 10

    def __init__(self):
        self.__data = deque([], self.story_size)
        self.__data_dict = dict()
        self.data = list()

    def __getitem__(self, key=None):
        if key is None:
            return list(self.__data)
        if isinstance(key, int):
            return self.__data[key]
        elif isinstance(key, str):
            return self.__dict.get[key]
        
    def __len__(self):
        return __len(self.__data)
    
    def add(self, *_):
        raise NoRight   #TODO class NoRight
    
    def __add(self, desiee):
        self.__data. append(desiee)
        self.__data_dict = {des.name: des for des in self.__data}
        self.data = [des for des in self.__data]

    def healthy(self):
        return all([desiese.cured for ])






class Desiese:

    def __init__(self, name, doctor):
        self.name = name
        self.doctor = doctor
        self.treatment = list()
        self.time = datetime.now()
        self.cured = False
        self.cure = None
    
    def cure(self):
        self.cured = True
        self.cure_time = datetime.now()

    def treat(self, treatment):
        self.treatment.append(treatment)