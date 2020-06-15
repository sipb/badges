import django

class Achievement:
    def __init__(self,ach_id,badge_id,circumstances,awarder):
        '''
        initializes an Achievement instance
        '''
        self.ach_id = ach_id # to be assigned automatically
        self.badge = badge_id
        self.circumstances = circumstances # description of how they got it
        self.awarder = awarder # to be automated
        self.status = "just awarded" # shows progress of physical badge