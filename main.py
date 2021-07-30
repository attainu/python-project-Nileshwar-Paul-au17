import sys
import argparse
from parking import Parking


if __name__ == '__main__':
    p = Parking()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
    args = parser.parse_args()
    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip('\n')
                p.show(line)
    else:
        while True:
            input_str = input("\n$ ").split(" ")
            try:
                if input_str[0] == 'create_parking_lot' and input_str[1].isnumeric():
                    n = p.create_parking(int(input_str[1]))
                    print(f"\n {n} Parking slots Created \n")
                elif input_str[0] == "park" and len(input_str) == 3:
                    p.park_car(input_str[1], input_str[2])
                elif input_str[0] == "Exit":
                    raise Exception
                elif input_str[0] == "status":
                    p.display()
                elif input_str[0] == "leave" and input_str[1].isnumeric():
                    p.free_slot(int(input_str[1]))
                elif input_str[0] == "registration_numbers_for_cars_with_colour":
                    regs = p.display_rgno_by_color(input_str[1])
                    if len(regs) != 0:
                        print(', '.join(regs))
                    else:
                        print("Not found")
                elif input_str[0] == "slot_numbers_for_cars_with_colour":
                    var = p.display_slotno_by_color(input_str[1])
                    if len(var) == 0:
                        print("Not Found")
                    else:
                        print(str(var)[1:-1])
                elif input_str[0] == "slot_number_for_registration_number":
                    var = p.display_slotno_by_regno(input_str[1])
                    if var == -1:
                        print("Not Found")
                    else:
                        print(var)
                else:
                    print("Enter correct Command")
            except Exception:
                if input_str[0] == "Exit":
                    sys.exit()
                if p.n == 0:
                    print("First You Need To Create Parking Slots")
                print("Exception ariesd")
                sys.exit()
