import glob

filenames = glob.glob("files/*.txt")

description = ""

for filename in filenames:
    with open(filename,'r') as file:
        description += file.read()

with open("merged_text.txt","w") as file:
    file.write(description)