# Day 1
# 217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        else:
            return True

# 53. Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value_of_summ, current_value_of_summ = nums[0], nums[0]
        for i in range(1, len(nums)):
            current_value_of_summ = max(current_value_of_summ + nums[i],nums[i])
            if current_value_of_summ > value_of_summ:
                value_of_summ = current_value_of_summ
        return value_of_summ

# 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

# 88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        for i in range(0, n):
            nums1[i] = nums2[i]

        return nums1

# Day 2
# 704. Binary Search
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

# 278. First Bad Version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n

        while l < r:
            m = (l + r) >> 1
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l

# 35. Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)

# 189. Rotate Array
# https://stackoverflow.com/questions/57152755/difference-between-nums-nums-1-and-nums-nums-1#:~:text=The%20assignment%20nums%20%3D%20nums%5B%3A%3A%2D1%5D
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [num**2 for num in nums]
        result.sort()
        return result

# Day 3
# 283. Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = 0
        len_list = len(nums)
        while counter < len_list:
            if nums[counter] == 0:
                nums.append(nums.pop(counter))
                len_list -= 1
            else:
                counter += 1

# 167. Two Sum II - Input Array Is Sorted
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1

        while start < end:
            check_targer = numbers[start] + numbers[end]
            if check_targer == target:
                return [start + 1, end + 1]
            elif check_targer > target:
                end -= 1
            else:
                start += 1

# 350. Intersection of Two Arrays II
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort(), nums2.sort()
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result += nums1[i],
                i += 1
                j += 1

        return result

# 121. Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_list = len(prices)
        profit = 0
        first_stock = prices[0]
        for i in range(1, len_list):
            if (first_stock > prices[i]):
                first_stock = prices[i]
            elif (prices[i] - first_stock > profit):
                profit = prices[i] - first_stock
        return profit

# Day 4
# 344. Reverse String
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

# 557. Reverse Words in a String III
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for item in s.split(' '):
            result.append(item[::-1])
        return ' '.join(result)

# 566. Reshape the Matrix
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if mat == [] or r * c != len(mat) * len(mat[0]):
            return mat

        ans = [
            [0 for j in range(c)] for i in range(r)
        ]

        k = 0
        for row in mat:
            for num in row:
                ans[k // c][k % c] = num
                k += 1
        return ans

# 118. Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows < 1:
            return result

        for i in range(0, numRows):
            row = []

            if i == 0:
                row.append(1)
            else:
                row.insert(0, 1)
                row.insert(i, 1)

                for j in range(1, i):
                    left_above = result[i - 1][j  - 1]
                    right_above = result[i - 1][j]
                    row.insert(j, left_above + right_above)

            result.append(row)

        return result

# Day 5
# 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head

        for i in range(0, n):
            if fast.next is None:
                if i == n - 1:
                    head = head.next
                return head
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        if slow.next is not None:
            slow.next = slow.next.next

        return head

# 74. Search a 2D Matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        counter = False
        for item in matrix:
            if target in item:
                counter = True
        return counter
