import copy


from peano.peano_number import PeanoNumber

from peano.integer_number import IntegerNumber


class PeanoFraction:
    numerator: IntegerNumber
    denominator: PeanoNumber

    def __init__(self, numerator: IntegerNumber, denominator: PeanoNumber):
        if denominator.number == ["զրոյ"]:
            raise Exception("Denominator of fraction cannot be 0")

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"numerator : {self.numerator}/ denominator {self.denominator}"

    def sum(self, additive): # TODO Reorganization your idea and made sum of PeanoFraction :: last problem !! global_denominator and denominator of self equals

        if self.numerator.number == additive.numerator.number and self.numerator.number == ["զրոյ"]:
            return ["զրոյ"]

        if self.numerator.number == ["զրոյ"]:
            return additive

        if not isinstance(additive, PeanoFraction):
            raise Exception(" It is not Fraction for calc ")
        global_denominator: PeanoNumber

        # This is calculating global denominator code <<<

        if self.denominator.division_with_remainder(additive.denominator) == ["զրոյ"]:
            global_denominator = copy.deepcopy(self.denominator)
        elif additive.denominator.division_with_remainder(self.denominator) == ["զրոյ"]:
            global_denominator = copy.deepcopy(additive.denominator)
        else:
            global_denominator = PeanoNumber(self.denominator.multiply(additive.denominator).copy())
        # >>>

        # calculating numerators for sum  <<<
        self.numerator.multiply(global_denominator.integer_division(self.denominator))
        additive.numerator.multiply(global_denominator.integer_division(additive.denominator))
        # >>>

        # sum <<<
        self.numerator.sum(additive.numerator)
        # >>>

        # result <<<

        minus_zero = ["զրոյ"]
        minus_zero.insert(0, "բացասական")

        if self.numerator.number == ["զրոյ"] or self.numerator.number == ["զրոյ"]:
            return ["զրոյ"]

        self.denominator = copy.deepcopy(global_denominator)
        # >>>

        return self

    def diff(self, additive): # TODO Reorganization your idea and made sum of PeanoFraction :: last problem !! global_denominator and denominator of self equals

        if self.numerator.number == additive.numerator.number and self.numerator.number == ["զրոյ"]:
            return ["զրոյ"]

        if self.numerator.number == ["զրոյ"]:
            if "բացասական" in additive.numerator.number:
                additive.numerator.number.pop(additive.numerator.index("բացասական"))
                return additive
            else:
                additive.numerator.number.insert(0, "բացասական")
                return additive


        if not isinstance(additive, PeanoFraction):
            raise Exception(" It is not Fraction for calc ")
        global_denominator: PeanoNumber

        # This is calculating global denominator code <<<

        if self.denominator.division_with_remainder(additive.denominator) ==["զրոյ"]:
            global_denominator = copy.deepcopy(self.denominator)
        elif additive.denominator.division_with_remainder(self.denominator) ==["զրոյ"]:
            global_denominator = copy.deepcopy(additive.denominator)
        else:
            global_denominator = PeanoNumber(self.denominator.multiply(additive.denominator).copy())
        # >>>

        # calculating numerators for sum  <<<
        self.numerator.multiply(global_denominator.integer_division(self.denominator))
        additive.numerator.multiply(global_denominator.integer_division(additive.denominator))
        # >>>

        # diff <<<
        self.numerator.diff(additive.numerator)
        # >>>

        minus_zero =["զրոյ"].copy()
        minus_zero.insert(0, "բացասական")

        if self.numerator.number ==["զրոյ"] or self.numerator.number == ["զրոյ"]:
            return ["զրոյ"].copy()

        # result <<<
        self.denominator = copy.deepcopy(global_denominator)
        # >>>

        return self

    def multiply(self, multiple):
        if self.numerator.number == ["զրոյ"] or multiple.numerator.number == ["զրոյ"]:
            return ["զրոյ"].copy()

        if not isinstance(multiple, PeanoFraction):
            raise Exception(" It is not Fraction for calc ")

        self.numerator = self.numerator.multiply(multiple.numerator)
        self.denominator = self.denominator.multiply(multiple.denominator)

        return self

    def division(self, divisor):
        if self.numerator.number == ["զրոյ"] or divisor.numerator.number == ["զրոյ"]:
            return ["զրոյ"].copy()

        divisor_numerator = copy.deepcopy(divisor.numerator)

        divisor.numerator = copy.deepcopy(divisor.denominator)
        if "բացասական" in divisor_numerator.number:
            divisor_numerator.number.pop(divisor_numerator.number.index("բացասական"))
            divisor.numerator.number.insert(0, "բացասական")

        divisor.denominator = copy.deepcopy(divisor_numerator)

        self.numerator = self.numerator.multiply(divisor.numerator)
        self.denominator = self.denominator.multiply(divisor.denominator)

        return self
