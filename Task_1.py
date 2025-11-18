

try:
    fh = open('sample.txt', 'rt')
    count=0
    print("Reading file content:")
    for i in fh.readlines():
        count+=1
        print(f"Line {count}: {i.rstrip("\n")}")
except:
    print("Error: The file 'sample.txt' was not found.")

