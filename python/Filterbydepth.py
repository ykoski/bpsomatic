import sys
import argparse
import os

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

    writemut = True
    with open(args.input,'r') as ifile, open(args.output,'w') as ofile:
        for line in ifile:
            if line[0] != '#':
                line = line.split('\t')
                stats=line[9].split(':')
                ad = stats[1].split(',')
                ad = [int(x) for x in ad]
                depth = sum(ad)
                if depth < 100:
                    writemut = False
                for i in ad[1:]:
                    if i >= 7:
                        writemut = True
                        break
                    else:
                        writemut = False
                if writemut:
                    ofile.write('\t'.join(line))
                writemut = True
            else:
                ofile.write(line)

main()
