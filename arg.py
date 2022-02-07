import numpy as np
import argparse

################################
# define a function, a simple mean here
def readCommands():
  '''
  Read commandline arguments
  '''
  p = argparse.ArgumentParser(description=("An illustration of a command line parser"))
  p.add_argument("--numb", dest ="numb", type=int, default=10, help=("Lenght of array to generate\nDefault = 10"))
  cmdargs = p.parse_args()
  return cmdargs

def getMean(x):
  mean=np.mean(x)
  return(mean)


################################
# the main block

if __name__ == '__main__':
  # create some data
    com=readCommands()
    data=np.random.rand(com.numb)
  # call our function
    meanX=getMean(data)
    print("Mean is",meanX)