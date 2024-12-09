import copy

"""

    PeanoNumber class for natural number class: number > 0 
    and can't give: number < 0
    
    In PeanoNumber is located 5 functions:
            sum 
            diff
            multiply
            integer_division
            division_with_remainder
            
    Arg of functions can be list[str], PeanoNumber and IntegerNumber.(PeanoNumber and IntegerNumber be converted to list)
    
    sum is remove from additive "զրոյ" and by count of list add in self.number in PeanoNumber "յաջորդ"
    
    diff is remove from removable and self.number "զրոյ"
      and by count of list remove in self.number of PeanoNumber "յաջորդ" of end in self.number be added "զրոյ"․
      It's functions can't calc if first number(self.number) fewer (<) than second number (additive)
    
    multiply is remove from multiple "զրոյ", create new number with 0 value 
      and sum number with self.number:(for reference error it is copy in other variable) 
      by multiple length's counts.
    
    integer_division 
      diff to divisor while self.number > divisor and added in other variable counts of diff
      and return counts of diffs
    division_with_remainder 
      diff to divisor while self.number > divisor and return remainder of self.number after all diffs
    
    
"""

class PeanoNumber:
    number: list[str] = []

    def __init__(self, number: list[str]):
        if "բացասական" in number:
            raise Exception(" because num < 0 program can't calc ")
        self.number = number.copy()

    def sum(self, additive):

        if isinstance(additive, PeanoNumber):
            additive = additive.number.copy()
        if "զրոյ" in additive:
            additive.pop(additive.index("զրոյ"))


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
        number_peano_one = PeanoNumber(["զրոյ"])

        for i in multiple:
            number_peano_one.sum(num_mult)

        if not "զրոյ" in number_peano_one.number:
            number_peano_one.number.append("զրոյ")

        return number_peano_one.number.copy()

    def integer_division(self, divisor):

        if isinstance(divisor, PeanoNumber):
            divisor = divisor.number.copy()

        quotient = PeanoNumber(["զրոյ"])
        if len(self.number) < len(divisor):
            raise Exception(" It's impossible calc ")
        if self.number == ["զրոյ"] or divisor == ["զրոյ"]:
            raise Exception(" Zero's impossible calc ")
        if self.number == divisor:
            return ["յաջորդ", "զրոյ"]

        number_one_peano = copy.deepcopy(self)

        while len(number_one_peano.number) > len(divisor):
            number_one_peano.diff(divisor)
            quotient.sum(["յաջորդ", "զրոյ"])


        return quotient.number.copy()

    def division_with_remainder(self, divisor):

        if isinstance(divisor, PeanoNumber):
            divisor = divisor.number.copy()



        number_one_peano = copy.deepcopy(self)
        if len(number_one_peano.number) == len(divisor):
            return ["զրոյ"]

        while len(number_one_peano.number) > len(divisor):
            number_one_peano.diff(divisor)
            if "զրոյ" in number_one_peano.number:
                number_one_peano.number.pop(number_one_peano.number.index("զրոյ"))

        number_one_peano.number.append("զրոյ")
        return number_one_peano

    def __str__(self):
        return f"{self.number}"
