class Solution:
    def bucket_sort(self, arr):
        maxval = max(arr)
        dict_size = maxval // 10
        bucks = {}
        for i in range(dict_size+1):
            bucks[i] = []
        for num in arr:
            tmp = str(num)
            l = int(len(tmp[:-1]))
            if l > 1:
                (bucks[int(tmp[:-1])]).append(num)
            else:
                (bucks[0]).append(num)
        ans = []
        for k,v in bucks.items():
            if len(v) > 1:
                ans += self.bubble_sort(v)
            if len(v) == 1:
                ans += v
        return ans

    def bubble_sort(self, arr):
        is_sorted = False
        length = len(arr) - 1
        while not is_sorted:
            is_sorted = True
            for i in range(length):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    is_sorted = False
            length -= 1
        return arr


s = Solution()
arr = [120, 7, 11, 32, 13, 0, 5, 100, 46, 7]
print(s.bucket_sort(arr))
