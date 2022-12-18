import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.content_dict = {}
        self.content_dict.update(kwargs)
        self.contents = []
        
        for ball in self.content_dict:
            i = self.content_dict[ball]
            while i > 0:
                i-=1
                self.contents.append(ball)

    def draw(self, n):
        if n > len(self.contents):
            return self.contents

        draws = []
        while n > 0:
            i = random.randint(0, len(self.contents)-1)
            draws.append(self.contents.pop(i))
            n-=1
        return draws


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):    
    n = num_experiments
    num_correct = 0    
    
    while n > 0:
        hat_copy = copy.deepcopy(hat)
        draws = hat_copy.draw(num_balls_drawn)
        draws.sort()
        draws_freq = {}
        for draw in draws:
            if draw in draws_freq:
                draws_freq[draw] += 1
            else:
                draws_freq[draw] = 1
                
        expected = True
        i = 0
        for ball in expected_balls:
            if ball not in draws_freq:
                expected = False
                break
            if draws_freq[ball] < expected_balls[ball]:
                expected = False
                break

        if expected:
            num_correct += 1

        n-=1

    return num_correct / num_experiments