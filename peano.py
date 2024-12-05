def sequent(number):
    seq_number = number.copy()
    seq_number.insert(0, "յաջորդ")
    return seq_number


zero : list[str] = ["զրոյ"]

one : list[str] = sequent(zero)

two : list[str] = sequent(one)

three : list[str] = sequent(two)

four : list[str] = sequent(three)

five : list[str] = sequent(four)

six : list[str] = sequent(five)

seven : list[str] = sequent(six)

eight : list[str] = sequent(seven)

nine : list[str] = sequent(eight)



# def str_to_int(str_num : str):
#     number = []
#     for i in str_num:
#
#     pass


class PeanoNumber:
    log = False
    number: list[str] = []

    def __init__(self, number: list[str]):
        self.number = number.copy()

    def sum(self, additive):

        if isinstance(additive, PeanoNumber):
            additive = additive.number.copy()
        if "զրոյ" in additive:
            additive.pop(additive.index("զրոյ"))

        if self.log:
            print(" Starting Sum ")

        for i in additive:
            self.number.insert(0, i)

        return self.number

    def diff(self, number_peano):

        if isinstance(number_peano, PeanoNumber):
            number_peano = number_peano.number.copy()

        number_peano.pop(number_peano.index("զրոյ"))
        self.number.pop(self.number.index("զրոյ"))


        if len(self.number) > len(number_peano):  # TODO check on Vahagn's lesson check operator

            for i in number_peano:
                self.number.pop()
            self.number.append("զրոյ")

        elif len(self.number) < len(number_peano):  # TODO check on Vahagn's lesson check operator

            for i in self.number:
                number_peano.pop()
            number_peano.insert(0, "-")
            self.number = number_peano.copy()

        elif len(self.number) == len(number_peano):  # TODO check on Vahagn's lesson check operator
            self.number = ["զրոյ"]

        return self.number

    def multiply(self, number_peano):

        if isinstance(number_peano, PeanoNumber):
            number_peano = number_peano.number

        num_mult = self.number.copy()
        number_peano.pop()
        self.number = []

        for i in number_peano:
            self.sum(num_mult)

        self.number.append("զրոյ")
        return self.number

    def integer_division(self, number_peano):

        if isinstance(number_peano, PeanoNumber):
            number_peano = number_peano.number

        quotient = PeanoNumber("0")

        while len(self.number) > len(number_peano):
            self.diff(number_peano)
            quotient.sum(one)

        self.number = quotient.number.copy()

        return quotient

    def division_with_remainder(self, number_peano):

        if isinstance(number_peano, PeanoNumber):
            number_peano = number_peano.number

        quotient = PeanoNumber(zero)

        while len(self.number) > len(number_peano):
            self.diff(number_peano)
            quotient.sum(one)

        return self.number

    def __str__(self):
        return f"{self.number}"

    class PeanoNumberConverter:

        def str_to_int(self, str_num: str):
            ten = nine.copy()
            ten.insert(0, "յաջորդ")

            int_number = PeanoNumber(zero)

            for i in range(len(str_num)):
                int_number.sum(self.check_digit(str_num[i]))

                if not i >= (len(str_num) - 1):
                    int_number.multiply(ten)

            return int_number.number.copy()

        @staticmethod
        def check_digit(str_num: str):
            number = []

            if not len(str_num) == 1:
                raise Exception(" Program can't work with input symbols or number than 9 ")
            if str_num == "0":
                number = zero
            elif str_num == "1":
                number = one
            elif str_num == "2":
                number = two
            elif str_num == "3":
                number = three
            elif str_num == "4":
                number = four
            elif str_num == "5":
                number = five
            elif str_num == "6":
                number = six
            elif str_num == "7":
                number = seven
            elif str_num == "8":
                number = eight
            elif str_num == "9":
                number = nine
            else:
                raise Exception(" Type a number  < 10")

            return number.copy()

# def str_to_int(str_num: str):
#     ten = nine.copy()
#     ten.insert(0, "յաջորդ")
#
#     int_number = PeanoNumber(zero)
#
#
#
#     for i in range(len(str_num)):
#         int_number.sum(check_digit(str_num[i]))
#
#         if not i >= (len(str_num) - 1):
#             int_number.multiply(ten)
#
#     return int_number.number.copy()
#
# def check_digit(str_num: str):
#     number = []
#
#     if not len(str_num) == 1:
#         raise Exception(" Program can't work with input symbols or number than 9 ")
#     if str_num == "0":
#         number = zero
#     elif str_num == "1":
#         number = one
#     elif str_num == "2":
#         number = two
#     elif str_num == "3":
#         number = three
#     elif str_num == "4":
#         number = four
#     elif str_num == "5":
#         number = five
#     elif str_num == "6":
#         number = six
#     elif str_num == "7":
#         number = seven
#     elif str_num == "8":
#         number = eight
#     elif str_num == "9":
#         number = nine
#     else:
#         raise Exception(" Type a number  < 10")
#
#     return number.copy()
peano_converter = PeanoNumber.PeanoNumberConverter()

a = PeanoNumber(peano_converter.str_to_int(input(" Input a number ")))


# b = PeanoNumber(input(" Input a number "))
print(a)
# print(" integer division ")
# print(b)
# print(" = ")
# print(a.multiply(b))
