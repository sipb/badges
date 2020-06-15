import django

class Person:
    def __init__(self,kerberos,name,graduation_year,achievement_list):
        '''
        initializes a Person instance
        '''
        self.kerb = kerberos
        self.name = name
        self.year = graduation_year
        self.achs = achievement_list