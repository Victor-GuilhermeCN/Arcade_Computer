class BasicOperations:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def mult(self, value1, value2):
        return value1 * value2

    def div(self, value1, value2):
        return value1 / value2


class Verify:

    def __init__(self, value1, value2,):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def verify_if_is_a_number():
        try:
            value1 = int(input('1º Number: '))
            value2 = int(input('2º Number: '))
            if type(value1) != int:
                print('It is not a number.')
                return Verify.verify_if_is_a_number()
        except:
            print('It is not a number.')
            return Verify.verify_if_is_a_number
        else:
            user = BasicOperations(value1, value2)