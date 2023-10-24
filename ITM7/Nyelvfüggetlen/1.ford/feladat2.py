import collections

Dino = collections.namedtuple("Dino", "weight length")

def solve(dinos:list):
  dinos.sort(key = lambda dino: dino.weight)
  result = 0
  maxLength = 0 
  iOther = len(dinos)-1
  for i in range(len(dinos)-1, -1, -1):
    dino = dinos[i]
    while dinos[iOther].weight > dino.weight:
      maxLength = max(maxLength, dinos[iOther].length)
      iOther -= 1
    if maxLength <= dino.length:
      result += 1
  return result

# A lassú megoldás.
def solveBruteForce(dinos:list):
  result = 0
  for i in range(len(dinos)):
    strong = True
    for j in range(len(dinos)):
      if j == i:
        continue
      if dinos[j].weight > dinos[i].weight and dinos[j].length > dinos[i].length:
        strong = False
        break
    if strong:
      result += 1
  return result

def solveFile(fn:str, fOut):
  dinos = []
  with open(fn) as f:
    for line in f:
      weight, length = map(int, line.strip().split())
      assert weight >= 1
      assert length >= 1
      dinos.append(Dino(weight, length))
  assert dinos
  
  result = solve(dinos)

  message = "Output for %s: %s" % (fn, result)
  print(message)
  fOut.write(message+"\n")

  if "pelda" in fn:
    fnPeldaOut = fn.replace(".in.", ".out.")
    assert fnPeldaOut != fn
    with open(fnPeldaOut, "w") as fPeldaOut:
      fPeldaOut.write(str(result))

def main():
  problemName = "dino"
  with open("out.txt", "w") as fOut:
    for i in range(1, 6):
      solveFile(problemName + "%s.in.txt" % (i,), fOut)
    for i in range(1, 3):
      solveFile(problemName + ".pelda%s.in.txt" % (i,), fOut)

if __name__ == "__main__":
  main()
