filename_input = "input.txt"
filename_output = "ping1.txt"

with open(filename_input, "r") as file_input:
    data = file_input.read()  # Read input data from file

lines = data.split("\n")  # Split data into lines

filtered_lines = [line for line in lines if "HTTP/1.1 200 OK -- Server: cloudflare" in line]  # Filter lines

filtered_data = "\n".join(filtered_lines)  # Join lines back into a string

with open(filename_output, "w") as file_output:
    file_output.write(filtered_data)  # Save the filtered data to file

#print("Data has been filtered and saved to", filename_output)