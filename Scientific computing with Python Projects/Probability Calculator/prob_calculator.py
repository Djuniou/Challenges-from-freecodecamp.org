import copy
import random
# Consider using the modules imported above.

class Hat():
    def __init__(self,**hat):
        self.total_balls = 0
        self.contents = []
        self.__dict__.update(hat)
        for entry in hat:
            for value in range(hat[entry]):
                self.contents.append(entry)
                self.total_balls += 1        
       
    def draw(self,number):
        self.out_balls = []
        if (number<self.total_balls):
            for i in range(number): # number=number of balls to be taken out
                x=random.randint(0,len(self.contents)-1)
                self.out_balls.append(self.contents[x])
                self.contents.pop(x)            
            return self.out_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total_success = 0
    expected_list = []
    for entry in expected_balls:
        for value in range(expected_balls[entry]):
            expected_list.append(entry)
    for i in range(0,num_experiments):
        exp_hat = copy.deepcopy(hat)
        out_balls = exp_hat.draw(num_balls_drawn)    
        for k,item in enumerate(expected_list):
            if (item in out_balls):
                out_balls.remove(item)
                if (k==(len(expected_list)-1)):
                    total_success += 1            
            else:
                break    
    return (total_success/num_experiments)        
