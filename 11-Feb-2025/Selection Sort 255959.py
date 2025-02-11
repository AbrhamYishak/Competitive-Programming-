# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min_ind = i
            for j in range(i+1,n):
                if arr[j] < arr[min_ind]:
                    min_ind = j
            arr[min_ind],arr[i] = arr[i],arr[min_ind]
        return arr