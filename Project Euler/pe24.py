def permutation_debut(str):
  permutation("", str)

def permutation(prefix, str, iter=1):
  if iter == 100000:
    return str
  n =len(str)
  if n == 0:
    #print(prefix)
    iter += 1
  else:
    for i in range(n):
      iter += 1
      permutation(prefix + str[i], str[:i] + str[i+1:n], iter)

res = permutation_debut("0123456789")
print(res)