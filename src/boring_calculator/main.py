
class Calculator():
    '''
    Calculator can perform supported operations against value in memory
    Default memory value is float 0. Operations are performed with floats.
    '''
    def __init__(self):
        self.memory = 0.0

    def add(self, value: float) -> float:
        '''
        Adds the provided value to the value saved in memory.

        :param value: The value to be added to the in-memory value.
        :return: The updated in-memory value after addition.
        '''
        self.memory += value
        return self.memory

    def subtract(self, value: float) -> float:
        '''
        Subtracts the provided value from the value saved in memory.

        :param value: The value to be subtracted from the in-memory value.
        :return: The updated in-memory value after subtraction.
        '''
        self.memory -= value
        return self.memory

    def divide(self, value: float) -> float:
        '''
        Divides value saved in memory by provided value
        :param value: value how much to divide the value saved in memory
        :return: new in memory value after division
        '''
        self.memory = self.memory / value
        return self.memory

    def multiply(self, value: float) -> float:
        '''
        Multiplies the value saved in memory by the provided value.

        :param value: The value by which to multiply the in-memory value.
        :return: The updated in-memory value after multiplication.
        '''
        self.memory = self.memory * value
        return self.memory

    def root(self, n: int) -> float:
        '''
        Raises the value saved in memory to the power of 1 divided by the
        provided value.

        :param value: The value to be used as the divisor in the exp (1/value).
        :return: The updated in-memory value after applying the root.
        '''
        self.memory = self.memory ** (1.0/n)
        return self.memory

    def reset(self) -> float:
        '''
        Resets the value saved in memory to its initial state.

        :return: None
        '''
        self.memory = 0
        return self.memory
