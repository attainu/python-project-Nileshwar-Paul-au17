from file_car import Car 

class Parking:
    
    def __init__(self):

        self.slots = float('inf')
        self.slotNo = 0
        self.used_slots = 0
        
    
    def create_parking(self,n):
        
        self.slots = [0] * n
        print(f"\n {n} Parking slots Created \n")
        
        self.total_slots = n
        
        return  self.total_slots
    
    
    def empty_slots(self):

        for idx in range(len(self.slots)):
            
            if self.slots[idx] == 0:
                
                return idx
        return -1
    
    
    def park_car(self,rgno,color):

        if self.used_slots < self.total_slots:

            self.slotno = self.empty_slots()
            self.slots[self.slotno]=Car(rgno,color)
            self.used_slots+=1
            self.slotno+=1
            return self.slotno
        else:
            
            print("ParkingSlot Not Available")
            return -1
    
    
    def free_slot(self,slotno):

        if self.used_slots > 0 and self.slots[slotno-1] != 0 :

            self.slots[slotno-1] = 0
            self.used_slots -= 1

            return True

        else:
             return False

    def display(self):

        print("SlotNo.\tRgNo.\tColour")

        for i in range(len(self.slots)):

            if self.slots[i] != 0 :

                print(f"{i+1} \t\t {self.slots[i].RgNo} \t\t {self.slots[i].Color}")
            
            else:
                
                continue 
        

    
    

    def display_slotno_by_color(self,color):

        slotno = []

        for i in range(len(self.slots)):

            if i == 0:

                continue
            
            if self.slots[i].Color == color :

                slotno.append(i+1)
        
        return slotno



    def display_rgno_by_color(self,color):

        regs=[]

        for i in self.slots:

            if i == 0:

                continue
            
            if i.Color == color :
                regs.append(i.RgNo)
        

        return regs

    def display_slotno_by_regno(self,rgno):


        for i in range(len(self.slots)):
            if i == 0:

                continue
            
            if self.slots[i].RgNo == rgno:

                return i+1
        
        return -1
    


if __name__ == "__main__":

    p=Parking()
    p.create_parking(6)
    
    print(p.empty_slots())
    p.park_car("HR-07Y-1234","Black")
    print(p.empty_slots())
    p.park_car("DL-08T-0010","White")
    print(p.empty_slots())
    p.park_car("KA-9OP-8503","White")
    print(p.empty_slots())
    p.park_car("DL-05A-8456","Blue")
    print(p.empty_slots())
    p.park_car("HP-0RF-8966","Red")
    print(p.empty_slots())
    p.park_car("PB-09U-4444","Green")
    
    print(p.empty_slots())
    p.park_car("UP-05A-0001","Yellow")
    
    p.display()
    p.free_slot(3)
    p.display()
    p.park_car("Jk-09I-8900","Red")
    p.display()

    print(p.display_rgno_by_color("Red"))

    print(p.display_slotno_by_color("Red"))

    print(p.display_slotno_by_regno("DL-05A-8456"))

    