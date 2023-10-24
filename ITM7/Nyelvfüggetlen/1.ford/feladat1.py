def solve(n):
  assert n
  x = 1
  while x <= n:
    x *= 2
  return x - 1

# A lassú megoldás.
def solveBruteForce(n):
  result = 0
  for i in range(1, n+1):
    result |= i
  return result

# teszt
for i in range(1, 100):
  assert solve(i) == solveBruteForce(i)
  
def solveFile(fn:str, fOut):
  with open(fn) as f:
    n = int(f.readline().strip())
  assert n
  
  result = solve(n)

  message = "Output for %s: %s" % (fn, result)
  print(message)
  fOut.write(message+"\n")

  if "pelda" in fn:
    fnPeldaOut = fn.replace(".in.", ".out.")
    assert fnPeldaOut != fn
    with open(fnPeldaOut, "w") as fPeldaOut:
      fPeldaOut.write(str(result))

def main():
  problemName = "vagy"
  with open("out.txt", "w") as fOut:
    for i in range(1, 6):
      solveFile(problemName + "%s.in.txt" % (i,), fOut)
    for i in range(1, 3):
      solveFile(problemName + ".pelda%s.in.txt" % (i,), fOut)

if __name__ == "__main__":
  main()
