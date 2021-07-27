from file_car import Car 



class Parking:
    
    def __init__(self):

        self.Slots = float('inf')
        self.SlotNo = 0
        self.Used_slots = 0
        
    
    def create_parking(self,n):
        
        self.Slots = [0] * n
        print(f"\n {n} Parking Slots Created \n")
        
        self.TotalSlots = n
        #return self.TotalSlots 
    
    def empty_slots(self):

        for idx in range(len(self.Slots)):
            
            if self.Slots[idx] == 0:
                
                return idx

    def park_car(self,RgNo,Color):

        if self.Used_slots < self.TotalSlots:

            SlotNo = self.empty_slots()
            self.Slots[self.SlotNo]=Car(RgNo,Color)
            self.Used_slots+=1

        else:
            
            return "ParkingSlot Not Available"

if __name__ == "__main__":

    #p=Parking()
    #p.create_parking(6)
    #print(p.empty_slots())
    #p.park_car("DL-05A-8456","White")



