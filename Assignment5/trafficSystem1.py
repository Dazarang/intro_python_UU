
from statistics import mean, median
from time import sleep
import destinations
import trafficComponents as tc


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        self.time = 0
        
        self.destination = destinations.Destinations()
        
        self.lane1 = tc.Lane(11)
        self.laneW = tc.Lane(8)
        self.laneS = tc.Lane(8)
        
        self.lightW = tc.Light(14, 6)
        self.lightS = tc.Light(14, 4)
        
        self.queue = []
        self.showQueue = []
        self.amountQueue = 0 
        
        self.vehicleCount = 0
        self.blockedCount = 0
        self.laneBlocked = False
        
        
        self.wInSysTime = []
        self.sInSysTime = []
        


    def snapshot(self):
        print(f'Time step {self.time}')
        if self.laneBlocked:
            print(f'{self.lightW} {self.laneW}*{self.lane1} {self.showQueue}\n'
                    f'{self.lightS} {self.laneS}')
        else:
            print(f'{self.lightW} {self.laneW} {self.lane1} {self.showQueue}\n'
                    f'{self.lightS} {self.laneS}')

    def step(self):
        self.time += 1
        
        ### Move vehicles S or W depending on light ###
        
        if self.lightW.is_green():
            vehicle = self.laneW.remove_first()
            
            if vehicle != None:
                self.wInSysTime.append(self.time - vehicle.borntime)
                
        if self.lightS.is_green():
            vehicle = self.laneS.remove_first()
            
            if vehicle != None:
                self.sInSysTime.append(self.time - vehicle.borntime)
                
        self.laneW.step()
        self.laneS.step()
        self.lightW.step()
        self.lightS.step()
        
        ### Fill S or W from Lane depending on destination ###
        
        if self.lane1.get_first() != None:
            if self.lane1.get_first().destination == "W" and self.laneW.is_last_free():
                self.laneW.enter(self.lane1.remove_first())
                self.laneBlocked = False
            elif self.lane1.get_first().destination == "S" and self.laneS.is_last_free():
                self.laneS.enter(self.lane1.remove_first())
                self.laneBlocked = False
            else: 
                self.laneBlocked = True
                self.blockedCount += 1
        
        self.lane1.step()
        
        ### Queue at point E and store destination ###
        
        dest = self.destination.step()
        
        if dest != None:
            self.queue.append(tc.Vehicle(dest, self.time))
            self.showQueue.append(dest)
            self.vehicleCount += 1
        
        if self.lane1.is_last_free() and len(self.queue) > 0:
            self.lane1.enter(self.queue.pop(0))
            self.showQueue.pop(0)
            
        if len(self.queue) > 0:
            self.amountQueue += 1

    def in_system(self):
        return (self.lane1.number_in_lane() + self.laneW.number_in_lane() + 
                self.laneS.number_in_lane() + len(self.queue))

    def print_statistics(self):
        vOutW, vOutS = len(self.wInSysTime), len(self.sInSysTime)
        
        minTimeW, minTimeS = min(self.wInSysTime), min(self.sInSysTime)
        
        maxTimeW, maxTimeS = max(self.wInSysTime), max(self.sInSysTime)
        
        meanTimeW, meanTimeS = round(mean(self.wInSysTime), 1), round(mean(self.sInSysTime), 1)
        
        medianTimeW, medianTimeS = round(median(self.wInSysTime), 1), round(median(self.sInSysTime), 1)
        
        blocked = round((self.blockedCount/self.time)*100, 2)
        q = round((self.amountQueue/self.time)*100, 2)
        
        print(f"Statistics after {self.time} steps: ")
        print()
        print(f'Created vehicles: {self.vehicleCount}')
        print(f'In system\t: {self.in_system()}')
        print()
        print("At exit\t\t\t West \t\t\t South")
        print(f'Vehicles out\t: \t {vOutW}\t\t\t {vOutS}')
        print(f'Minimal time\t: \t {minTimeW}\t\t\t {minTimeS}')
        print(f'Maximal time\t: \t {maxTimeW}\t\t\t {maxTimeS}')
        print(f'Mean time\t: \t {meanTimeW}\t\t\t {meanTimeS}')
        print(f'Median time\t: \t {medianTimeW}\t\t\t {medianTimeS}')
        print(f'Blocked\t\t: \t\t {blocked} %')
        print(f'Queue\t\t: \t\t {q} %')


def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()
