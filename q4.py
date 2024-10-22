import re

def is_valid_number_plate(plate):
    """Check if the vehicle number plate is valid based on Indian format."""
    
    pattern = r'^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$'
    

    if re.match(pattern, plate):
        return True
    else:
        return False

def main():
    print("Welcome to the Indian Vehicle Number Plate") 
    plate_number = input("Enter the vehicle number plate (format: XX NN YY)
    if is_valid_number_plate(plate_number):
        print("The number plate is valid.")
    else:
        print("The number plate is invalid. Please follow the format 'XX NN YY NNNN'.")


if __name__ == "__main__":
    main()
