# Ask user to enter temprature in celsius
celsius = input("Enter temprature in celsius: ")

# convert to integer
celsius = int(celsius)

# formula
fahrenheit = (celsius * 1.8) + 32

#finally print
print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
      %(celsius, fahrenheit))
