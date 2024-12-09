from peano.peano_number_converter import PeanoNumberConverter

"""

    You must work with PeanoNumberConverter 
                            methods
                                str_to_int -> IntegerNumber
                                str_to_num_peano -> PeanoNumber
                                str_to_fraction -> PeanoFraction

"""



peano_converter = PeanoNumberConverter()

# a = (peano_converter.str_to_int(input(" input a number")))
# b = (peano_converter.str_to_int(input(" input a number")))

a = peano_converter.str_to_int(input(" Input a fraction like this 'n/m' n and m are numbers like 1,2,3 ... "))

b = peano_converter.str_to_int(input(" Input a fraction like this 'n/m' n and m are numbers like 1,2,3 ... "))

print(a)

print(a.sum(b))
