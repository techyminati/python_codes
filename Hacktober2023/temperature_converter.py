''' Program to convert between temperatures in Fahrenheit and Celsius '''

def convert_celsius(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

def convert_fahrenheit(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print(f"Please enter the temperature's input type of either Fahrenheit (F) or Celsius (C).\n")
    temperature_type = input("Will this temperature be in Fahrenheit (F) or Celsius (C)? ")

    if temperature_type == 'C' or temperature_type == 'c':
        temperature_input = float(input("Enter temperature in Celsius: "))
        temperature_output = convert_celsius(temperature_input)
        print(f"{temperature_input} degrees in Celsius is equal to {temperature_output} degrees in Fahrenheit.")
    elif temperature_type == 'F' or temperature_type == 'f':
        temperature_input = float(input("Enter temperature in Fahrenheit: "))
        temperature_output = convert_fahrenheit(temperature_input)
        print(f"{temperature_input} degrees in Fahrenheit is equal to {temperature_output} degrees in Celsius.")
    else:
        print('\nPlease try again and enter a valid input of F, C, f, or c.')

if __name__ == "__main__":
    main()
