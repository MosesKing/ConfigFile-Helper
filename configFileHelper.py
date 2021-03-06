import os


def getFiles(inputFile, outputFile):
    with open(outputFile, "w") as a:
        for path, subdirs, files in os.walk(r'{}'.format(inputFile)):
            for filename in files:
                f = os.path.join(path, filename)
                a.write('<file format='"CSV"' path="{}"/>{}'.format(str(f), os.linesep)) 

def main():

    outputFile = 'I:\ResultFiles\output.txt'
    inputFile = input("You'd like a written list of files from which directory (please put in full path): ")

    getFiles(inputFile, outputFile)

    print("List of files made")
    print("Please see the created file on YOUR ResultFile Directory! ")

    input()

if __name__ == '__main__':
    main()