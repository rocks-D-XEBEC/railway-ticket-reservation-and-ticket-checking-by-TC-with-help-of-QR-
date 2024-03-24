# -*- coding: utf-8 -*-
import pickle
import qrcode
from random import randint
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

class User:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

class TICKET_BOOK:
    def __init__(self, Class, boarding_point, quota):
        self.Class = Class
        self.boarding_point = boarding_point
        self.quota = quota
    
    def __str__(self):
        return f"Class: {self.Class}, Boarding Point: {self.boarding_point}, Quota: {self.quota}"

class Train_Ticket:
    Admin_list = []
    Cust_list = []
    Tc_list = []
    ticket_list = []
    loc_list = []
    pnr = []
    train = {}

    @classmethod
    def initialize(cls):
        cls.Admin_list = []
        cls.Cust_list = []
        cls.Tc_list = []
        cls.ticket_list = []
        cls.loc_list = []
        cls.pnr = []
        cls.train = {}

    def __init__(self, user=None, tkt_bk=None):
        if isinstance(user, User) and isinstance(tkt_bk, TICKET_BOOK):
            Train_Ticket.Admin_list.append(user)
            Train_Ticket.ticket_list.append(tkt_bk)

    def Admin_SignUp(self):
        print('+-----------------------+')
        print('   ENTER USER DETAILS    ')
        print('+-----------------------+')

        name = input("Enter your Name      : ")
        mo_no = input("Enter your Phone no. : ")
        add = input("Enter your Address   : ")
        email = input("Enter your Email     : ")
        print('')
        newkey = input('Enter Username       : ')
        newvalue = input('Enter Password       : ')
        Train_Ticket.Admin_list.append(User(name, add, mo_no, email))

        admin = {newkey: newvalue}
        with open("AdminInfoList.pickle", "wb") as pickle_out:
            pickle.dump(Train_Ticket.Admin_list, pickle_out)

        with open("Admindict.pickle", "wb") as pickle_out:
            pickle.dump(admin, pickle_out)

    def Cust_SignUp(self):
        print('+-----------------------+')
        print('   ENTER USER DETAILS    ')
        print('+-----------------------+')

        name = input("Enter your Name      : ")
        mo_no = input("Enter your Phone no. : ")
        add = input("Enter your Address   : ")
        email = input("Enter your Email     : ")
        print('')
        newkey = input('Enter Username       : ')
        newvalue = input('Enter Password       : ')
        Train_Ticket.Cust_list.append(User(name, add, mo_no, email))

        cust = {newkey: newvalue}
        with open("CustInfoList.pickle", "wb") as pickle_out:
            pickle.dump(Train_Ticket.Cust_list, pickle_out)

        with open("custdict.pickle", "wb") as pickle_out:
            pickle.dump(cust, pickle_out)

    def Tc_SignUp(self):
        print('+-----------------------+')
        print('   ENTER USER DETAILS    ')
        print('+-----------------------+')
        name = input("Enter your Name      : ")
        mo_no = input("Enter your Phone no. : ")
        add = input("Enter your Address   : ")
        email = input("Enter your Email     : ")
        print('')
        newkey = input('Enter Username       : ')
        newvalue = input('Enter Password       : ')
        Train_Ticket.Tc_list.append(User(name, add, mo_no, email))

        tc = {newkey: newvalue}
        with open("TcInfoList.pickle", "wb") as pickle_out:
            pickle.dump(Train_Ticket.Tc_list, pickle_out)

        with open("tcdict.pickle", "wb") as pickle_out:
            pickle.dump(tc, pickle_out)

    def ADlogin(self):
        my_file = Path("admindict.pickle")
        if my_file.exists():
            with open("admindict.pickle", "rb") as pickle_in:
                admin = pickle.load(pickle_in)
                login_username = input('Enter Username       : ')
                login_password = input('Enter Password       : ')

                if login_username in admin and admin[login_username] == login_password:
                    while True:
                        print('╔═[ADMIN]══════════════╗')
                        print(" 1.Add new Location.")
                        print(" 2.Add new Route.")
                        print(" 3.Manage Route.")
                        print(" 0.Back.")
                        print('╚══════════════════════╝')

                        choice = input('Enter Your Choice    : ')

                        if choice == '1':
                            print('+-----------------------+')
                            print("  CREATE NEW LOCATION    ")
                            print('+-----------------------+')
                            loc = input('Enter Your Choice    : ')
                            Train_Ticket.loc_list.append(loc)

                            with open("loc_list.pickle", "wb") as pickle_out:
                                pickle.dump(Train_Ticket.loc_list, pickle_out)

                        elif choice == '2':
                            From = input("Enter Source         : ")
                            to = input("Enter Destination    : ")
                            if From in Train_Ticket.loc_list:
                                if to in Train_Ticket.loc_list:
                                    Train_Ticket.train[From] = to
                                    with open("Route.pickle", "wb") as pickle_out:
                                        pickle.dump(Train_Ticket.train, pickle_out)
                                    print("Route is added!!!")
                                else:
                                    print('Invalid Destination!!!')
                            else:
                                print('Invalid Source!!!')

                        elif choice == '3':
                            print("Manage Route")
                            while True:
                                print('╔═[ADMIN]══════════════╗')
                                print(" 1.Delete Route.")
                                print(" 2.Change Route.")
                                print(" 0.Back.")
                                print('╚══════════════════════╝')
                                sub_choice = input('Enter Your Choice    : ')

                                if sub_choice == '1':
                                    From = input("Enter Source         : ")
                                    to = input("Enter Destination    : ")
                                    if From in Train_Ticket.train:
                                        if Train_Ticket.train[From] == to:
                                            del Train_Ticket.train[From]
                                            print("Successfully Removed!!!!")
                                        else:
                                            print("Invalid Destination!!!")
                                    else:
                                        print("Invalid Source!!!")

                                elif sub_choice == '2':
                                    From = input("Enter Source         : ")
                                    to = input("Enter Destination    : ")
                                    if len(From) > 5:
                                        if From in Train_Ticket.train:
                                            if Train_Ticket.train[From] == to:
                                                new_key = input('Enter New Source :')
                                                Train_Ticket.train[new_key] = Train_Ticket.train.pop(From)
                                                print("Successfully Update!!!!")
                                            else:
                                                print("Invalid Destination!!!")
                                        else:
                                            print("Invalid Source!!!")

                                    elif choice == '2':
                                        From = input("Enter Source         : ")
                                        to = input("Enter Destination    : ")

                                    if From in Train_Ticket.train:
                                        if Train_Ticket.train[From] == to:
                                            new_value = input('Enter New Destination :')
                                            Train_Ticket.train[From] = new_value
                                            print("Successfully Update!!!!")
                                        else:
                                            print("Invalid Destination!!!")
                                    else:


                                        print("Invalid Source!!!")

                                elif sub_choice == '0':
                                    exit_program()
                                    break
                                else:
                                    print('Invalid username or password')
                            else:
                                print("Signup first!!!")
                                
                        elif choice == '0':
                            exit_program()
                            break

    def CUSlogin(self):
        my_file = Path("custdict.pickle")
        if my_file.exists():
            with open("custdict.pickle", "rb") as pickle_in:
                cust = pickle.load(pickle_in)
                login_username = input('Enter Username: ')
                login_password = input('Enter Password: ')

                if login_username in cust and cust[login_username] == login_password:
                    while True:
                        print('╔═[CUSTOMER]═══════════╗')
                        print(' 1.Book Ticket.')
                        print(' 2.View History.')
                        print(' 0.Back.')
                        print('╚══════════════════════╝')

                        choice = input('Enter Your Choice: ')
                        print('')

                        if choice == '1':
                            with open("Route.pickle", "rb") as pickle_in:
                                train = pickle.load(pickle_in)
                            From = input("Enter Source: ")
                            to = input("Enter Destination: ")
                            if train.get(From) == to:
                                print('Train is available for the given route')
                                self.ticket_book()
                            else:
                                print('Train is not available for the given route')
                        elif choice == '2':
                            print('+-----------------------+')
                            print("     RECENT HISTORY     ")
                            print('+-----------------------+')
                            for ticket in Train_Ticket.ticket_list:
                                print("Class: ", ticket.Class)
                                print("Boarding Point: ", ticket.boarding_point)
                                print("Quota: ", ticket.quota)
                                print("-------------------------")

                        elif choice == '0':
                            break

                        else:
                            print('Invalid choice. Please try again.')

                else:
                    print('Invalid username or password')

        else:
            print("Signup first!!!")

    def TClogin(self):
        my_file = Path("tcdict.pickle")
        if my_file.exists():
            with open("tcdict.pickle", "rb") as pickle_in:
                tc = pickle.load(pickle_in)
                login_username = input('Enter Username       : ')
                login_password = input('Enter Password       : ')
                if login_username in tc:
                    if tc[login_username] == login_password:
                        while True:
                            print('╔═[TC]═════════════════╗')
                            print(' 1.Check In Database.')
                            print(' 0.Back.')
                            print('╚══════════════════════╝')

                            print('')
                            choice = input('Enter Your Choice    : ')
                            print('')
                            if choice == '1':
                                print('+-----------------------+')
                                print('   CHECK IN DATABASE     ')
                                print('+-----------------------+')
                                print('')
                                with open("pnr.pickle", "rb") as pickle_in:
                                    Train_Ticket.pnr = pickle.load(pickle_in)
                                a = int(input('Enter PNR NO.        : '))
                                if a in Train_Ticket.pnr:
                                    print('+-----------------------+')
                                    print("      TICKET DETAILS     ")
                                    print('+-----------------------+')
                                    with open("ticket_list.pickle", "rb") as pickle_in:
                                        Train_Ticket.ticket_list = pickle.load(pickle_in)
                                    print(Train_Ticket.ticket_list[0])
                                else:
                                    print("Invalid PNR!!!")
                            elif choice == '0':
                                break
                    else:
                        print('Invalid username or password')
                else:
                    print('Invalid username or password')

        else:
            print("Signup first!!!")

    def ticket_book(self):
        print('+-----------------------+')
        print('   RESERVATION FORM      ')
        print('+-----------------------+')
        Class = input('Enter Class          : ')
        bdg_pt = input('Enter Boarding point  : ')
        quota = input('Enter Quota          : ')

        new_ticket = TICKET_BOOK(Class, bdg_pt, quota)
        Train_Ticket.ticket_list.append(new_ticket)
        with open("ticket_list.pickle", "wb") as pickle_out:
            pickle.dump(Train_Ticket.ticket_list, pickle_out)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,  # Adjust the box size as needed
            border=4,
        )
        x = randint(1000000000, 10000000000)  # random number
        Train_Ticket.pnr.append(x)
        with open("pnr.pickle", "wb") as pickle_out:
            pickle.dump(Train_Ticket.pnr, pickle_out)

        data = ("PNR NO             :: " + str(x) + "\t\n" + "CLASS               :: " + Class + "\t\n" +
                "BOARDING PT :: " + bdg_pt + "\t\n" + "QUOTA              :: " + quota)
        qr.add_data(data)
        qr.make(fit=True)

        # Generate QR code image
        qr_img = qr.make_image()

        # Create an image with details
        img = Image.new('RGB', (300, 400), color='white')
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()

        details_text = f"PNR NO             :: {x}\nCLASS               :: {Class}\nBOARDING PT :: {bdg_pt}\nQUOTA              :: {quota}"
        draw.text((10, 10), details_text, font=font, fill='black')

        # Resize QR code image to match the height of the details image
        qr_img = qr_img.resize((img.height, img.height))

        # Combine the details image and QR code image side by side
        combined_img = Image.new('RGB', (img.width + qr_img.width, img.height))
        combined_img.paste(img, (0, 0))
        combined_img.paste(qr_img, (img.width, 0))

        # Save the combined image
        name_img = input("Name the file (include .jpg extension): ")  # e.g. file.jpg
        combined_img.save(name_img)


def load_data():
    try:
        with open("AdminInfoList.pickle", "rb") as pickle_in:
            Train_Ticket.Admin_list = pickle.load(pickle_in)
        with open("CustInfoList.pickle", "rb") as pickle_in:
            Train_Ticket.Cust_list = pickle.load(pickle_in)
        with open("TcInfoList.pickle", "rb") as pickle_in:
            Train_Ticket.Tc_list = pickle.load(pickle_in)
        with open("Route.pickle", "rb") as pickle_in:
            Train_Ticket.train = pickle.load(pickle_in)
        with open("pnr.pickle", "rb") as pickle_in:
            Train_Ticket.pnr = pickle.load(pickle_in)
        with open("ticket_list.pickle", "rb") as pickle_in:
            Train_Ticket.ticket_list = pickle.load(pickle_in)
        with open("loc_list.pickle", "rb") as pickle_in:
            Train_Ticket.loc_list = pickle.load(pickle_in)
    except FileNotFoundError:
        # Files don't exist, initialize with empty lists/dicts
        Train_Ticket.Admin_list = []
        Train_Ticket.Cust_list = []
        Train_Ticket.Tc_list = []
        Train_Ticket.train = {}
        Train_Ticket.pnr = []
        Train_Ticket.ticket_list = []
        Train_Ticket.loc_list = []

def save_data():
    with open("AdminInfoList.pickle", "wb") as pickle_out:
        pickle.dump(Train_Ticket.Admin_list, pickle_out)
    with open("CustInfoList.pickle", "wb") as pickle_out:
        pickle.dump(Train_Ticket.Cust_list, pickle_out)
    with open("TcInfoList.pickle", "wb") as pickle_out:
        pickle.dump(Train_Ticket.Tc_list, pickle_out)
    with open("Route.pickle", "wb") as pickle_out:
        pickle.dump(Train_Ticket.train, pickle_out)
    with open("pnr.pickle", "wb") as pickle_out:
        pickle.dump(Train_Ticket.pnr, pickle_out)
    with open("ticket_list.pickle", "wb") as pickle_out:
        pickle.dump(Train_Ticket.ticket_list, pickle_out)
    with open("loc_list.pickle", "wb") as pickle_out:
        pickle.dump(Train_Ticket.loc_list, pickle_out)

def exit_program():
    save_data()
    print("Data saved. Exiting program.")
    exit()
def view_pickle_data(filename):
    try:
        with open(filename, 'rb') as pickle_file:
            data = pickle.load(pickle_file)
            print(f"\nContents of {filename}:")
            print(data)
            print()
            if filename == "ticket_list.pickle":
                for ticket in data:
                    print(ticket)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main part of the code
Train_Ticket.initialize()
t = Train_Ticket()

while True:
    load_data()
    print('╔═[Main Menu]══════════╗')
    print(' 1.Admin Account.')
    print(' 2.Customer Account.')
    print(' 3.Ticket Checker.')
    print(' 4.View File Contents.')
    print(' 0.Exit.')
    print('╚══════════════════════╝')

    main_choice = input('Enter Your Choice: ')
    print('')

    if main_choice == '1':
        while True:
            print('╔═[ADMIN]══════════════╗')
            print(' 1.Log In.')
            print(' 2.Sign up.')
            print(' 0.Back.')
            print('╚══════════════════════╝')

            sub_choice_admin = input('Enter Your Choice: ')
            print('')

            if sub_choice_admin == '1':
                t.ADlogin()
            elif sub_choice_admin == '2':
                t.Admin_SignUp()
            elif sub_choice_admin == '0':
                exit_program()
                break

    elif main_choice == '2':
        while True:
            print('╔═[CUSTOMER]═══════════╗')
            print(' 1.Log In.')
            print(' 2.Sign up.')
            print(' 0.Back.')
            print('╚══════════════════════╝')

            sub_choice_cust = input('Enter Your Choice: ')
            print('')

            if sub_choice_cust == '1':
                t.CUSlogin()
            elif sub_choice_cust == '2':
                t.Cust_SignUp()
            elif sub_choice_cust == '0':
                break

    elif main_choice == '3':
        while True:
            print('╔═[TC]═════════════════╗')
            print(' 1.Log In.')
            print(' 2.Sign up.')
            print(' 0.Back.')
            print('╚══════════════════════╝')

            sub_choice_tc = input('Enter Your Choice: ')
            print('')

            if sub_choice_tc == '1':
                t.TClogin()
            elif sub_choice_tc == '2':
                t.Tc_SignUp()
            elif sub_choice_tc == '0':
                break

    elif main_choice == '4':
        print("Select a file to view:")
        print("1. AdminInfoList.pickle")
        print("2. Admindict.pickle")
        print("3. CustInfoList.pickle")
        print("4. custdict.pickle")
        print("5. TcInfoList.pickle")
        print("6. tcdict.pickle")
        print("7. Route.pickle")
        print("8. ticket_list.pickle")
        print("9. pnr.pickle")
        print("0. Back")
        file_choice = input("Enter your choice: ")

        if file_choice == '0':
            continue

        try:
            index = int(file_choice)
            if 1 <= index <= 9:  # Update the range based on the number of files
                selected_filenames = [
                    "AdminInfoList.pickle",
                    "Admindict.pickle",
                    "CustInfoList.pickle",
                    "custdict.pickle",
                    "TcInfoList.pickle",
                    "tcdict.pickle",
                    "Route.pickle",
                    "ticket_list.pickle",
                    "pnr.pickle",
                ]
                selected_filename = selected_filenames[index - 1]
                view_pickle_data(selected_filename)
            else:
                print("Invalid choice. Please enter a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    elif main_choice == '0':
        exit_program()
        break

    else:
        print('Invalid choice. Please try again.')
