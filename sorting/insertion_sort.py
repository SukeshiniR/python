# Insertion Sort
class Solution:
    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            curr = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > curr:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = curr
        return arr


s = Solution()
print(s.insertion_sort([12, 6, 3, 23, 1, 6]))
