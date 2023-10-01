# import sys, os
# from datetime import datetime
# def    greet_user(name):
#     print("Hello, " + name + "!")
# greet_user("Tanmoy")
# current_time=datetime.now()
# print("Current time is " + str(current_time))


"""
Sample code to test pylint

"""
from datetime import datetime
def greet_user(name):
    """
        Greets an user
    """
    return ("Hello, " + name + "!")
greet_user("Tanmoy")
current_time=datetime.now()
print("Current time is " + str(current_time))
