#
#
# Regression and Classification programming exercises
#

#	In this exercise we will be taking a small data set and computing a linear function
#	that fits it, by hand.
#	

#	the data set

import numpy as np

sleep =  [5, 6, 7, 8, 10]
scores = [65,51,75,75,86]


def compute_regression(sleep,scores):

    #	First, compute the average amount of each list

    avg_sleep = np.average(sleep)
    avg_scores = np.average(scores)

    #	Then normalize the lists by subtracting the mean value from each entry

    normalized_sleep = map(lambda x: x - avg_sleep, sleep)
    normalized_scores = map(lambda x: x - avg_scores, scores)

    #	Compute the slope of the line by taking the sum over each student
    #	of the product of their normalized sleep times their normalized test score.
    #	Then divide this by the sum of squares of the normalized sleep times.

    product = []
    for x, y in zip(normalized_sleep, normalized_scores):
        product.append(x * y)
    slope = np.sum(product)
    slope = slope / np.sum(map(lambda x: x ** 2, normalized_sleep))

    #	Finally, We have a linear function of the form
    #	y - avg_y = slope * ( x - avg_x )
    #	Rewrite this function in the form
    #	y = m * x + b
    #	Then return the values m, b
    m = slope
    b = slope * (-avg_sleep) + avg_scores
    
    print ("m:{} \nb:{}").format(m, b)
    return m,b


if __name__=="__main__":
    m,b = compute_regression(sleep,scores)
    print "Your linear model is y={}*x+{}".format(m,b)
