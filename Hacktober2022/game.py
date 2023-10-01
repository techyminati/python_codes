import random 

def game1():
  print('Welcome to the game. Please follow the instructions carefully')
  print('Enter lower and upper limit. Both are inclusive')
  print('\nYou have 6 tries to guess the number')

  lower_limit = int(input('Enter lower limit : '))
  upper_limit = int(input('Enter upper limit : '))

  if upper_limit < lower_limit:
      print('Entered limits are not correct')
      upper_limit = int(input('Enter upper limit : '))
      lower_limit = int(input('Enter lower limit : '))

  if upper_limit - lower_limit < 7:
      print('Differnce between limits should be more than 6')
      lower_limit = int(input('Enter lower limit : '))
      upper_limit = int(input('Enter upper limit : '))
          
  ans  = random.randrange(lower_limit,upper_limit+1)
  
  for i in range(6):
      user_input = int(input('Guess the number : '))
      if user_input < ans :
          print('The number is greater than your guess')
      elif user_input > ans :
          print('The number is smaller than your guess')
      else:
          print('you have guessed in',(i+1),'tries')
          print('you have guessed the number correctly')  
          break
  else:
    print("You couldn't guess the number correctly. ")
    print('Number was', ans)

game1()
