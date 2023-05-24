import os
import sys
import json
import signal
import keyboard
import AppOpener as ao
import customtkinter as ctk
from infi.systray import SysTrayIcon

with open('shortcut.json', 'r') as file:
    data = json.load(file)


def edit_json():
    command = "notepad.exe shortcut.json"
    os.system(command)


def reboot():
    os.execl(sys.executable, sys.executable, *sys.argv)

# customtkinter init


def gui(syst):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("KeebShot")

    frame_1 = ctk.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    label_1 = ctk.CTkLabel(master=frame_1, text="Add Shortcuts",
                           font=ctk.CTkFont(size=15, weight="bold"))
    label_1.pack(pady=10, padx=10)

    frame_2 = ctk.CTkFrame(master=frame_1)
    frame_2.pack(pady=10, padx=10, fill="both")

    # label_2 = ctk.CTkLabel(
    #     master=frame_2, text=json.dumps(data, indent=4))
    # label_2.pack(pady=10, padx=10)

    text_1 = ctk.CTkTextbox(master=frame_2, width=300, height=200)
    text_1.pack(pady=10, padx=10)
    text_1.insert("0.0", text=json.dumps(data, indent=4))
    text_1.configure(state=ctk.DISABLED)

    label_3 = ctk.CTkLabel(master=frame_1, text="Edit Json", font=ctk.CTkFont(
        size=15, weight="bold"), anchor="w")
    label_3.pack(pady=10, padx=10)

    button_1 = ctk.CTkButton(
        master=frame_1, text="Edit JSON", command=edit_json)
    button_1.pack(pady=10, padx=10)

    button_1 = ctk.CTkButton(
        master=frame_1, text="Restart App", command=reboot)
    button_1.pack(pady=10, padx=10)

    app.mainloop()


# Keeb shortcut
def key_press(short):
    # print("callback =>", short)
    ao.open(f"{short['name']}", match_closest=True)


def on_key_press(event):
    # print("Event => ", type(event))

    for shortcut in data:
        if keyboard.is_pressed(shortcut['key']):
            # print("key => ", shortcut)
            key_press(shortcut)


keyboard.on_press(on_key_press)

# kill the program


def kill(syst):
    os.kill(os.getpid(), signal.SIGILL)


# System Tray icon
menu_op = (("Settings", None, gui),)
syst = SysTrayIcon("icon.ico", "KeebShot", menu_op, on_quit=kill)
syst.start()
if os.name == 'nt':  # For Windows
    os.system('taskkill /IM cmd.exe /F')
# waiting for the keypress
keyboard.wait()
