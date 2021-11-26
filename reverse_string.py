#reverse strng 

# 1.using swap
def reverse_v1(self, strs: str):
    post_idx = len(strs) - 1
    pre_idx = 0

    while post_idx - pre_idx > 0:
        temp = strs[post_idx]
        strs[post_idx] = strs[pre_idx]
        strs[pre_idx] = temp

        post_idx = post_idx - 1
        pre_idx = pre_idx + 1

# 2.using swap
def reverse_v2(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left <right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 3.pythonic way solution
def reverse_pythonnic_way(self, s: List[str]) -> None:
    s.reverse()
