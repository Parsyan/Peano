import copy


from peano.peano_number import PeanoNumber

from peano.integer_number import IntegerNumber

"""

    PeanoFraction class for fraction number: "4/5".
    
    numerator can be less (<) than 0 and more (>) than zero
        and if numerator zero fraction is zero
    
    denominator can't be less (<) than 0 and be zero
    
    IntegerNumber can be < 0 > and be 0 
    PeanoNumber can't be < 0 
        but can be 0 it's problem can solution in class constructor 
    

    PeanoFraction structure
        numerator : IntegerNumber
        denominator : PeanoNumber
    
    PeanoFraction methods:
        sum
        diff
        multiply
        division
        
        sum
            for since check for zero numerators of two numbers
            after arg check we calc global denominator
            after by global providing we calc numerators
            after sum numerators
        diff
            for since check for zero numerators of two numbers
            after arg check we calc global denominator
            after by global providing we calc numerators
            after diff numerators
        multiply
            for since check for zero numerators of two numbers 
                and if on of numbers zero results zero
            after arg check
            first fraction numerator multiply to second fraction numerator
            first fraction denominator multiply to second fraction denominator
        division
            for since check for zero numerators of two numbers 
                and if on of numbers zero results zero
            reverse value of second fraction 
                (numerator to denominator, denominator to numerator)
            
"""

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

    def sum(self, additive):

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

    def diff(self, additive):

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
