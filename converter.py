def binary_to_decimal(binary):
  decimal = 0
  binary = binary[::-1] 
  for i, digit in enumerate(binary):
    if digit == '1':
      decimal += 2**i
  return decimal

def decimal_to_binary(decimal):
  binary = ''
  while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
  return binary

def main():
  while True:
    print("Enter 'b' for binary to decimal conversion, 'd' for decimal to binary conversion, or 'q' to quit:")
    conversion_type = input()

    if conversion_type == 'b':
      print("Enter a binary number:")
      binary = input()
      decimal = binary_to_decimal(binary)
      print(f"The decimal equivalent is {decimal}")
    elif conversion_type == 'd':
      print("Enter a decimal number:")
      decimal = int(input())
      binary = decimal_to_binary(decimal)
      print(f"The binary equivalent is {binary}")
    elif conversion_type == 'q':
      break  # Exit the loop and end the program
    else:
      print("Invalid input. Please try again.")

if __name__ == "__main__":
  main()
