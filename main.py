class Function:
    var_1 = float()
    var_2 = float()
    operation_1 = None

    def Result(self, var_1, var_2, operation_1):
        self.var_1 = var_1
        self.var_2 = var_2
        self.operation_1 = operation_1
        if operation_1 == '+':
            return var_1 + var_2
        elif operation_1 == '-':
            return var_1 - var_2
        elif operation_1 == '*':
            return var_1 * var_2
        elif operation_1 == '/':
            return var_1 / var_2
        else:
            return 'Такой операции нет!'


class Three_numbers(Function):
    var_3 = float()

    def result(self, var_1, var_2, operation_1, var_3):
        self.var_3 = var_3
        var_12 = super(Three_numbers, self).Result(var_1, var_2, operation_1)
        return super(Three_numbers, self).Result(var_12, var_3, operation_1)


class Two_operations(Function):
    operation_2 = None

    def result(self, var_1, var_2, operation_1, operation_2):
        self.operation_2 = operation_2
        return super(Two_operations, self).Result(var_1, var_2, operation_1) + super(Two_operations, self).Result(var_1,
                                                                                                                  var_2,
                                                                                                                  operation_2)


# Задание 1. Создаем объект класса Function, выполняем операцию сложения двух чисел.
Fun_1 = Function()
print(Fun_1.Result(5, 7, '+'))

# Задание 2. Создаем объект класса Three_numbers, выполняем операцию умножения трех чисел. По иерархии это наследник класса Function.
Fun_2 = Three_numbers()
print(Fun_2.result(5, 7, '*', 8))

# Создаем объект класса Two_operations, выполняем операцию сложения двух чисел и умножения двух чисел. Получившиеся ответы складываем. По иерархии это наследник класса Function.
Fun_3 = Two_operations()
print(Fun_3.result(5, 7, '+', '*'))

print(Fun_2.result(5, 7, '*', 8) + Fun_3.result(5, 7, '+', '*'))


# Дополнительное задание. Я реализовал сложение комплексных чисел.
class Complex:
    def Set_Value(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        result = Complex()
        result.real = self.real + other.real
        result.image = self.image + other.image
        return result

    def print_result(self):
        print(self.real, '+', self.image, 'i')


comp_1 = Complex()
comp_2 = Complex()
comp_1.Set_Value(5, 3)
comp_2.Set_Value(8, 2)

comp_3 = comp_1 + comp_2
comp_3.print_result()
