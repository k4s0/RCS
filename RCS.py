# RCS (Raspberry_Control_Script)
# @Author Lorenzo Casini 
from gpiozero import CPUTemperature
import os
import time

#This method check the current cpu temperature.
def check_cpu_temperature():
    cpu_temp = CPUTemperature
    return cpu_temp.teperature
#This method clear the terminal
def clear_terminal():
    os.system("clear")

#This method print the menu.
def print_menu():
    print("Menu")
    print("\t0) Exit")
    print("\t1) Update Raspberry Firmware")
    print("\t2) Update Raspberry OS & SW")
    print("\t3) Check Temperature")
    user_input=int(input("Choose one option->"))
    return user_input

#Init the main menu.
clear_terminal()
user_input = print_menu()

#Check user input and call the correct function.
if user_input == 0: #Exit from the script
    print("Exiting the script...")
    time.sleep(2)
    clear_terminal()
    exit()

elif user_input == 1: #Update raspberry firmware
    print("User Choose ->1")

elif user_input == 2: #Update raspberry OS & SW
    print("User Choose ->2")

elif user_input == 3:
    check_cpu_temperature()
    
else: #Default case if some scientist insert invalid input
    print("Invalid Input, please enter a valid option.")
    time.sleep(2)
    clear_terminal()
    print_menu()
