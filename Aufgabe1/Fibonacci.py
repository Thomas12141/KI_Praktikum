def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum13(nums):
  if len(nums)==0:
    return 0
  c = 0
  i = 0
  while i < len(nums):
    if i == len(nums)-1 and nums[i] == 13:
      break
    if nums[i] == 13:
      i+=2
      continue
    c += nums[i]
    i+=1
  return c


print(sum13([1, 2, 13, 2, 1, 13]))
