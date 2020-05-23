# Counting Sort
class Solution:
    def sort_array(self, arr):
        pos_arr = []
        neg_arr = []
        min_val = min(arr)
        max_val = max(arr)
        pos_idx = [0] * (max_val + 1)
        if min_val < 0:
            for num in arr:
                if num < 0:
                    neg_arr.append(num)
                else:
                    pos_arr.append(num)
            neg_idx = [0] * (abs(min_val)+1)
            ans = self.counting_sort(neg_arr, neg_idx) + self.counting_sort(pos_arr, pos_idx)
        else:
            ans = self.counting_sort(arr, pos_idx)
        return ans

    def counting_sort(self, arr, idx):
        for i in arr:
            idx[i] += 1

        j = 1
        while j < len(idx):
            idx[j] = idx[j-1] + idx[j]
            j += 1

        ans = [0] * (len(arr)+1)
        for num in arr:
            ans[idx[num]] = num
            idx[num] -= 1
        return ans[1:]


s = Solution()
arr = [12, 7, 11, -2, 13, 5, 0, 6, -7]
print(s.sort_array(arr))
