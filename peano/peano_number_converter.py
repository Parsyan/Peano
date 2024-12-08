import copy

from peano.integer_number import IntegerNumber
from peano.peano_fracton import PeanoFraction
from peano.peano_number import PeanoNumber


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

    def fraction_to_int(self, str_num : str):

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
