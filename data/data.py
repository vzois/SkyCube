import sys
import argparse
import time
from subprocess import call


def script(N=2048,D=2,distr='i'):
     filename = "d_"+str(N)+"_"+str(D)+"_"+distr
     f = open(filename, "w")
     arg_call = ["./randdataset", "-"+distr,"-n",str(N),"-d",str(D),"-s",str(int(time.time()))]
     print arg_call
     call(arg_call,stdout=f)
     f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Optional Arguments')
    parser.add_argument("-n",dest='n',default=2048,type=int,help="cardinality > 0, default:2048")
    parser.add_argument("-d",dest='d',default=2,type=int,help="dimensionality > 0, default:2")
    parser.add_argument("-distr",dest='distr',default='i',type=str,help="dimensionality > 0, (c)orrelated, (i)ndependent, (a)nticorrelated,default:i")
    args = parser.parse_args()
    
    if args.n <=0:
        print "Cardinality has to be > 0 !!!"
        exit(1)
    if args.d <=0:
        print "Dimensionality has to be > 0 !!!"
        exit(1)
    if args.distr !='c' and args.distr !='i' and args.distr !='a':
        print "Distribution has to be (c)orrelated, (i)ndependent, (a)nticorrelated!!!"
        exit(1)
    
    script(N=args.n,D=args.d,distr=args.distr)


