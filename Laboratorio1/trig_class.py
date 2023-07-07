"""
06/07/23
J.E.V.A.
Trig calss
version: 1.1.2
"""
# import needed libraries
import math
import datetime

# we asign important variables
pi = math.pi
current_time = datetime.datetime.now()


class trig():
    def __init__(self) -> None:
        pass

    def cos_pi(self):  # we make a cos method
        return math.cos(pi)

    def sin_pi(self):  # we make a sin method
        return math.sin(pi)

    def tan_pi(self):  # we make a tan method
        return math.tan(pi)


class logs():
    def __init__(self, file):
        self.file = file

    def add_log(self, string):  # we add a string to the file
        with open(self.file, "a") as log_file:
            log_file.write(str(current_time))
            log_file.write('\n')
            log_file.write(str(string))
            log_file.write('\n')
