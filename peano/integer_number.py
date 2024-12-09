import copy

from peano.peano_number import PeanoNumber

"""

    IntegerNumber class for integer number: 0 < number > 0 
    It's extended PeanoNumber class and overrides it's methods
    
    In IntegerNumber
     is located 5 functions:
            sum 
            diff
            multiply
            integer_division
            division_with_remainder

    Arg of functions can be list[str], PeanoNumber and IntegerNumber.(PeanoNumber and IntegerNumber be converted to list)

    sum is remove from additive "զրոյ" 
      and 
        if all two numbers are > 0: by count of list add in self.number in PeanoNumber "յաջորդ",
        if all two numbers are > 0: save "-" how "բացասական", 
            after by count of list add in self.number in PeanoNumber "յաջորդ" and add "բացասական" in result
        else:
            is_first_minus : bool type
            if "բացասական" in first num
                delete "բացասական"
                is_first_minus = True
            else 
                delete "բացասական"
                is_first_minus = False
                
            if first num > second num 
                first num diff to second num 
                if is_first_minus == True # only is_first_minus equal to this condition
                    add "բացասական" in first num
            if first num < second num
                second num diff to first num
                if is_first_minus == False 
                    add "բացասական" in second num
        
    diff 
      if first num > 0 and second num < 0 will be sum first num and second num absolute value
      
      if first num > 0 and second num > 0 will be diff first num and second num absolute value
      
      if first num < 0 and second num > 0 will be sum first num and second num absolute value 
        and added "բացասական" in result
        
      if first num < 0 and second num < 0: 
        if first num > second num will be diff to second num and added "բացասական" in result
        if first num < second num will be diff to first num


    multiply 
        if first num > 0 and second num > 0 will be first num multiply to second num
        if first num < 0 and second num < 0 will be deleted "բացասական" in all two numbers and
         first num multiply to second num
        else
            if first num < 0 will be deleted "բացասական" in first_num
            if second num < 0 will be deleted "բացասական" in second num
            after will be first num multiply to second num
            and in the result added "բացասական"
        

    integer_division ##Descryption: division method likes multiply method 
      if first num > 0 and second num > 0 result will be > 0 
      if first num < 0 and second num < 0 result will be > 0
      else 
        if first num < 0 or second num < 0 result will be < 0
          
    division_with_remainder 
      if first num > 0 result will be > 0
      if first num < 0 result will be < 0
      
      # How is that possible? 
      # 4 / 3 = 1 (1) 4 = 3 * 1 + 1
      # if remainder be > 0 when 4 < 0 
      # -4 / 3 = -1 (1) 
      # -4 != 3 * (-1) + 1 = 2
      # -4 = 3 * (-1) - 1   

Description: if you want know how realized 
    sum, diff, multiply, integer_division and division_with_remainder
    you can check peano/peano/peano_number.py file

Description: __str__ method realized in PeanoNumber and
 when IntegerNumber extend PeanoNumber it give and __str__ method also.
 Because of it in this code that's method not realized.


"""


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

            first_num_is_minus: bool

            if "զրոյ" in self.number:
                self.number.pop(self.number.index("զրոյ"))

            if "բացասական" in self.number:
                self.number.pop(self.number.index("բացասական"))
                first_num_is_minus = True
            else:
                additive.pop(additive.index("բացասական"))
                first_num_is_minus = False

            if len(self.number) > len(additive):

                peano_num = PeanoNumber(self.number.copy())

                peano_num.diff(additive)
                self.number = peano_num.number.copy()

                if first_num_is_minus:
                    self.number.insert(0, "բացասական")

            elif len(self.number) < len(additive):

                    peano_num = PeanoNumber(additive.copy())

                    peano_num.diff(self.number.copy())

                    additive = peano_num.number.copy()

                    if not first_num_is_minus:
                        additive.insert(0, "բացասական")

                    self.number = additive.copy()


            elif len(self.number) == len(additive):
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

            if len(self.number) > len(removable):

                for i in removable:
                    self.number.pop()
                self.number.append("զրոյ")

            elif len(self.number) < len(removable):
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
