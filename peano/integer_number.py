import copy

from peano.peano_number import PeanoNumber


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
            self.number = peano_num.copy()
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
