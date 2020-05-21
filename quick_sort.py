# Quick Sort
class Solution:
    def quick_sort(self, arr, low, high):
        if low < high:
            j = self.partition(arr, low, high)
            self.quick_sort(arr, low, j)
            self.quick_sort(arr, j+1, high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high
        while True:
            while arr[i] < pivot:
                i += 1
                if i == high:
                    break
            while arr[j] >= pivot:
                j -= 1
                if j == low:
                    break
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                arr[low], arr[j] = arr[j], arr[low]
                break
        return j


s = Solution()
arr = [12, 7, 11, 13, 5, 6, 7]
print(s.quick_sort(arr, 0, len(arr)-1))
