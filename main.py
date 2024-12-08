from peano.peano_number_converter import PeanoNumberConverter





peano_converter = PeanoNumberConverter()



# a = PeanoNumber(peano_converter.str_to_int(input(" input a number")))
# b = IntegerNumber(peano_converter.str_to_int(input(" input a number")))

a = peano_converter.str_to_int(input(" Input a fraction like this 'n/m' n and m are numbers like 1,2,3 ... "))

b = peano_converter.str_to_num_peano(input(" Input a fraction like this 'n/m' n and m are numbers like 1,2,3 ... "))

print(a)

print(a.diff(b))
