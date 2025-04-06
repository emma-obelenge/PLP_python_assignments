userInput = f"{input('Enter file name: ')}.txt"

try:
    with open(userInput, "r") as readFile:
        fileContent = readFile.readlines()

    modified_content = [line.upper() for line in fileContent]
    output_file = "modified_" + userInput

    with open(output_file, 'w') as newFile:
         newFile.writelines(modified_content)
    print(f"Modified content successfully written to: {output_file}")
         
except FileNotFoundError:
    print("Error: File doesn't exist or can't be read!")

finally:
    print("Thank you for using this program!")