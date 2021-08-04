import sys
import argparse
from parking import Parking


if __name__ == '__main__':
    p = Parking()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='src_file')
    args = parser.parse_args()
    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                p.file_input(line)
    else:
        while True:
            inp = input("\n$ ").split(" ")
            try:
                if(inp[0] == 'create_parking_lot' and len(inp) == 1):
                    n = p.create_parking(100)
                    print(f"\n {n} Parking slots Created \n")
                elif(inp[0] == 'create_parking_lot' and inp[1].isdigit()):
                    n = p.create_parking(int(inp[1]))
                    print(f"\n {n} Parking slots Created \n")
                elif inp[0] == "park" and len(inp) == 3:
                    p.park_car(inp[1], inp[2])
                elif inp[0] == "Exit":
                    raise Exception
                elif inp[0] == "status":
                    p.display()
                elif inp[0] == "leave" and inp[1].isnumeric():
                    p.free_slot(int(inp[1]))
                elif(inp[0] == "registration_numbers_for_cars_with_colour"):
                    regs = p.display_rgno_by_color(inp[1])
                    if len(regs) != 0:
                        print(', '.join(regs))
                    else:
                        print("Not found")
                elif inp[0] == "slot_numbers_for_cars_with_colour":
                    var = p.display_slotno_by_color(inp[1])
                    if len(var) == 0:
                        print("Not Found")
                    else:
                        print(str(var)[1:-1])
                elif inp[0] == "slot_number_for_registration_number":
                    var = p.display_slotno_by_regno(inp[1])
                    if var == -1:
                        print("Not Found")
                    else:
                        print(var)
                else:
                    print("Enter correct Command")
            except Exception:
                if inp[0] == "Exit":
                    sys.exit()
                if p.n == 0:
                    print("First You Need To Create Parking Slots")
                print("Exception ariesd")
                sys.exit()
