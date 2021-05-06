import numpy as np

class blotto():
  def __init__(self,entry):
    self.total_wins = 0
    entry_sum = 0
    if len(entry) != 10:
      raise Exception('Entry must have 10 nonnegative integers')
    for el in entry:
      entry_sum += el
    self.entry = entry
  def clear_wins(self):
    self.total_wins = 0
  def win(self):
    self.total_wins += 1
  
def blotto_match(blotto1, blotto2):
  carriage = 1
  prev_winner = None
  blotto1_points = 0
  blotto2_points = 0
  for i in range(10):
    if carriage == 3:
      if prev_winner == blotto1:
        blotto1_points += i+1
      else:
        blotto2_points += i+1
    else:
      if blotto1.entry[i] < blotto2.entry[i]:
        blotto2_points += i+1
        if prev_winner == blotto2:
          carriage += 1
        else:
          prev_winner = blotto2
          carriage = 1
      elif blotto1.entry[i] > blotto2.entry[i]:
        blotto1_points += i+1
        if prev_winner == blotto1:
          carriage += 1
        else:
          prev_winner = blotto1
          carriage = 1
      else:
        prev_winner = None
        carriage = 0
  if blotto1_points > blotto2_points:
    blotto1.win()
  if blotto1_points < blotto2_points:
    blotto2.win()

def reinitialize_blottoes(blottoes):
  for blotto in blottoes:
    blotto.clear_wins()

def sort_blottoes(blottoes):
  if len(blottoes) > 1:
    mid = len(blottoes) // 2
    L = blottoes[:mid]
    R = blottoes[mid:]
    sort_blottoes(R)
    sort_blottoes(L)
    i = j = k = 0
    while i < len(L) and j < len(R):
      if L[i].total_wins > R[j].total_wins:
        blottoes[k] = L[i]
        i += 1
      else:
        blottoes[k] = R[j]
        j += 1
      k += 1
    while j < len(R):
      blottoes[k] = R[j]
      j += 1
      k += 1
    while i < len(L):
      blottoes[k] = L[i]
      i += 1
      k += 1

def get_random_blottoes(num):
  average = 0
  blottoes = [0 for j in range(num)]
  for i in range(num):
    x = np.random.uniform(0,1,size=10)
    blottoes[i] = blotto(np.round(100*x/np.sum(x)))
  return blottoes

def blotto_tournament(blottoes,num_output):
  if num_output > len(blottoes):
    raise Exception('num_output should be less than the length of blottoes')
  reinitialize_blottoes(blottoes)
  B = len(blottoes)
  for i in range(B):
    for j in range(i,B):
      blotto_match(blottoes[i],blottoes[j])
  sort_blottoes(blottoes)
  return blottoes[:num_output]

def generate_evolved_blottoes(blottoes):
  new_blottoes = [0 for j in range(len(blottoes))]
  B = len(blottoes)
  for i in range(B):
    x = np.random.uniform(-1,1,size=10)
    while np.sum(np.round(x)) != 0 or np.any(np.array(blottoes[i].entry)+np.round(x)<0):
      x = np.random.uniform(0,1,size=10)
    new_blottoes[i] = blotto(blottoes[i].entry + np.round(x))
  return new_blottoes

NUM_RANDOM = 100
NUM_EVOLVED = 100
ITERS = 10000
blottoes = get_random_blottoes(2*NUM_EVOLVED+NUM_RANDOM)
for k in range(ITERS):
  x = blotto_tournament(blottoes, NUM_EVOLVED)
  blottoes = x + generate_evolved_blottoes(x) + get_random_blottoes(NUM_RANDOM)
  print(blottoes[0].entry)