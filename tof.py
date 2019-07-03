#!/usr/bin/python3


###########################################
# module: tof.py
# Rigoberto Tellez
# A02169682
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from absv import absv
from ln import ln
import math

def tof(expr):
    if isinstance(expr, const):
        return const_tof(expr)
    elif isinstance(expr, pwr):
        return pwr_tof(expr)
    elif isinstance(expr, prod):
        return prod_tof(expr)
    elif isinstance(expr, plus):
        return plus_tof(expr)
    elif isinstance(expr, quot):
        return quot_tof(expr)
    elif isinstance(expr, ln):
        return ln_tof(expr)
    elif isinstance(expr, absv):
        return absv_tof(expr)
    else:
        raise Exception('tof: ' + str(expr))

## here is how you can implement converting
## a constant to a function.
def const_tof(c): #make a function of a constant
    assert isinstance(c, const)
    def f(x):
        return c.get_val()
    return f

def pwr_tof(expr): #find the function expr object in different methods
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()
    if isinstance(expb, const):
        if isinstance(d, const): #compute then constant and return a constant function
            baseValue = expb.get_val()
            degValue =  d.get_val()
            def f(x):
                return baseValue ** degValue
            return f
        elif not isinstance(d, const):
            if expb.get_val() == math.e:
                degFunction = tof(d)
                finalFunction = lambda x: math.e**degFunction(x)
                return finalFunction
        else:
            raise Exception('pw_tof: case 0:' + str(expr))
    elif isinstance(expb, var):
        if isinstance(d, const): #return a function with a variable raised to a constant power
            # degValue = d.get_val()
            # f = lambda x: x**degValue
            # return f
            degValue = d.get_val()
            def f(x):
                if x == 0 and degValue < 0:
                    return 0
                else:
                    return x ** degValue

            return f
        else:
            raise Exception('pw_tof: case 1:' + str(expr))
    elif isinstance(expb, plus): #recursive compute the function of the two plus elements and
                                 #return a function that wil add them together
        if isinstance(d, const):
            degValue = d.get_val()
            elt1 = expb.get_elt1()
            elt2 = expb.get_elt2()
            elt1Function = tof(elt1)
            elt2Function = tof(elt2)
            finalFunction = lambda x: (elt1Function(x) + elt2Function(x))**degValue
            return finalFunction
        else:
            raise Exception('pw_tof: case 2:' + str(expr))
    elif isinstance(expb, pwr): #recrusively compute the function of the pwr obj
                                # and return a function that is raised to the d constant
        if isinstance(d, const):
            deg1Value = d.get_val()
            base2Function = tof(expb)
            finalFunction = lambda x: ((base2Function(x)))**deg1Value
            return finalFunction
        else:
            raise Exception('pw_tof: case 3:' + str(expr))
    elif isinstance(expb, prod):#recursively compute the function of the two mult elements and
                                #return a function that will multiply them
        if isinstance(d, const):
            degValue = d.get_val()
            mult1 = expb.get_mult1()
            mult2 = expb.get_mult2()
            mult1Function = tof(mult1)
            mult2Function = tof(mult2)
            finalFunction = lambda x: (mult1Function(x) * mult2Function(x))**degValue
            return finalFunction
        else:
            raise Exception('pw_tof: case 4:' + str(expr))
    elif isinstance(expb, quot):
        if isinstance(d, const):
            degValue = d.get_val()
            numerator = expb.get_num()
            denom = expb.get_denom()
            numeratorFunction = tof(numerator)
            denominatorFunction = tof(denom)
            quotFunction = lambda x: (numeratorFunction(x) / denominatorFunction(x)) ** degValue
            return quotFunction
    elif isinstance(expb, ln):
        if isinstance(d, const):
            degValue = d.get_val()
            exprFunction = tof(expb.get_expr())
            finalFunction = lambda x: math.log(exprFunction(x), math.e)**degValue
            return finalFunction
    else:
        raise Exception('pw_tof: case 5:' + str(expr))

def prod_tof(expr): #recursively compute the the function of the two mult objects
                    #and return a function that will multiply the those two functions
    assert isinstance(expr, prod)
    mult1 = expr.get_mult1()
    mult2 = expr.get_mult2()
    mult1Function = tof(mult1)
    mult2Function = tof(mult2)
    finalFunction = lambda x: (mult1Function(x) * mult2Function(x))
    return finalFunction

def plus_tof(expr): #recursively compute the function of the tow plus object and
                    #return a function that will add the two function together
    assert isinstance(expr, plus)
    element1 = expr.get_elt1()
    element2 = expr.get_elt2()
    elt1Function = tof(element1)
    elt2Function = tof(element2)
    finalFunction = lambda x: (elt1Function(x) + elt2Function(x))
    return finalFunction
def quot_tof(expr): #recursively compute the function of quot object
    assert isinstance(expr, quot)
    numerator = expr.get_num()
    denominator = expr.get_denom()
    numeratorFunction = tof(numerator)
    denominatorFunction = tof(denominator)

    def exprFunction(x):
        if denominatorFunction(x) == 0:
            raise Exception('You cannot divide by zero' + str(expr))
        else:
            return numeratorFunction(x) / denominatorFunction(x)

    return exprFunction
def ln_tof(lnexpr):
    assert  isinstance(lnexpr, ln)
    exprFunction = tof(lnexpr.get_expr())
    finalFunction = lambda x: math.log(exprFunction(x), math.e)
    return finalFunction
def absv_tof(absExpr):
    assert isinstance(absExpr, absv)
    exprFunc = tof(absExpr.get_expr())
    absFunc = lambda x: abs(exprFunc(x))
    return absFunc
