import re

filename_input = "ping1.txt"
filename_output = "ping2.txt"

with open(filename_input, "r") as file_input:
    data = file_input.read()  # Read input data from file

lines = data.split("\n")  # Split data into lines

filtered_lines2 = [re.sub(r"HTTP/1\.1 200 OK -- Server: cloudflare", "", line) for line in lines]  # Remove the code
filtered_lines = [re.sub(r":443", "", line2) for line2 in filtered_lines2]  # Remove the code

filtered_data = "\n".join(filtered_lines)  # Join lines back into a string

with open(filename_output, "w") as file_output:
    file_output.write(filtered_data)  # Save the filtered data to file

#print("Data has been filtered and saved to", filename_output)