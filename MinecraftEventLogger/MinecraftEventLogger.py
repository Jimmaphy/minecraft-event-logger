# Import the required libraries
import argparse

# Get the filepath from the command line
parser = argparse.ArgumentParser(description='Process a mathematical expression')
parser.add_argument("file", help="Enter the path to the file")
file = parser.parse_args().file

# Prepare for the data
data = []

# Open the file with reading permissions
with open(file, 'r') as file:
    # Read the file line by line
    for line in file:
        # Check whether the line is a finished message that came from the server
        if '[System]' in line and 'het parkour af' in line:
            # Get only the message part
            message = line.split('[CHAT]')[1].removeprefix(' ')
            
            # Split the message into part
            parts = message.split(' ')

            # Select the third, fourth and sixth part of the message
            data.append([parts[2], parts[3], parts[5]])

# Create a new file with writing permissions to store the data in as csv
with open('data.csv', 'w') as file:
    # Write the header
    file.write('Name,Time,Deaths\n')
    
    # Read all the data
    for line in data:
        # Write the data to the file
        file.write(f'{line[0]},{line[1]},{line[2]}\n')