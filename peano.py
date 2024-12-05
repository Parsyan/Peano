def sequent(number):
    seq_number = number.copy()
    seq_number.insert(0, "յաջորդ")
    return seq_number


zero = ["զրոյ"]

one = sequent(zero)

two = sequent(one)

three = sequent(two)

four = sequent(three)

five = sequent(four)

six = sequent(five)

seven = sequent(six)

eight = sequent(seven)

nine = sequent(eight)


class PeanoNumber:
    log = False
    number: list[str] = []

    def __init__(self, num):
        if not isinstance(num, str):
            raise SyntaxError(" Your number must be in str ")

        if num == "0":
            self.number = zero
        elif num == "1":
            self.number = one
        elif num == "2":
            self.number = two
        elif num == "3":
            self.number = three
        elif num == "4":
            self.number = four
        elif num == "5":
            self.number = five
        elif num == "6":
            self.number = six
        elif num == "7":
            self.number = seven
        elif num == "8":
            self.number = eight
        elif num == "9":
            self.number = nine
        else:
            raise Exception(" Type a number  < 10")

        self.number = self.number.copy()

    def sum(self, additive):

        if isinstance(additive, PeanoNumber):
            additive = additive.number.copy()

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


# def sum_peano_numbers(first_num_peano, second_num_peano):
# result = first_num_peano.copy()
#
# second_num_peano.pop()
# for i in second_num_peano:
#     result.insert(0, i)
# return result

a = PeanoNumber(input(" Input a number "))
b = PeanoNumber(input(" Input a number "))
print(a)
print(" integer division ")
print(b)
print(" = ")
print(a.diff(b))
