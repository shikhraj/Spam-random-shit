import pyautogui, time, string, random

time.sleep(3)
while True:
    letters = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)



    number = str(random.randint(1001,9999))
    

    pyautogui.typewrite("https://prnt.sc/" + letters + number)
    pyautogui.press("enter")
    time.sleep(2)
