def difference(*args: (int,float)):
    if len(args) == 0: return 0

    min_val = min(args)
    max_val = max(args)
    mydiff = round(max_val - min_val,2)

    return mydiff


print([1,2,3],"=>",difference(1,2,3))
print([5,-5],"=>",difference(5,-5))
print([10.2, -2.2, 0, 1.1, 0.5],"=>",difference(10.2, -2.2, 0, 1.1, 0.5))
print("difference()","=>",difference())