import random

def check(c , p):
  if c == p:
    return 0
  if c == 1 and p == 2:
    return -1
  if c == 3 and p == 1:
    return -1
  if c == 2 and p == 3:
    return -1
  return 1
    
c = 0
a = [0,0]
while c < 3:
  c += 1
  computer = random.randint(1,3)
  player = int(input('Choose Snake / Water / Gun : ( 1 / 2 / 3: '))
  r = check(computer, player)
  if r == 0:
    print('Draw')
  elif r == 1:
    print('+1 for you')
    a[1] = a[1] + 1
  else:
    print('Comp got it')
    a[0] = a[0] + 1
if a[1] > a[0]:
  print('You won!')
else:
  print('You lose amigo!')