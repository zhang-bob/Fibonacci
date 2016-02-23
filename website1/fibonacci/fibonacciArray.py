__author__ = 'zhangb3'
class FibonacciArray:
    def __init__(self):
        self.MAXIMUM = 5000

    def generate_fibonacci_string(self, number):
        fobinacci_string = ""
        message = ""
        status = 0
        first_number = 1
        second_number = 1
        new_number = 0

        # Check whether the parameter can convert to integer
        try:
            number = int(number)
        except:
            status=1
            message = "The number you input is not right, an integer is expected"
            return (status, message)

        # return error if the request number is bigger than MAXIMUM setting
        if number > self.MAXIMUM:
            status = 1
            message = "The number is bigger than maximum limitation %s" % self.MAXIMUM
            return (status, message)

        # negative integer is not allowed
        if number <= 0 :
            status = 1
            message = "zero and negative integer is not allowed to generate fibonacci string"
            return (status, message)

        if number == 1:
            return (status, first_number)
        if number == 2:
            return (status, str(first_number) + " " + str(second_number))

        fobinacci_string = "1 1"
        index = 2
        while index < number:
            new_number = first_number + second_number
            first_number = second_number
            second_number = new_number
            fobinacci_string = str(fobinacci_string) + " " + str(new_number)
            index += 1
        return (status, fobinacci_string)
