# ParkingLot
Design a parking lot using Python with Test driven approach.

## Dependencies

You just need Python. The code is compatible with Python2 as well as Python3. Visit the link https://www.python.org/downloads/ to install Python. 
It can be run in any operating system.

## Description

This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots. 

 main .py execute these following commands. all the commands are case sensitive
 
   
    Commands                    Discription

1. `create_parking_lot n ` - Given n number of slots, create a parking lot
 https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/create_parking_lot.png

2. `park car_regno car_color` - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Parking Slot Not available".
https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/park%20registration_number%20colour.png

3. `status` - Prints the slot number, registration number and color of the parked vehicles.
https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/status.png

4. `leave x` - Removes vehicle from slot number x
https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/leave.png

5.  `registration_numbers_for_cars_with_colour colour_name` - this command will give you a list of registration numbers of that particular colour given by you. this command is very helpful to find vehicals parked in your parking
https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/list%20rgno%20by%20colour.png

6. `slot_numbers_for_cars_with_colour colour_name` - this command give you the list of parking  slot number of cars of colour specified by you.
https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/list%20slot%20no%20by%20colour.png

7. `slot_number_for_registration_number registration number`- This command give you the parking slot number of a particular car whoes registration number given by you
https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/slot%20number%20by%20rgno.png

8. `Exit` - To close the programe you can type "Exit". 
https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/exit.png




## Python Library we are using in this :-

1. sys :- Discription inside the Doc folder of the repository

2. argparse :-Discription inside the Doc folder of the repository


## SET UP


1. Clone the repository

2. open shell in your system and set the path of this repository in your shell

3. Run `python main.py` to run without input test case file. This opens a shell where you can write your commands like -

4. First you need to create parking slots of your parking by entering command :-

        `create_parking_lot n `

n is the number of vehicles can be parked in your parking

5. To run with a Input file execute `python main.py -f Input_file_name.txt. 

for example a input test file (run_test.txt) is given in the repository
https://github.com/attainu/python-project-Nileshwar-Paul-au17/blob/dev/Pic/output_of%20input_text_file.png