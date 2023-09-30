import sys, os
from datetime import datetime
def    greet_user(name):
    print("Hello, " + name + "!")
greet_user("Alice")
current_time=datetime.now()
print("Current time is " + str(current_time))