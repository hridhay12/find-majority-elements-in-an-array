class Solution:
    def majorityElement(self, arr):
        n=len(arr)
        count = 0
        candidate = -1  # Initialize candidate to -1, which is not a valid element in the array

        # Phase 1: Finding a potential candidate
        for num in arr:
            if count == 0:
                candidate = num
                count = 1  # When a new candidate is chosen, its count starts at 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Phase 2: Verifying the candidate (necessary because the first phase only guarantees
        # that if a majority element exists, it will be the candidate found)
        count = 0
        for num in arr:
            if num == candidate:
                count += 1
        if count > n // 2:
            return candidate
        else:
            return -1 # If no majority element found or array was empty
if __name__ == "__main__":
    # Example usage
    sol = Solution()
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    result = sol.majorityElement(arr)
    if result != -1:
        print(f"The majority element is: {result}")
    else:
        print("No majority element found.")     