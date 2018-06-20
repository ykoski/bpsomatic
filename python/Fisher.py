import sys
import math
import argparse
import os.path

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", dest = "input", help="This program takes one vcf file as an input")
parser.add_argument("-o", "--output", dest = "output", help="File to output.")

args = parser.parse_args()

def main():

    CheckArguments(args)
    with open(args.input,'r') as ifile, open(args.output,'w') as ofile:
        for line in ifile:
            if line[0] != '#':
                line = line.split('\t')
                tumor = line[9]
                normal = line[10]
                # Let's modify variables tumor and normal to be lists where first element is variant
                # reads and second element is reference reads
                tumor = tumor.split(':')[1]
                tumor = tumor.split(',')
                tumor = [int(x) for x in tumor]
                normal = normal.split(':')[1]
                normal = normal.split(',')
                normal = [int(x) for x in normal]
                for i in range(1,len(tumor)):
                    tumor_count = [tumor[i],tumor[0]]
                    normal_count = [normal[i],normal[0]]
                    somaticp = Fisher(tumor_count,normal_count)
                    print(somaticp)
                    line[7] = line[7]+";Somaticp=%.5g" % somaticp
                ofile.write('\t'.join(line))
            else:
                ofile.write(line)

def CheckArguments(args):
    if args.input == None or args.output == None:
        print("Error! Input or output argument is missing. Exiting...")
        exit()
    elif os.path.isfile(args.input) == False:
        print("Error! Input file doesn't exist. Exiting...")
        exit()


def Fisher(tum,nor):
    pvalue = Loghypergeom(tum,nor)
    while nor[0] > 0:
        nor, tum = Adjust(nor,tum)
        pvalue += Loghypergeom(tum,nor)
    return pvalue

def Adjust(a,b):
    a[0] -= 1
    a[1] += 1
    b[0] += 1
    b[1] -= 1
    return (a, b)

def Loghypergeom(tum,nor):
    a = tum[0]
    c = tum[1]
    b = nor[0]
    d = nor[1]
    n = a+b+c+d
    if a>=0 and b>=0 and c >= 0 and d >= 0:
        pval = (math.log(math.factorial(a+b)) + math.log(math.factorial(c+d)) + math.log(math.factorial(a+c)) + math.log(math.factorial(b+d))) - \
        (math.log(math.factorial(a)) + math.log(math.factorial(b)) + math.log(math.factorial(c)) + math.log(math.factorial(d)) + math.log(math.factorial(n)))
    else:
        pval = 0
    return math.exp(pval)

if __name__ == "__main__":
    #sys.exit(main(sys.argv))
    main()
