import time
import notify2
import win10toast
import os
import sys

def linux():
    notify2.init("Reminder")
    notice = notify2.Notification('Drink water', "It's been 2 hrs since you last drank water!")
    while True:
      notice.show()
      time.sleep(7200)

def windows():
  toast = win10toast.ToastNotifier()
  toast.show_toast("Reminder", "It's been 2 hrs since you last drank water!", duration=7200)

def mac():
  while True:
    command = "osascript -e \'display alert \"Its been 2 hrs, Drink water\"\'"
    os.system(command)
    time.sleep(7200)

if __name__ == "__main__":
    if sys.platform == "linux":
        linux()
    elif sys.platform == "win32":
        windows()
    elif sys.platform == "darwin":
        mac()