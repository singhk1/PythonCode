
import sys
def median(ls1, ls2):
    if len(ls1) > len(ls2):
        return median(ls2, ls1)

    x = len(ls1)
    y = len(ls2)
    maxsize = sys.maxsize
    minsize = -sys.maxsize -1
    low=0
    high = x
    while(low < high):
        partX = (low + high)//2
        partY = (x + y + 1)//2 - partX

        max_leftX = minsize if partX == 0 else ls1[partX - 1]
        min_rightX = maxsize if partX == x else ls1[partX]

        max_leftY = minsize if partY== 0 else ls2[partY - 1]
        min_rightY = maxsize if partY == x else ls2[partY]

        if max_leftX <= min_rightY and max_leftY <= min_rightX:
            if ((x + y) % 2 == 0):
                    return max(max_leftX, max_leftY) + min(min_rightX, min_rightY)/2;
            else:
                return max(max_leftX, max_leftY);
        elif max_leftX > min_rightY:
            high = partX - 1;
        else:
            low = partX + 1;

def median2(ls1, ls2):
    nums = sorted(ls1 + ls2)
    index = 0
    if len(nums) % 2 == 0:
        index = int(len(nums)/2)
        result = (nums[index - 1] + nums[index]) / 2
        return result
    else:
        index = int((len(nums) - 1)/2)
        return nums[index]


ls1 = [1, 3, 8, 9, 15]
ls2 = [7, 11, 19, 21, 18, 25]
print(median(ls1, ls2))
print(median2(ls1, ls2))
