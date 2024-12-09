import copy

from peano.integer_number import IntegerNumber
from peano.peano_fraction import PeanoFraction
from peano.peano_number import PeanoNumber

"""
    PeanoNumberConverter class for work with custom creating numbers how:
        PeanoNumber class for natural numbers in peano/peano/peano_number.py
        IntegerNumber class for integer numbers in peano/peano/integer_number.py
        PeanoFraction class for fraction numbers in peano/peano/peano_fraction.py
    In PeanoNumberConverter is located 4 methods
        str_to_fraction arg syntax must be like this :"1/3" 
        str_to_int arg syntax must be like this : "5", "-4"
        str_to_num_peano arg syntax must be like this : "8" and can't be < 0 
        
        check_digit arg str len == 1 and get in dict by key "0" -> "զրոյ"
        
        str_to_fraction give "2/4" by example divide to ["2", "4"] and convert for numerator and denominator
        denominator can't be zero 
        
        str_to_int "554" -> (("5" -> check_digit) * 10 + ("5" -> check_digit)) * 10 + ("4" -> check_digit) 
        str_to_num_peano work like str_to_int but save since "-" how "բացասական"
        

"""

class PeanoNumberConverter:

    nums: dict[str:list[str]] = {
        "0": ["զրոյ"],
        "1": ["յաջորդ", "զրոյ"],
        "2": ["յաջորդ", "յաջորդ", "զրոյ"],
        "3": ["յաջորդ", "յաջորդ", "յաջորդ", "զրոյ"],
        "4": ["յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "զրոյ"],
        "5": ["յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "զրոյ"],
        "6": ["յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "զրոյ"],
        "7": ["յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "զրոյ"],
        "8": ["յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "զրոյ"],
        "9": ["յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "յաջորդ", "զրոյ"]
    }

    def str_to_fraction(self, str_num : str):

        fraction_mini = str_num.split("/")
        fraction = PeanoFraction(
            IntegerNumber(self.nums[fraction_mini[0]]),
            PeanoNumber(self.nums[fraction_mini[1]])
        )

        return fraction

    def str_to_int(self, str_num: str):
        ten = self.nums["9"].copy()
        ten.insert(0, "յաջորդ")

        minus = "բացասական"

        int_peano_number = IntegerNumber(self.nums["0"].copy())
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

        return copy.deepcopy(int_peano_number)

    def str_to_num_peano(self, str_num: str):
        ten = self.nums["9"].copy()
        ten.insert(0, "յաջորդ")


        peano_number = PeanoNumber(self.nums["0"].copy())

        for i in range(len(str_num)):
            peano_number.sum(self.check_digit(str_num[i]))

            if not i >= (len(str_num) - 1):
                peano_number.number = peano_number.multiply(ten)



        return copy.deepcopy(peano_number)

    def check_digit(self, str_num: str):
        number = []

        if not len(str_num) == 1:
            raise Exception(" Program can't work with input symbols or number than 9 ")

        number = self.nums[str_num]

        # else:
        #     raise Exception(" Type a number  < 10")

        return number.copy()
