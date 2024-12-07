import copy
from copy import deepcopy


def sequent(number):
    seq_number = number.copy()
    seq_number.insert(0, "յաջորդ")
    return seq_number


zero: list[str] = ["զրոյ"]

one: list[str] = sequent(zero)

two: list[str] = sequent(one)

three: list[str] = sequent(two)

four: list[str] = sequent(three)

five: list[str] = sequent(four)

six: list[str] = sequent(five)

seven: list[str] = sequent(six)

eight: list[str] = sequent(seven)

nine: list[str] = sequent(eight)


class PeanoNumberConverter:

    def str_to_int(self, str_num: str):
        ten = nine.copy()
        ten.insert(0, "յաջորդ")

        minus = "բացասական"

        int_peano_number = PeanoNumber(zero)
        is_minus = False
        if "-" in str_num:
            is_minus = True
            str_num = str_num.replace("-", "")

        for i in range(len(str_num)):
            int_peano_number.sum(self.check_digit(str_num[i]))

            if not i >= (len(str_num) - 1):
                int_peano_number.number = int_peano_number.multiply(ten)

        if is_minus:
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

    def diff(self, removable):

        if isinstance(removable, PeanoNumber):
            removable = removable.number.copy()
        if "զրոյ" in removable:
            removable.pop(removable.index("զրոյ"))
        if "զրոյ" in self.number:
            self.number.pop(self.number.index("զրոյ"))

        if len(self.number) > len(removable):  # TODO check on Vahagn's lesson check operator

            for i in removable:
                self.number.pop()
            self.number.append("զրոյ")

        elif len(self.number) < len(removable):
            raise Exception(" because num1 < num2 program can't calc ")

        elif len(self.number) == len(removable):  # TODO check on Vahagn's lesson check operator
            self.number = ["զրոյ"]

        return self.number

    def multiply(self, multiple):

        if isinstance(multiple, PeanoNumber):
            multiple = multiple.number.copy()

        num_mult = self.number.copy()
        multiple.pop()
        number_peano_one = PeanoNumber(zero.copy())

        for i in multiple:
            number_peano_one.sum(num_mult)
        if not "զրոյ" in number_peano_one.number:
            number_peano_one.number.append("զրոյ")

        return number_peano_one.number.copy()

    def integer_division(self, divisor):

        if isinstance(divisor, PeanoNumber):
            divisor = divisor.number.copy()

        quotient = PeanoNumber(zero)
        if len(self.number) < len(divisor):
            raise Exception(" It's impossible calc ")
        if self.number == zero.copy() or divisor == zero.copy():
            raise Exception(" Zero's impossible calc ")
        if self.number == divisor:
            return one.copy()

        number_one_peano = copy.deepcopy(self)

        while len(number_one_peano.number) > len(divisor):
            number_one_peano.diff(divisor)
            quotient.sum(one)


        return quotient

    def division_with_remainder(self, divisor):

        if isinstance(divisor, PeanoNumber):
            divisor = divisor.number.copy()



        number_one_peano = copy.deepcopy(self)
        if len(number_one_peano.number) == len(divisor):
            return zero.copy()

        while len(number_one_peano.number) > len(divisor):
            number_one_peano.diff(divisor)
            if "զրոյ" in number_one_peano.number:
                number_one_peano.number.pop(number_one_peano.number.index("զրոյ"))

        number_one_peano.number.append("զրոյ")
        return number_one_peano

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

            number_peano_one = PeanoNumber(self.number.copy())

            for i in additive:
                number_peano_one.number.insert(0, i)
            self.number = number_peano_one.number.copy()

            self.number.insert(0, minus)

        else:

            if len(self.number) > len(additive):  # TODO check on Vahagn's lesson check operator

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

                first_num_is_minus: bool

                if "բացասական" in additive:
                    additive.pop(additive.index("բացասական"))
                    first_num_is_minus = True

                else:
                    if "բացասական" in additive:
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

    def diff(self, removable):

        if isinstance(removable, PeanoNumber):
            removable = removable.number.copy()

        if "զրոյ" in removable:
            removable.pop(removable.index("զրոյ"))
        if "զրոյ" in self.number:
            self.number.pop(self.number.index("զրոյ"))

        if not "բացասական" in self.number and not "բացասական" in removable:

            if len(self.number) > len(removable):  # TODO check on Vahagn's lesson check operator

                for i in removable:
                    self.number.pop()
                self.number.append("զրոյ")

            elif len(self.number) < len(removable):  # TODO check on Vahagn's lesson check operator
                minus = "բացասական"
                for i in self.number:
                    removable.pop()
                self.number = removable.copy()

                self.number.insert(0, minus)
                self.number.append("զրոյ")


            elif len(self.number) == len(removable):  # TODO check on Vahagn's lesson check operator
                self.number = ["զրոյ"]

        elif "բացասական" in self.number and "բացասական" in removable:
            removable.pop(removable.index("բացասական"))
            self.sum(removable)


        elif "բացասական" in self.number and not "բացասական" in removable:
            self.number.pop(self.number.index("բացասական"))

            self.number.append("զրոյ")

            self.sum(removable)
            self.number.insert(0, "բացասական")


        elif not "բացասական" in self.number and "բացասական" in removable:
            removable.pop(removable.index("բացասական"))

            self.number.append("զրոյ")

            self.sum(removable)

        return self.number

    def multiply(self, multiple):

        if isinstance(multiple, PeanoNumber):
            multiple = multiple.number

        if "բացասական" in self.number and "բացասական" in multiple:
            self.number.pop(self.number.index("բացասական"))
            multiple.pop(multiple.index("բացասական"))
            peano_num = PeanoNumber(self.number.copy())
            peano_num = peano_num.multiply(multiple)
            self.number = peano_num.number.copy()
        elif not "բացասական" in self.number and not "բացասական" in multiple:
            peano_num = PeanoNumber(self.number.copy())
            peano_num = peano_num.multiply(multiple)
            self.number = peano_num.copy()
        else:
            if "բացասական" in self.number:
                self.number.pop(self.number.index("բացասական"))
            if "բացասական" in multiple:
                multiple.pop(multiple.index("բացասական"))

            peano_num = PeanoNumber(self.number.copy())
            peano_num = peano_num.multiply(multiple)
            self.number = peano_num.copy()
            self.number.insert(0, "բացասական")

        return self.number

    def integer_division(self, divisor):

        if isinstance(divisor, PeanoNumber):
            divisor = divisor.number

        if "բացասական" in self.number and "բացասական" in divisor:
            self.number.pop(self.number.index("բացասական"))
            divisor.pop(divisor.index("բացասական"))
            peano_number = PeanoNumber(self.number.copy())
            peano_number = copy.deepcopy(peano_number.integer_division(divisor))
            self.number = peano_number.number.copy()

        elif not "բացասական" in self.number and not "բացասական" in divisor:
            peano_number = PeanoNumber(self.number.copy())
            peano_number.integer_division(divisor)
            self.number = peano_number.number.copy()

        else:
            if "բացասական" in self.number:
                self.number.pop(self.number.index("բացասական"))
            if "բացասական" in divisor:
                divisor.pop(divisor.index("բացասական"))

            self.integer_division(divisor)
            self.number.insert(0, "բացասական")

        return self.number

    def division_with_remainder(self, divisor):

        if isinstance(divisor, PeanoNumber):
            divisor = divisor.number
        is_minus = False

        if "բացասական" in self.number:
            self.number.pop(self.number.index("բացասական"))
            is_minus = True

        if "բացասական" in divisor:
            divisor.pop(divisor.index("բացասական"))

        peano_number = PeanoNumber(self.number.copy())
        peano_number.division_with_remainder(divisor)

        self.number = peano_number.number.copy()

        if is_minus:
            self.number.insert(0, "բացասական")

        return self.number


peano_converter = PeanoNumberConverter()


class PeanoFraction(PeanoNumber):
    numerator: IntegerNumber
    denominator: PeanoNumber

    def __init__(self, numerator: IntegerNumber, denominator: PeanoNumber):
        if denominator.number == zero:
            raise Exception("Denominator of fraction cannot be zero")

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"numerator : {self.numerator}/ denominator {self.denominator}"

    def sum(self, additive): # TODO Reorganization your idea and made sum of PeanoFraction :: last problem !! global_denominator and denominator of self equals

        if self.numerator.number == zero:
            return additive

        if not isinstance(additive, PeanoFraction):
            raise Exception(" It is not Fraction for calc ")
        global_denominator: PeanoNumber

        # This is calculating global denominator code <<<

        if self.denominator.division_with_remainder(additive.denominator) == zero:
            global_denominator = deepcopy(self.denominator)
        elif additive.denominator.division_with_remainder(self.denominator) == zero:
            global_denominator = deepcopy(additive.denominator)
        else:
            global_denominator = PeanoNumber(self.denominator.multiply(additive.denominator).copy())
        # >>>

        # calculating numerators for sum  <<<
        self.numerator.multiply(global_denominator.integer_division(self.denominator))
        additive.numerator.multiply(global_denominator.integer_division(additive.denominator))
        # >>>

        # result <<<
        self.numerator.sum(additive.numerator)

        nzero = zero.copy()
        nzero.insert(0, "բացասական")

        if self.numerator.number == zero or self.numerator.number == nzero:
            return zero.copy()

        self.denominator = copy.deepcopy(global_denominator)
        # >>>

        return self


a = PeanoFraction(
                            IntegerNumber(peano_converter.str_to_int(input(" Input a number "))),
                            PeanoNumber(peano_converter.str_to_int(input(" Input a number ")))
                  )

b = PeanoFraction(
                           IntegerNumber(peano_converter.str_to_int(input(" Input a number "))),
                           PeanoNumber(peano_converter.str_to_int(input(" Input a number ")))
                  )
# a = PeanoNumber(peano_converter.str_to_int(input(" Input a number ")))
# b = PeanoNumber(peano_converter.str_to_int(input(" Input a number ")))

print(a)

print(a.sum(b))
