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
    number = []

    def __init__(self, num):
        if num == "0":
            self.number = zero
        if num == "1":
            self.number = one
        if num == "2":
            self.number = two
        if num == "3":
            self.number = three
        if num == "4":
            self.number = four
        if num == "5":
            self.number = five
        if num == "6":
            self.number = six
        if num == "7":
            self.number = seven
        if num == "8":
            self.number = eight
        if num == "9":
            self.number = nine

    def __init__(self, number_peano):
        self.number = number_peano

    def sum(self, additive):
        try:
            del additive[additive.index("զրոյ")]
        except ValueError as e:
            pass

        for i in additive:
            self.number.insert(0, i)

        return self.number

    def diff(self, number_peano):

        try:
            del number_peano[number_peano.index("զրոյ")]
        except ValueError as e:
            pass
        try:
            del self.number[self.number.index("զրոյ")]
        except ValueError as e:
            pass

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
        num_mult = self.number.copy()
        number_peano.pop()
        self.number = []

        for i in number_peano:
            self.sum(num_mult)

        self.number.append("զրոյ")
        return self.number

    def integer_division(self, number_peano):
        quotient = PeanoNumber(zero)

        while len(self.number) > len(number_peano):
            self.diff(number_peano)
            quotient.sum(one)

        self.number = quotient.number.copy()

        return quotient

    def division_with_remainder(self, number_peano):
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

a = PeanoNumber(five)

print(a)
print( " integer division " )
print(two)
print(" = ")
print(a.integer_division(two))
