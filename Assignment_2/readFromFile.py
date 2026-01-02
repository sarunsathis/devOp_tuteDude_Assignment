import writeToFile as wtf

def readFromFile(filePath):
    with open(filePath, 'r') as file:
        content = file.read()
    return content

if __name__ == "__main__":
    filePath = "Assignment_2/results/" + input("Enter file name of the result to be read: ")
    try:
        fileContent = "readFromFile Result from File: " + filePath + "\n\n"
        fileContent += readFromFile(filePath) + "\n\nFile read successfully."
        wtf.writeto_file("readFromFile.txt", fileContent)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")