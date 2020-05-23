# Bubble sort
class Solution:
    def bubble_sort(self, arr):
        is_sorted = False
        length = len(arr) - 1
        while not is_sorted:
            is_sorted = True
            for i in range(length):
                if arr[i] > arr[i+1]:
                    # swap the values
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    is_sorted = False
            length -= 1


s = Solution()
arr = [12, 11, 13, 5, 6, 7]
s.bubble_sort(arr)
print(arr)
