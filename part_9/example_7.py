import sys

nums_lc = [i ** 2 for i in range(1000000)]
print(sys.getsizeof(nums_lc))

nums_gc = (i ** 2 for i in range(1000000))
print(sys.getsizeof(nums_gc))

# 1 000   10 000   100 000   1 000 0000
# 8856    85176    800984    8448728
# 208     208      208       208
#