class Solution(object):

    def getRange(self, arr, x):
        # first = self.binarySearchIterative(arr, 0, len(arr)-1, x, True )
        # last = self.binarySearchIterative(arr, 0, len(arr)-1, x, False)

        first = self.binarySearchRecursive(arr, 0, len(arr)-1, x, True)
        last = self.binarySearchRecursive(arr, 0, len(arr)-1, x, False)

        return [first, last]


    def binarySearchRecursive(self, arr, low, high, x, findFirst):
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
                return mid
            if x > arr[mid]:
                return self.binarySearchRecursive(arr, mid + 1, high, x, findFirst)
            else:
                return self.binarySearchRecursive(arr, low, mid-1, x, findFirst)
        else:
            if (mid == len(arr)-1 or x < arr[mid+1]) and arr[mid] == x:
                    return mid 
            if x < arr[mid]:
                return self.binarySearchRecursive(arr, low, mid-1, x, findFirst)
            else:
                return self.binarySearchRecursive(arr, mid + 1, high, x, findFirst)



    def binarySearchIterative(self, arr, low, high, x, findFirst):
        while True:
            if high < low:
                return -1
            mid = low + (high - low) // 2
            if findFirst:
                if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
                    return mid
                if x > arr[mid]:
                    low = mid + 1 
                else:
                    high = mid - 1
            else:
                if (mid == len(arr)-1 or x < arr[mid+1]) and arr[mid] == x:
                    return mid 
                if x < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1




arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
x = 9
print(Solution().getRange(arr, 9))
# [6, 8]