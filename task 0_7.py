# This function converts a Celsius temperature reading and returns the temperature in Farenheit
def celsius_to_farenheit(temp):
    farenheit = (temp * 1.8) + 32

    return farenheit

# This function converts a Farenheit temperature reading and returns the temperature in Celsius
def farenheit_to_celsius(temp):
    celsius = (temp - 32) / 1.8

    return celsius

print("Enter either 1 or 2 to choose from the below options")
print("1.       - Celsius to Farenheit Converter")
print("2.       - Farenheit to Celsius Converter")
option = int(input(""))

if (option != 1) and (option != 2):
    print("You have entered an invalid option.")
    print("Program exiting.")
else:
    if option == 1:
        celsius = int(input("Enter temperature in Celsius: "))
        print(f"{celsius} degrees celsius converted to farenheit is: {round(celsius_to_farenheit(celsius), 1)} degrees farenheit.")
    else:
        farenheit = int(input("Enter a temperature in Farenheit: "))
        print(f"{farenheit} degrees farenheit converted to celsius is: {round(farenheit_to_celsius(farenheit), 1)} degrees celsius.")