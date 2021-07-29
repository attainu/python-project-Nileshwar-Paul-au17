import sys
from file_car import Car 


class Parking:
    
    def __init__(self):

        self.slots = float('inf')
        self.slotNo = 0
        self.used_slots = 0
        self.n = 0
        
    
    def create_parking(self,n):
        
        self.n = n
        self.slots = [0] * n
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
            print(f"Slot Number {self.slotno} Alloted")
            return self.slotno

        else:
            
            print("ParkingSlot Not Available")
            return 
    
    
    def free_slot(self,slotno):
        
        if self.used_slots > 0 and self.slots[slotno-1] != 0 :

            self.slots[slotno-1] = 0
            self.used_slots -= 1
            print(f"Slot Number {slotno} is Free")
            return 
        
        else:
             print("Enter wrong slot number")
             return 

    
    def display(self):

        print("SlotNo.\t\tRgNo.\t\t\tColour")

        for i in range(len(self.slots)):

            if self.slots[i] != 0 :

                print(f"{i+1} \t\t{self.slots[i].RgNo} \t\t {self.slots[i].Color}")
            
            else:
                
                continue 
        

    def display_slotno_by_color(self,color):

        slotno = []

        for i in range(len(self.slots)):

            if self.slots[i] == 0:

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
        
        if len(regs) != 0:

            print(regs)
        
        else:
            print("Not Found")
        
        return


    def display_slotno_by_regno(self,rgno):


        for i in range(len(self.slots)):
            if self.slots[i] == 0:
                continue

            elif self.slots[i].RgNo == rgno:
                
                
                return (i+1)
        
        
        return -1
         
    



if __name__ == "__main__":
    
    p = Parking()

    
    while True:

        input_str=input("\n$ ").split(" ") #Taking Input from User

        
        try:

            if input_str[0] == "create_parking_lot" and input_str[1].isnumeric():
                
                n=p.create_parking(int(input_str[1]))
                print(f"\n {n} Parking slots Created \n")
            
        
            elif input_str[0] == "park" and len(input_str) == 3:

                p.park_car(input_str[1],input_str[2])
        
            
            elif input_str[0] == "Exit":
            
                raise Exception
            
        
            elif input_str[0] == "status":

                p.display()

        
            elif input_str[0] == "leave" and input_str[1].isnumeric():

                p.free_slot(int(input_str[1]))
            
        
            elif input_str[0] == "registration_numbers_for_cars_with_colour" :
                
                p.display_rgno_by_color(input_str[1])
            
        
            
            elif input_str[0] == "slot_numbers_for_cars_with_colour":
                
                var=p.display_slotno_by_color(input_str[1])

                if len(var) == 0:

                    print("Not Found")

                else:

                    for i in range(len(var)):

                        print(var[i],end=",")
                    
            
        
            elif input_str[0] == "slot_number_for_registration_number":

                var=p.display_slotno_by_regno(input_str[1])

                if var == -1 :
                    
                    print("Not Found")
                
                else:

                    print(var)



            else:
                print("Enter correct Command")
            
   
        except:
              
            if input_str[0]=="Exit":    #If user press Exit command to terminate
            
                 sys.exit() 
            
            if p.n == 0:           #If user try to park car before creating Slots

                print("First You Need To Create Parking Slots")
                
            
            print("Exception ariesd")
            
            sys.exit()
    
    
    


   