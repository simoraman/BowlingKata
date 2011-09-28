
class Game:
    def __init__(self):
        self.rolls=[0]*21
        self.current_roll=0
        
    def roll(self,  pins):
        self.rolls[self.current_roll]=pins
        self.current_roll+=1
    
    def score(self):
        _score=0
        frame_index=0
        frame=0
        
        while frame<10:
            if self.is_spare(frame_index):
                _score+=10+self.rolls[frame_index+2]
            else:
                _score+=self.rolls[frame_index]+self.rolls[frame_index+1]
            frame_index+=2
            frame+=1
        return _score
        
    def is_spare(self,  frame_index):
        return self.rolls[frame_index]+self.rolls[frame_index+1] == 10
