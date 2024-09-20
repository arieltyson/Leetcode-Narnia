'''
My solution begins from line 50 so if you want to take a fair try at the code, 
copy the function signature : 
  def subtract_lists(A: List[int], B: List[int]) -> List[int]:
And give it a go by pasting over this file. If you run into problems,
the solution can be found at the GitHub link to the problem. Good luck !
'''
















































from collections import deque

def subtract_lists(A: List[int], B: List[int]) -> List[int]:
    def is_A_smaller(A, B):
        if len(A) != len(B):
            return len(A) < len(B)
        return A < B

    A = A[::-1]
    B = B[::-1]
    
    len_diff = len(A) - len(B)
    if len_diff > 0:
        B += [0] * len_diff
    elif len_diff < 0:
        A += [0] * (-len_diff)
    
    is_negative = False
    if is_A_smaller(A[::-1], B[::-1]):
        A, B = B, A
        is_negative = True

    result = deque()
    borrow = 0

    for i in range(len(A)):
        diff = A[i] - B[i] - borrow
        
        if diff < 0:
            diff += 10
            borrow = 1
            j = i + 1
            while A[j] == 0:
                A[j] = 9
                j += 1
            A[j] -= 1
        else:
            borrow = 0

        result.appendleft(diff)

    while len(result) > 1 and result[0] == 0:
        result.popleft()

    final_result = list(result)

    if is_negative:
        final_result[0] = -final_result[0]

    return final_result
