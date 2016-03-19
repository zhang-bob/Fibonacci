__author__ = 'zhangb3'
from multiprocessing.sharedctypes import Array, Value

class FibonacciArray:
    def __init__(self):
        # restrict maximum number for this web service to avoid overload
        self.MAXIMUM = 5000

        # index of valid number in shared array
        self.current_index = Value('i', 0)

        #Share array to optimize performance if there are too many requests come in
        self.share_array = Array('i',self.MAXIMUM)

    def generate_fibonacci_string(self, number):
        message = ""
        status = 0

        (number, status, message) = self.__check_integer(number)
        if status != 0:
           return (status, message)

        (status, message) = self.__check_negative_integer(number)
        if status != 0:
            return (status, message)

        (status, message) = self.__check_maximum(number)
        if status != 0:
            return (status, message)

        # if the request string has been reserved in shared memory, return directly
        if self.current_index.value >= number:
            return self.share_array[number-1]

        fobinacci_string = self.__get_fibonacci_string(number)
        return (status, fobinacci_string)

    def __get_fibonacci_string(self, number):
        status =0
        first_number = 0
        second_number = 1
        fobinacci_string = str(first_number) + " " + str(second_number)

        if number == 1:
            self.current_index.value = 1
            return (status, first_number)
        if number == 2:
            self.current_index.value = 2
            return (status, str(first_number) + " " + str(second_number))

        index = 2
        while index < number:
            new_number = first_number + second_number
            first_number = second_number
            second_number = new_number

            fobinacci_string = str(fobinacci_string) + " " + str(new_number)
            index += 1

            #Add the value into share Array
            self.share_array = fobinacci_string.split()
        self.current_index.value = number
        return fobinacci_string

    def __check_maximum(self, number):
        # return error if the request number is bigger than MAXIMUM setting
        status = 0
        message = ""
        if number > self.MAXIMUM:
            status = 1
            message = "The number is bigger than maximum limitation %s" % self.MAXIMUM
        return (status, message)

    def __check_integer(self, number):
        # Check whether the parameter can convert to integer
        try:
            status = 0
            message = ""
            number = int(number)
        except:
            status=1
            message = "The number you input is not right, an integer is expected"
        return (number, status, message)

    def __check_negative_integer(self, number):
        # negative integer is not allowed
        status = 0
        message = ""
        if number <= 0 :
            status = 1
            message = "zero and negative integer is not allowed to generate fibonacci string"
        return (status, message)