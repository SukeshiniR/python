# Selection Sort
class Solution:
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


s = Solution()
arr = [12, 7, 11, 13, 5, 6, 7]
print(s.selection_sort(arr))
