def factors(n):
  for val in range(1, n+1):
      if n % val == 0:
          yield val
fact = factors(10)
print(next(fact))
print(next(fact))

# print(factors(20))

# factors_of_20 = factors(20)
# print(next(factors_of_20))
