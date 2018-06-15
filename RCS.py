#!/usr/bin/env python3

# RCS - Raspberry Control Script
# @Author Lorenzo Casini aka CaSo

import io
import os
import time

#This fucntion check te disk usage on a RPiself.
def check_disk():
    clear_terminal()
    os.system("df -h")
    time.sleep(5)

#This function create a gratefully exit when user press Ctrl + C.
def exit_gracefully():
    clear_terminal()
    print("Exiting...")
    time.sleep(2)

#This function update the RPi Firmware
def update_firmware():
    clear_terminal()
    print("Initializing the firmware update process...")
    time.sleep(2)
    os.system("sudo rpi-update")
    time.sleep(5)
    clear_terminal()
    print("If you update your RPi firmware , please reboot the system !!!")
    time.sleep(5)

#This function update the RPi OS & SW
def update_pi():
    clear_terminal()
    print("Initializing the OS & SW  update process...\n")
    time.sleep(2)
    os.system("sudo apt-get update && sudo apt-get upgrade")
    time.sleep(5)

#This function check the current cpu temperature.
def check_cpu_temp():
    clear_terminal()
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=","CPU Temp: "))

#This function clear the terminal
def clear_terminal():
    os.system("clear")

#This function print the menu.
def print_menu():
    clear_terminal()
    print(30 * "-", "RCS - MENU", 30 * "-")
    print("\t0) Exit")
    print("\t1) Update Raspberry Firmware")
    print("\t2) Update Raspberry OS & SW")
    print("\t3) Check Temperature")
    print("\t4) Check Disk Usage")
    print(30 * "-","Version 1.0",29 * "-")

#Check the user input and call the correct function
def main():

    while True:

        print_menu()

        while True:
            try:
                user_input = int(input("Enter your choice [0-3]: "))
                break
            except ValueError:
                print_menu()

        if user_input == 0: #Exit from the script
            exit()

        elif user_input == 1: #Update raspberry firmware
            update_firmware()

        elif user_input == 2: #Update raspberry OS & SW
            update_pi()

        elif user_input == 3: #Check raspberry temperature
            print(check_cpu_temp())
            time.sleep(3)

        elif user_input == 4:
            check_disk()

        else: #Default case if some scientist insert invalid input
            input("Wrong options selection. Press any key to try again...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        exit_gracefully()
