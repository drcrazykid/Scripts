import uuid

class Player:

    def __init__(self,first="",last="",dupr=0.0,phone="(###) ###-####",player_id = "",wins = 0, losses = 0):
        self.fn = str(first).capitalize()
        self.ln = str(last).capitalize()
        
        self.rating = dupr
        self.phone_num = phone
        if player_id == "":
            self.unique_id = self.id_gen()
        else:
            self.unique_id = player_id
        self.wins = wins
        self.losses = losses
    
    def id_gen(self):
        return uuid.uuid4().hex[:7].upper()
    
    def full_name(self):
        return f"{self.fn} {self.ln}"

    def record(self):
        return f"{self.wins}-{self.losses}"

    def get_info(self):
        for k,v in self.__dict__.items():
            print(f"{k.capitalize()}: {v}")
            
    
    def __str__(self):
        return "\n".join(f"{k.capitalize()}: {v}" for k,v in self.__dict__.items())
    
    def update_record(self,winorloss:int):
        if winorloss == 1:
            self.wins += 1
        elif winorloss == -1:
            self.losses += 1