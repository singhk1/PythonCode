def product_except_self(ls):
    product = 1
    zeros = 0
    for id, i in enumerate(ls):
        if i == 0:
            zeros += 1
        else:
            product *= i
    if zeros > 1:
        return [0]*len(ls)
    new_ls = []
    for id, i in enumerate(ls):
        if zeros:
            if i == 0:
                new_ls.append(product)
            else:
                new_ls.append(0)
        else:
            new_ls.append(product // i)
    return new_ls

def productExceptSelf(nums):
        out_array = [0 for i in range(len(nums))]
        out_array[0] = 1

        for i in range(1, len(nums)):
            out_array[i] = nums[i - 1] * out_array[i - 1]
        #print(out_array)
        r = 1
        for i in reversed(range(len(nums))):
            out_array[i] = out_array[i] * r
            r = r * nums[i]
        return out_array

ls1 = [1, 2, 3, 4, 5]
#print(product_except_self(ls1))
ls2 = [0, 1]
#print(product_except_self(ls2))
ls3 = [0, 1, 0]
#print(product_except_self(ls3))
print(productExceptSelf(ls1))
print(productExceptSelf(ls2))
