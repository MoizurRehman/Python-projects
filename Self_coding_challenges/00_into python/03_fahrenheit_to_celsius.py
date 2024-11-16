def main():
    tem_in_fahrenheit = float(input("Enter a temperature in fahrenheit "))
    degrees_celsius = (tem_in_fahrenheit - 32) * 5.0/9.0
    print(degrees_celsius)

main()