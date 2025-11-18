
text = input("Enter text to write to the file: ")
fh = open("output.txt", "wt")
fh.write(f"{text.strip()}\n")
fh.close()

print("Data successfully written to output.txt.")

additionalText = input("Enter additional text to append: ")
fh2=open("output.txt", "at")
fh2.write(additionalText.strip())
fh2.close()

print("Data successfully appended.")

fh3=open("output.txt", "rt")
print("Final content of output.txt:")
for i in fh3.readlines():
    print(i.rstrip("\n"))
