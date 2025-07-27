from collections import OrderedDict

regular_dict = {}
regular_dict['a'] = 1
regular_dict['b'] = 2
regular_dict['c'] = 3
regular_dict['d'] = 4

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print("regular_dict:", regular_dict)
print("ordered_dict:", ordered_dict)

ordered_dict.move_to_end('b')  # 'b'
print("OrderedDict after move_to_end('b'):", ordered_dict)
