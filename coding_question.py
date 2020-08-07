# """Question: 4"""
# A python program to create user-defined exception
# class MyError is derived from super class Exception


class MyError(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
        # __str__ is to print() the value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(3 * 2)
# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occured: ', error.value)

"""Question: 12"""
# Python code to remove duplicate elements


class RemoveDuplicate:
    def __init__(self, duplicate):
        self.final_list = []
        self.data = duplicate

    def remove(self):
        for num in self.data:
            if num not in self.final_list:
                self.final_list.append(num)
        return self.final_list


duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
r_list = RemoveDuplicate(duplicate)
print(r_list.remove())

"""Question: 11"""
# Nan means “Not a number”,
# this is because while your are getting input from user it would be string and
# you have to convert it into integer
