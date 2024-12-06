

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

class PeanoNumberConverter:

    def str_to_int(self, str_num: str):
        ten = nine.copy()
        ten.insert(0, "յաջորդ")

        minus = "բացասական"

        int_peano_number = PeanoNumber(zero)
        isminus = False
        if "-" in str_num:
            isminus = True
            str_num = str_num.replace("-", "")

        for i in range(len(str_num)):
            int_peano_number.sum(self.check_digit(str_num[i]))

            if not i >= (len(str_num) - 1):
                int_peano_number.multiply(ten)

        if isminus:
            int_peano_number.number.insert(0, minus)

        return int_peano_number.number.copy()

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


class PeanoNumber:
    log = False
    number: list[str] = []

    def __init__(self, number: list[str]):
        if "բացասական" in number:
            raise Exception(" because num < 0 program can't calc ")
        self.number = number.copy()

    def sum(self, additive):

        if isinstance(additive, IntegerNumber):
            additive.sum(self.number)
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
        if "զրոյ" in number_peano:
            number_peano.pop(number_peano.index("զրոյ"))
        if "զրոյ" in self.number:
            self.number.pop(self.number.index("զրոյ"))


        if len(self.number) > len(number_peano):  # TODO check on Vahagn's lesson check operator

            for i in number_peano:
                self.number.pop()
            self.number.append("զրոյ")

        elif len(self.number) < len(number_peano):
            raise Exception(" because num1 < num2 program can't calc ")

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

        quotient = PeanoNumber(zero)
        if len(self.number) < len(number_peano):
            raise Exception(" It's impossible calc ")
        if self.number == zero.copy() or number_peano == zero.copy():
            raise Exception(" Zero's impossible calc ")

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



class IntegerNumber(PeanoNumber):
    number: list[str] = []


    def __init__(self, number: list[str]):
        self.number = number.copy()

    def sum(self, additive):

        if isinstance(additive, PeanoNumber):
            additive = additive.number.copy()


        if "զրոյ" in additive:
            additive.pop(additive.index("զրոյ"))

        minus = "բացասական"

        if not "բացասական" in self.number and not "բացասական" in additive:
            for i in additive:
                self.number.insert(0, i)

        elif "բացասական" in self.number and "բացասական" in additive:
            self.number.pop(self.number.index("բացասական"))
            additive.pop(additive.index("բացասական"))
            super().number = self.number.copy()
            for i in additive:
                super().number.insert(0, i)
            self.number = super().number.copy()

            self.number.insert(0, minus)

        else:

            if len(self.number) > len(additive): # TODO check on Vahagn's lesson check operator

                if "բացասական" in self.number:
                    self.number.pop(self.number.index("բացասական"))

                    peano_num = PeanoNumber(self.number.copy())


                    peano_num.diff(additive)
                    self.number = peano_num.number.copy()

                    self.number.insert(0, "բացասական")

                else:
                    additive.pop(additive.index("բացասական"))

                    peano_num = PeanoNumber(self.number.copy())
                    peano_num.diff(additive)

                    self.number = peano_num.number.copy()




            elif len(self.number) < len(additive):  # TODO check on Vahagn's lesson check operator

                first_num_is_minus : bool

                if "բացասական" in additive:
                    additive.pop(additive.index("բացասական"))
                    first_num_is_minus = True

                else:
                    additive.pop(additive.index("բացասական"))
                    first_num_is_minus = False

                additive.append("զրոյ")

                for i in self.number:
                    additive.pop()

                additive.insert(0, minus)
                self.number = additive.copy()

                if not first_num_is_minus:
                    self.number.insert(0, "բացասական")

            elif len(self.number) == len(additive):  # TODO check on Vahagn's lesson check operator
                self.number = ["զրոյ"]



        return self.number

    def diff(self, number_peano):

        if isinstance(number_peano, PeanoNumber):
            number_peano = number_peano.number.copy()

        if "զրոյ" in number_peano:
            number_peano.pop(number_peano.index("զրոյ"))
        if "զրոյ" in self.number:
            self.number.pop(self.number.index("զրոյ"))

        if not "բացասական" in self.number and not "բացասական" in number_peano:

            if len(self.number) > len(number_peano):  # TODO check on Vahagn's lesson check operator

                for i in number_peano:
                    self.number.pop()
                self.number.append("զրոյ")

            elif len(self.number) < len(number_peano):  # TODO check on Vahagn's lesson check operator
                minus = "բացասական"
                for i in self.number:
                    number_peano.pop()
                self.number = number_peano.copy()

                self.number.insert(0, minus)
                self.number.append("զրոյ")


            elif len(self.number) == len(number_peano):  # TODO check on Vahagn's lesson check operator
                self.number = ["զրոյ"]

        elif "բացասական" in self.number and "բացասական" in number_peano:
            number_peano.pop(number_peano.index("բացասական"))
            self.sum(number_peano)


        elif "բացասական" in self.number and not "բացասական" in number_peano:
            self.number.pop(self.number.index("բացասական"))

            self.number.append("զրոյ")

            self.sum(number_peano)
            self.number.insert(0, "բացասական")


        elif not "բացասական" in self.number and "բացասական" in number_peano:
            number_peano.pop(number_peano.index("բացասական"))

            self.number.append("զրոյ")

            self.sum(number_peano)


        return self.number

    def multiply(self, number_peano):

        if isinstance(number_peano, PeanoNumber):
            number_peano = number_peano.number

        if "բացասական" in self.number and "բացասական" in number_peano:
            self.number.pop(self.number.index("բացասական"))
            number_peano.pop(number_peano.index("բացասական"))
            peano_num = PeanoNumber(self.number.copy())
            peano_num.multiply(number_peano)
            self.number = peano_num.number.copy()
        elif not "բացասական" in self.number and not "բացասական" in number_peano:
            peano_num = PeanoNumber(self.number.copy())
            peano_num.multiply(number_peano)
            self.number = peano_num.number.copy()
        else:
            if "բացասական" in self.number:
                self.number.pop(self.number.index("բացասական"))
            if "բացասական" in number_peano:
                number_peano.pop(number_peano.index("բացասական"))

            peano_num = PeanoNumber(self.number.copy())
            peano_num.multiply(number_peano)
            self.number = peano_num.number.copy()
            self.number.insert(0, "բացասական")



        return self.number

    def integer_division(self, number_peano):


        if isinstance(number_peano, PeanoNumber):
            number_peano = number_peano.number

        if "բացասական" in self.number and "բացասական" in number_peano:
            self.number.pop(self.number.index("բացասական"))
            number_peano.pop(number_peano.index("բացասական"))
            peano_number = PeanoNumber(self.number.copy())
            peano_number.integer_division(number_peano)
            self.number = peano_number.number.copy()

        elif not "բացասական" in self.number and not "բացասական" in number_peano:
            peano_number = PeanoNumber(self.number.copy())
            peano_number.integer_division(number_peano)
            self.number = peano_number.number.copy()

        else:
            if "բացասական" in self.number:
                self.number.pop(self.number.index("բացասական"))
            if "բացասական" in number_peano:
                number_peano.pop(number_peano.index("բացասական"))

            self.integer_division(number_peano)
            self.number.insert(0, "բացասական")

        return self.number

    def division_with_remainder(self, number_peano):

        if isinstance(number_peano, PeanoNumber):
            number_peano = number_peano.number
        isMinus = False

        if "բացասական" in self.number:
            self.number.pop(self.number.index("բացասական"))
            isMinus = True

        if "բացասական" in number_peano:
            number_peano.pop(number_peano.index("բացասական"))


        peano_number = PeanoNumber(self.number.copy())
        peano_number.division_with_remainder(number_peano)

        self.number = peano_number.number.copy()

        if isMinus:
            self.number.insert(0, "բացասական")



        return self.number

peano_converter = PeanoNumberConverter()

a = IntegerNumber(peano_converter.str_to_int(input(" Input a number ")))
b = IntegerNumber(peano_converter.str_to_int(input(" Input a number ")))


# nfive = five.copy()
# nfive.insert(0, "բացասական")
print(a)
print(a.division_with_remainder(b))
# print(" integer division ")
# print(b)
# print(" = ")
# print(a.multiply(b))
