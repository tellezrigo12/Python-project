#!/usr/bin/python3

####################################
# Rigoberto Tellez
# A02169682
####################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_prod, make_const, make_pwr, make_plus, make_pwr_expr, make_quot, make_e_expr, make_ln
from maker import  make_absv
from tof import tof
from quot import quot
from absv import absv
from ln import ln
from absv import absv
import math

def deriv(expr):
    if isinstance(expr, const):
        return const_deriv(expr)
    elif isinstance(expr, pwr):
        return pwr_deriv(expr)
    elif isinstance(expr, prod):
        return prod_deriv(expr)
    elif isinstance(expr, plus):
        return plus_deriv(expr)
    elif isinstance(expr, quot):
        return quot_deriv(expr)
    elif isinstance(expr, ln):
        return ln_deriv(expr)
    else:
        raise Exception('deriv:' + repr(expr))

# the derivative of a consant is 0.
def const_deriv(c):
    assert isinstance(c, const)
    return const(val=0.0)

def plus_deriv(s):  #recursively compute the derivative of the left side of the plus operator and
                    #right side of the plus operator respectively and then add the two parts
    leftSide = s.get_elt1()
    rightSide = s.get_elt2()
    newLeftSide = deriv(leftSide)
    newRightSide = deriv(rightSide)
    finalResult = plus(newLeftSide, newRightSide)
    return finalResult

def pwr_deriv(p): #takes a pwr object takes the derivative of the
                  #the base by using lots of recursion
    assert isinstance(p, pwr)
    b = p.get_base()
    d = p.get_deg()
    if isinstance(b, var): #
        if isinstance(d, const):
            newDeg = d.get_val()
            newDeg = newDeg -1
            if newDeg < 0:
                return make_const(0)
            else:
                newReuslt = pwr(b, const(newDeg))
                finalProduct = prod(const(newDeg + 1), newReuslt)
                return finalProduct
        else:
            raise Exception('pwr_deriv: case 1: ' + str(p))
    if isinstance(b, pwr): #takes another pwr object and take the derivavtive recursively
        if isinstance(d, const):
            newB = deriv(b)
            newDeg = d.get_val() -1
            p = pwr(b, const(newDeg))
            newPart = prod(const(newDeg+1), p)
            finalResult = prod(newPart, newB)
            return finalResult
        else:
            raise Exception('pwr_deriv: case 2: ' + str(p))
    elif isinstance(b, plus): #takes plus object and computes the derivative recursively
        if isinstance(d, const):
            leftSide = b.get_elt1()
            rightSide = b.get_elt2()
            newDeg = d.get_val() - 1
            p = pwr(b, const(newDeg))
            p = prod(const(newDeg + 1), p)
            newLeftSide = deriv(leftSide)
            newRightSide = deriv(rightSide)
            newPart = plus(newLeftSide, newRightSide)
            finalResult = prod(p, newPart)
            return finalResult
        else:
            raise Exception('pwr_deriv: case 3: ' + str(p))
    elif isinstance(b, prod):#takes a prod objects and computes the derivative recursively
        if isinstance(d, const):
            newDeg = d.get_val() - 1
            p = pwr(b, const(newDeg))
            p = prod(const(newDeg + 1), p)
            b = prod_deriv(b)
            finalResult = prod(p, b)
            return finalResult
        else:
            raise Exception('pwr_deriv: case 4: ' + str(p))
    elif isinstance(b, quot):
        if isinstance(d, const):
            newDeg = d.get_val() - 1
            p = pwr(b, const(newDeg))
            p = prod(const(newDeg +1), p)
            b = deriv(b)
            finalResult = prod(p,b)
            return finalResult
        else:
            raise Exception('pwr deriv: case 5: ' + str(p))
    elif isinstance(b, const): #if the base is a constant then
                               #that base must be e and the deriv
                               #will be computed recusively
        if b.get_val() == math.e:
            if isinstance(d, const):
                return make_const(0)
            else:
                degDeriv = deriv(d)
                finalProduct = make_prod(p, degDeriv)
                return finalProduct
        else:
            raise Exception('power deriv: case 6:' + str(p))
    elif isinstance(b, ln):
        if isinstance(d, const):
            newDeg = d.get_val() - 1
            p = pwr(b, const(newDeg))
            p = prod(const(newDeg + 1), p)
            b = deriv(b)
            finalResult = prod(p, b)
            return finalResult
    else:
        raise Exception('power_deriv: case 7: ' + str(p))

def prod_deriv(p):
    assert isinstance(p, prod)
    m1 = p.get_mult1()
    m2 = p.get_mult2()
    if isinstance(m1, const):
        if isinstance(m2, const): #implement the constant rule
            return const(0)
            pass
        elif isinstance(m2, pwr): #recursively compute the pwr object derivative and use the constant rule
            newPart = deriv(m2)
            finalResult = prod(m1, newPart)
            return finalResult
        elif isinstance(m2, plus): #recursively compute the plus object derivative and use the constant rule
            newPart = deriv(m2)
            finalResult = prod(m1, newPart)
            return finalResult
        elif isinstance(m2, prod): #recursively compute the prod object derivative and use the constant rule
            newPart = deriv(m2)
            finalResult = prod(m1, newPart)
            return finalResult
        elif isinstance(m2, quot):
            newPart = deriv(m2)
            finalResult = prod(m1, newPart)
            return finalResult
        elif isinstance(m2, ln):
            newPart = deriv(m2)
            finalResult = prod(m1, newPart)
            return finalResult
        elif isinstance(m2, quot):
            newPart = deriv(m2)
            finalResult = prod(m1, newPart)
            return finalResult
        else:
            raise Exception('prod_deriv: case 0' + str(p))
    elif isinstance(m1, plus):
        if isinstance(m2, const): #recursively compute the plus object derivative and use the constant rule
            newPart = deriv(m1)
            finalResult = prod(m2, newPart)
            return finalResult
    elif isinstance(m1, pwr):
        if isinstance(m2, const): #recursively compute the pwr object derivative and use the constant rule
            newPart = deriv(m1)
            finalResult = prod(m2, newPart)
            return finalResult
    elif isinstance(m1, prod):
        if isinstance(m2, const): #recursively compute the prod object derivative and use the constant rule
            newPart = deriv(m1)
            finalResult = prod(m2, newPart)
            return finalResult
    elif isinstance(m1, ln):
        if isinstance(m2, const):
            newPart = deriv(m1)
            finalResult = prod(m2, newPart)
            return finalResult
    elif isinstance(m1, quot):
        if isinstance(m1, const):
            newPart = deriv(m1)
            finalResult = prod(m2, newPart)
            return finalResult
    m1Prime = deriv(m1)
    m2Prime = deriv(m2)
    element1 = prod(m1Prime, m2)
    element2 = prod(m2Prime, m1)
    pPrime = plus(element1, element2)
    return pPrime

def quot_deriv(expr): #recursively compute the derivatvie of a quotient
    assert isinstance(expr, quot)
    numerator = expr.get_num()
    denominator = expr.get_denom()
    numeratorPrime = deriv(numerator)
    denominatorPrime = deriv(denominator)
    element1 = prod(denominator, numeratorPrime)
    element2 = prod(numerator, denominatorPrime)
    element3 = prod(make_const(-1.0), element2)
    element4 = plus(element1, element3)
    element5 = pwr(denominator, make_const(2.0))
    exprPrime = quot(element4, element5)
    return exprPrime
def ln_deriv(expr):
    assert  isinstance(expr, ln)
    Denom = expr.get_expr()
    if isinstance(Denom, absv):
        Denom = Denom.get_expr()
    quotPart = make_quot(make_const(1), Denom)
    derrivExpr = deriv(Denom)
    return make_prod(quotPart, derrivExpr)
def logdiff(expr):
        lnExpr = applyLog(expr)
        lnExprPrime = deriv(lnExpr)
        return make_prod(expr, lnExprPrime)
def applyLog(expr):
    if isinstance(expr, quot):
        lnExpr1 = applyLog(expr.get_num())
        lnExpr2 = applyLog(expr.get_denom())
        minusPart = prod(const(-1.0), lnExpr2)
        return plus(lnExpr1, minusPart)
    if isinstance(expr, prod):
        if isinstance(expr.get_mult1(), const) and isinstance(expr.get_mult2(), pwr):
            return make_ln(expr)
        elif isinstance(expr.get_mult1(), pwr) and isinstance(expr.get_mult2(), const):
            return make_ln(expr)
        elif isinstance(expr.get_mult1(), const) and isinstance(expr.get_mult1(), const):
            return make_ln(expr)
        else:
            lnExpr1 = applyLog(expr.get_mult1())
            lnExpr2 = applyLog(expr.get_mult2())
            return make_plus(lnExpr1, lnExpr2)
    if isinstance(expr, plus):
        if isinstance(expr.get_elt1(), pwr):
            if isinstance(expr.get_elt2(), const):
                return make_ln(expr)
            if isinstance(expr.get_elt2(), pwr):
                return make_ln(expr)
            else:
                if isinstance(expr.get_elt2(), plus):
                    lnExpr = applyLog(expr.get_elt2())
                    return make_plus(make_ln(expr.get_elt1()),lnExpr )
                else:
                    return make_ln(expr)
        elif isinstance(expr.get_elt1(), const):
            if isinstance(expr.get_elt2(), const):
                return make_ln(expr)
            elif isinstance(expr.get_elt2(), pwr):
                return make_ln(expr)
            else:
                if isinstance(expr.get_elt2(), plus):
                    lnExpr = applyLog(expr.get_elt2())
                    return make_plus(make_ln(expr.get_elt1()),lnExpr )
                else:
                    return make_ln(expr)
        elif isinstance(expr.get_elt2(), const):
            if isinstance(expr.get_elt1(), const):
                return make_ln(expr)
            elif isinstance(expr.get_elt1(), pwr):
                return make_ln(expr)
            else:
                if isinstance(expr.get_elt1(), plus):
                    lnExpr = applyLog(expr.get_elt1())
                    return make_plus(lnExpr, make_ln(expr.get_elt2()))
                else:
                    return make_ln(expr)
        elif isinstance(expr.get_elt2(), pwr):
            if isinstance(expr.get_elt1(), const):
                return make_ln(expr)
            if isinstance(expr.get_elt1(), pwr):
                return make_ln(expr)
            else:
                if isinstance(expr.get_elt1(), plus):
                    lnExpr = applyLog(expr.get_elt1())
                    return make_plus(lnExpr, make_ln(expr.get_elt2()))
                else:
                    return make_ln(expr)
        else:
            lnExpr1 = applyLog(expr.get_elt1())
            lnExpr2 = applyLog(expr.get_elt2())
            return plus(lnExpr1, lnExpr2)
    elif isinstance(expr, pwr):
        if isinstance(expr.get_deg(), const):
            if expr.get_deg().get_val() == 1.0:
                if isinstance(expr.get_base(), var):
                    return make_ln(expr)
                else:
                    lnExpr = applyLog(expr.get_base())
                    return lnExpr
            else:
                if isinstance(expr.get_base(), var):
                    return make_prod(expr.get_deg(), make_ln(expr))
                else:
                    lnExpr = applyLog(expr.get_base())
                    return make_prod(expr.get_deg(), lnExpr)

        else:
            if isinstance(expr.get_base(), var):
                return make_prod(expr.get_deg(), make_ln(expr))
            else:
                lnExpr = applyLog(expr.get_base())
                return make_prod(expr.get_deg(), lnExpr)
    elif isinstance(expr, const):
        return make_ln(expr)

