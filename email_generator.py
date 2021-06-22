try:
    # system imports
    import sys
    import time
    import random

    # 3rd party imports
    import pyautogui
    import crayons
    import names

except ModuleNotFoundError as e:
    print(e)
    print("Failed to import 1 or more modules.")
    sys.exit()


def launch():
    print(crayons.green("Launching Chrome..."))
    pyautogui.hotkey("win", "r")
    time.sleep(.1)
    pyautogui.typewrite("chrome")
    time.sleep(.1)
    pyautogui.press("enter")
    print(crayons.green("Chrome is now open and running."))


def yandex():
    time.sleep(3)
    print(crayons.green("Opening Yandex"))
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(
        "https://passport.yandex.com/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_com&retpath=https%3A%2F%2Fmail.yandex.com%2F&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1")
    pyautogui.press("enter")
    print(crayons.green("Finding the form..."))


def generate(opt, _len):
    if _len > 0:
        if opt == "-u":
            letterMap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif opt == "-p":
            letterMap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
        info = ""
        for _ in range(15):
            info = info + random.choice(letterMap)
        return info


def fill_out():
    time.sleep(3)
    print(crayons.green("Generating info..."))

    # name
    fname = names.get_first_name()
    lname = names.get_last_name()
    pyautogui.typewrite(fname)
    pyautogui.press("tab")
    pyautogui.typewrite(lname)
    pyautogui.press("tab")
    print(crayons.blue(f"Name: {fname} {lname}"))

    # username
    uname = generate("-u", 15)
    pyautogui.typewrite(uname)
    pyautogui.press("tab")
    print(crayons.blue(f"Email: {uname}@yandex.com"))

    # password
    pword = generate("-p", 16)
    pyautogui.typewrite(pword + "\t" + pword + "\t" + "\t")
    print(crayons.blue(f"Password: {pword}"))

    # find security button
    answer = generate("-u", 7)
    pyautogui.hotkey("ctrl", "f")
    pyautogui.typewrite("I don")
    pyautogui.hotkey("ctrl", "return")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.typewrite(answer)
    print(crayons.blue(f"Security answer: {answer}"))

    print(crayons.yellow("Human verification required."))
    print(crayons.yellow("Enter the characters in the box showed on screen."))


if __name__ == "__main__":
    launch()
    yandex()
    fill_out()
