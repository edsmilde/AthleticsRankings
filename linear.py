import numpy
import csv


    

def getCoefficients(X, Y):
    Xt = numpy.transpose(X)
    XtX = numpy.matmul(Xt, X)
    XtY = numpy.matmul(Xt,Y)
    theta = numpy.linalg.lstsq(XtX, XtY, rcond=None)
    return theta


def getCoefficientsAddNormalization(X, Y):
    xHeight = len(X)
    xNormalization = numpy.ones((xHeight, 1))
    xNormalized = numpy.hstack((xNormalization, X))
    return getCoefficients(xNormalized, Y)

