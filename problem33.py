#!/usr/bin/python
#
# Project Euler -- Problem 33

def ones(n):
    return n % 10

def tens(n):
    n /= 10
    return n % 10

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


def lowest_terms(frac):
    divisor = gcd(frac[0], frac[1])
    return [n/divisor for n in frac]

def product(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    return[numerator, denominator]

def equals(frac1, frac2):
    return (frac1[0]*frac2[1]) == (frac1[1]*frac2[0])

if __name__ == "__main__":
    frac_list = []
    for numerator in range (11, 100):
        for denominator in range(11, 100):
            if (numerator != denominator):
                if ones(numerator) == tens(denominator):
                    print "Working on {0}/{1}".format(numerator, denominator)
                    frac = [numerator, denominator]
                    simplified = [tens(numerator), ones(denominator)]
                    print "frac {0}    simp {1}".format(frac, simplified)
                    if equals(frac, simplified):
                        print "\tGOT IT!!"
                        frac_list.append(simplified)
    print "frac list is {0}".format(frac_list)
    my_product = reduce(product, frac_list)
    print "product is {0}".format(my_product)
    answer = lowest_terms(product)
    print "Answer is {0}".format(answer)

