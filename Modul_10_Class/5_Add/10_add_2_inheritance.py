

class Person:
    name = None

    def greeting(self):
        print(f'I am {self.name}')


class Developer(Person):

    def do_job(self):
        print(f'I am writting code now...')


class Manager(Person):

    def manage(self):
        print('Deadlineis coming, hurry up!')


class TeamLead(Developer, Manager):

    def manage(self):
        print('I am TeamLead')
        return super().manage()


junior = Developer()

junior.name = 'Nike'

junior.greeting()       # I am Nike
junior.do_job()         # I am writting code now...


team_lead = TeamLead()

team_lead.name = 'Bob'
team_lead.greeting()    # I am Bob
team_lead.do_job()      # I am writting code now...
team_lead.manage()      # Deadlineis coming, hurry up   


