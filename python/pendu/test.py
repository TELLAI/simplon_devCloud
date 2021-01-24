"""class py_solution:
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
        result = ""
        while (num > 0):
             for ii, i in enumerate(val):
                if ((type(num // i)) == int):
                    result += syb[ii]
                    num = num % i
                    print(result)
        return result

my_num = py_solution()
print(my_num.int_to_Roman(7))"""

print(type(1.5))