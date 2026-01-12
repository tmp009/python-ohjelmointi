MIN_LEN = 42

length = float(input("Enter the length of the zander in centimeters: "))

if length < MIN_LEN:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {abs(length - MIN_LEN):.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")
