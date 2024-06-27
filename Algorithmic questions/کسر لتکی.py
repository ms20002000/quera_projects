def latex(start : int, n : int):
  result = ""
  if n == 1:
    result = str(start)
  else:
    result = str(start) + '+\\frac{'+ latex(2*start, n-1) + '}{' + latex(2*start + 1, n-1) + '}'
  return result


n = int(input())
start = 1
print(latex(start, n))






