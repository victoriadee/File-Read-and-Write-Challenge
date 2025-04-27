# Read, process, and write file content
def process_file(input_filename, output_filename):
    try:
        # Read the input file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Count words
        words = content.split()
        word_count = len(words)

        # Convert text to uppercase
        content_upper = content.upper()

        # Prepare the final text
        final_text = content_upper + f"\n\nWord Count: {word_count}"

        # Write to the output file
        with open(output_filename, 'w') as file:
            file.write(final_text)

        print(f"Success! '{output_filename}' has been created with the processed text.")

    except FileNotFoundError:
        print("Error: The input file does not exist.")
    except IOError:
        print("Error: Problem reading or writing the files.")

# File names
input_file = 'input.txt'
output_file = 'output.txt'

# Call the function
process_file(input_file, output_file)