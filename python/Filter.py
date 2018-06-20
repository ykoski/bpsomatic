import sys
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", dest = "input", help="This program takes one vcf file as an input")
parser.add_argument("-o", "--output", dest = "output", help="File to output.")

args = parser.parse_args()

def main():

    if args.input == None or args.output == None:
        print("Error! Input or output argument is missing. Exiting...")
        exit()
    elif os.path.isfile(args.input) == False:
        print("Error! Input file doesn't exist. Exiting...")
        exit()

    counter = 0
    with open(args.input,'r') as ifile, open(args.output,'w') as ofile:
        for line in ifile:
            counter += 1
            if line[0] != '#':
                if 'PASS' in line:
                    ofile.write(line)
                else:
                    pass
            else:
                ofile.write(line)
        print("Number of lines read:"+str(counter))

if __name__ == "__main__":
    # sys.exit(main(sys.argv))
    exit()
