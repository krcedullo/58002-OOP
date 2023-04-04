class TempConversion:
    def __init__(self, temp, temp_type):
        self.__temp = temp
        self.__temp_type = temp_type

    def celsius_to_fahrenheit(self):
        return (self.__temp * 1.8) + 32

    def kelvin_to_celsius(self):
        return self.__temp - 273.15

    def celsius_to_kelvin(self):
        return self.__temp + 273.15

    def fahrenheit_to_celsius(self):
        return (self.__temp - 32) / 1.8

    def kelvin_to_fahrenheit(self):
        return (self.__temp - 273.15) * 1.8 + 32

    def fahrenheit_to_kelvin(self):
        return self.celsius_to_kelvin(self.fahrenheit_to_celsius())


temp_type = input("Enter the temperature type (C, K, or F): ")
temp = float(input("Enter the temperature value: "))

temp_conv = TempConversion(temp, temp_type.upper())

if temp_conv._TempConversion__temp_type == "C":
    print(f"{temp_conv.celsius_to_fahrenheit()}F")
    print(f"{temp_conv.celsius_to_kelvin()}K")
elif temp_conv._TempConversion__temp_type == "K":
    print(f"{temp_conv.kelvin_to_celsius()}C")
    print(f"{temp_conv.kelvin_to_fahrenheit()}F")
elif temp_conv._TempConversion__temp_type == "F":
    print(f"{temp_conv.fahrenheit_to_celsius()}C")
    print(f"{temp_conv.fahrenheit_to_kelvin()}K")
else:
    print("Invalid temperature type")
