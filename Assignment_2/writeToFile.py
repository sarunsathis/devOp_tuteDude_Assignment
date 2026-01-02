def writeto_file(filename, content):
    try:
        with open("Assignment_2/results/" + filename, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    filename = input("Enter the filename to write to: ")
    content = input("Enter the content to write to the file: ")
    writeto_file(filename, content)