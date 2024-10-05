def temperature_conversion(value, from_unit, to_unit):
    # Convert from the original unit to Celsius
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid from_unit provided. Use 'celsius', 'fahrenheit', or 'kelvin'.")

    # Convert from Celsius to the desired unit
    if to_unit == 'celsius':
        converted_value = celsius
    elif to_unit == 'fahrenheit':
        converted_value = (celsius * 9/5) + 32
    elif to_unit == 'kelvin':
        converted_value = celsius + 273.15
    else:
        raise ValueError("Invalid to_unit provided. Use 'celsius', 'fahrenheit', or 'kelvin'.")

    return converted_value

# Example usage
if __name__ == "__main__":
    try:
        temperature = float(input("Enter the temperature: "))
        from_unit = input("Convert from (celsius, fahrenheit, kelvin): ").lower()
        to_unit = input("Convert to (celsius, fahrenheit, kelvin): ").lower()

        converted_temperature = temperature_conversion(temperature, from_unit, to_unit)
        print(f"{temperature} {from_unit.capitalize()} is equal to {converted_temperature:.2f} {to_unit.capitalize()}.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)