def index_product(nums):
    parr = []
    product = 1
    
    for i in nums:
        if i == 0:
            continue
        product = product * i
    
    if 0 in nums:
        for i in range(len(nums)): 
            parr.append(0)
    else:
        for i in nums:
            if i != 0:
                parr.append(product / i)
            else :
                parr.append(product)
    for i in range(len(nums)): 
        if nums[i] == 0:
            parr[i] = product     

    return parr

print(str(index_product([1, 2, 3, 0, 5])))