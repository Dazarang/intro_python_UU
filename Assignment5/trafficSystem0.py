
from statistics import mean, median
from time import sleep
import destinations
import trafficComponents as tc

class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self, lane1 = 5, lane2 = 5, period = 10, greenPeriod = 7):
        self.time = 0
        self.lane1 = tc.Lane(lane1)
        self.lane2 = tc.Lane(lane2)
        self.light = tc.Light(period, greenPeriod)
        self.destionation = destinations.Destinations()
        self.queue = []
        
    def snapshot(self):
        print(f'Time step {self.time}')
        print(f'{self.lane1}, {self.light}, {self.lane2}, '
                f'{[x.destination for x in self.queue]}')
    
    

    def step(self):
        self.time += 1
        
        self.lane1.remove_first()
        self.lane1.step()
        
        if self.light.is_green():
            v = self.lane2.remove_first()
            self.lane1.enter(v)
        
        self.light.step()
        self.lane2.step()
         
        dest = self.destionation.step()
        
        if dest != None:
            self.queue.append(tc.Vehicle(dest, self.time))
            
        if self.lane2.is_last_free() and len(self.queue) > 0:
            self.lane2.enter(self.queue.pop(0))

    def in_system(self):
        pass

    def print_statistics(self):
        pass

def main():
    ts = TrafficSystem()
    for i in range(50):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()
