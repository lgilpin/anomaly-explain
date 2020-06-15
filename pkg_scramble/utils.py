import logging
import numpy as np
import argparse

"""
Perform the binomial distribution (return a 0 or 1)
"""
def coinFlip(p):    
    result = np.random.binomial(1,p)
    return result

def scrambleFlags(n, p):
    flags = np.arange(n)
    #perform desired numbered of flips at required probability set above
    for i in range(0, n):    
        flags[i] = coinFlip(p)    
        i+=1
        
    #Results
    logging.debug('probability is set to {:f}'.format(p))
    logging.debug(flags)

    reasonable_count = np.count_nonzero(flags == 1)
    unreasonable_count = np.count_nonzero(flags == 0)

    #Total up heads and tails for easy user experience 
    logging.debug('Reasonable Count: {:d}'.format(reasonable_count))
    logging.debug('Uneasonable Count: {:d}'.format(unreasonable_count))

    logging.debug('Reasonable Percentage: {:f}'.format(reasonable_count/n))
    logging.debug('Unreasonable Percentage: {:f}'.format(unreasonable_count/n))    

    return flags

def chooseNewLabel(old_label, labels, probs):
    """
    Chooses a new label based on a distribution multi-class distribution
    labels are a dictionary of the label name and the probability
    """
    choice = np.random.choice(labels, p=probs)
    while choice == old_label:
        choice = np.random.choice(labels, p=probs)
    return choice

def printDistribution(p, flags):
    print('probability is set to {:f}'.format(p))
    print(flags)

    reasonable_count = np.count_nonzero(flags == 1)
    unreasonable_count = np.count_nonzero(flags == 0)

    #Total up heads and tails for easy user experience 
    print('Reasonable Count: {:d}'.format(reasonable_count))
    print('Uneasonable Count: {:d}'.format(unreasonable_count))

    print('Reasonable Percentage: {:f}'.format(reasonable_count/n))
    print('Unreasonable Percentage: {:f}'.format(unreasonable_count/n))
    

def main():
    """
    Verbose shows the dataset distributions etc. 
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action='store_true', 
                        help='This is the same as debug right now')
    parser.add_argument("-n", "--number", help="The number of items toscramble",
                        type=int, default=10)
    parser.add_argument("-p", "--probability", 
                        help="The probability for the binomial distribution",
                        type=float, default=.5)
    args = parser.parse_args()
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s: %(message)s')

    # Logging info for verbose and other debugging
    logging.info("Verbose output.")

    scrambleFlags(args.number, args.probability)

if __name__ == "__main__":
    # execute only if run as a script
    main()
