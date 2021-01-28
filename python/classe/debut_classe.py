val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
print(val[2])

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(59))

print(dir(list))

"""
result = ""
num = 59
while(num > 0):
    for ii, i in enumerate(val):
        if ((num % i) == 0) and (num > 0):
            num = num - i
            result = syb[ii] + result
            print(result)
"""
"""
for i in val:
    while (num > 0):
        count = 0
        if (num % i == 0):
            print(num)
            result += syb[count]
            num = (num - i)
            count += 1
        else:
            count += 1
#my_num = py_solution
#print(my_num.int_to_Roman(7, 7))
print(result)
"""
