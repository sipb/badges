import django

class Badge:
    def __init__(self,name,badge_id,badge_type,rank,description,picture,\
        instructions,creator,date_created,secret=False):
        '''
        initializes a Badge instance
        '''
        self.name = name
        self.no = badge_id # should be assigned automatically
        self.btype = badge_type
        self.rank = rank
        self.desc = description
        self.pic = picture
        self.instr = instructions
        self.date = date_created # there should be a way to get this automatically
        self.creator = creator # this too if we integrate it with athena authentification
        self.secret = secret