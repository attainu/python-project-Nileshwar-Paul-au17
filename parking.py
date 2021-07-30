from file_car import Car


class Parking:
    def __init__(self):
        self.slots = 0
        self.slotNo = 0
        self.used_slots = 0
        self.n = 0

    def create_parking(self, n):
        self.n = n
        self.slots = [0] * n
        self.total_slots = n
        return self.total_slots

    def empty_slots(self):
        for idx in range(len(self.slots)):
            if self.slots[idx] == 0:
                return idx
        return -1

    def uniq_rgno(self, rgno):
        for i in range(len(self.slots)):
            if self.slots[i] == 0:
                continue
            elif self.slots[i].RgNo == rgno:
                return False
        return True

    def park_car(self, rgno, color):
        check_rgno = True
        check_rgno = self.uniq_rgno(rgno)
        if check_rgno is False:
            print("This RgNo.car is already in Parking")
            print("Two RgNo. can not be same")
            return -1
        elif check_rgno == 1 and self.used_slots < self.total_slots:
            self.slotno = self.empty_slots()
            self.slots[self.slotno] = Car(rgno, color)
            self.used_slots += 1
            self.slotno += 1
            print(f"Slot Number  {self.slotno} Alloted")
            return
        else:
            print("ParkingSlot Not  Available")
            return

    def free_slot(self, slotno):
        if self.used_slots > 0 and self.slots[slotno-1] != 0:
            self.slots[slotno-1] = 0
            self.used_slots -= 1
            print(f"Slot Number {slotno} is Free")
            return 
        else:
            print("Enter wrong slot number")
            return

    def display(self):
        print("SlotNo.\t\tRgNo.\t\t\t\t\tColour")
        for i in range(len(self.slots)):
            if self.slots[i] != 0:
                print(f"{i+1} \t\t{self.slots[i].RgNo} \
                \t\t {self.slots[i].Color}")
            else:
                continue

    def display_slotno_by_color(self, color):
        slotno = []
        for i in range(len(self.slots)):
            if self.slots[i] == 0:
                continue
            if self.slots[i].Color == color:
                slotno.append(i+1)
        return slotno

    def display_rgno_by_color(self, color):
        regs = []
        for i in self.slots:
            if i == 0:
                continue
            if i.Color == color:
                regs.append(i.RgNo)
        return regs

    def display_slotno_by_regno(self, rgno):
        for i in range(len(self.slots)):
            if self.slots[i] == 0:
                continue
            elif self.slots[i].RgNo == rgno:
                return (i+1)
        return -1

    def show(self, line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.create_parking(n)
            print('Created a parking lot with '+str(res)+' slots')
        elif line.startswith('park'):
            regno = line.split(' ')[1]
            color = line.split(' ')[2]
            res = self.park_car(regno, color)
        elif line.startswith('leave'):
            leave_slotid = int(line.split(' ')[1])
            self.free_slot(leave_slotid)
        elif line.startswith('status'):
            self.display()
        elif line.startswith('registration_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            regnos = self.display_rgno_by_color(color)
            if len(regnos) != 0:
                print(', '.join(regnos))
            else:
                print("Not found")
        elif line.startswith('slot_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.display_slotno_by_color(color)
            print(*slotnos, sep=", ")
        elif line.startswith('slot_number_for_registration_number'):
            regno = line.split(' ')[1]
            slotno = self.display_slotno_by_regno(regno)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)
        elif line.startswith('exit'):
            exit(0)
