def celsius_to_farenheit(temp):
    farenheit = (temp * 1.8) + 32

    return farenheit

def farenheit_to_celsius(temp):
    celsius = (temp - 32) / 1.8

    return celsius

print(f"35 degrees celsius converted to farenheit is: {celsius_to_farenheit(35)} degrees farenheit.")

print(f"95 degrees farenheit converted to celsius is: {farenheit_to_celsius(95)} degrees celsius.")