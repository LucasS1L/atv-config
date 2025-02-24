def example01():
    from math import sqrt
    print('resolução numérica: ', sqrt(10))
    print()

def example02():
    import sympy as sp
    print('resolução simbólica: ', sp.sqrt(10))
    print()

def example03():
    import sympy as sp
    print('resolução simbólica: ', sp.sqrt(40))
    print()

def example04():
    from sympy import symbols, pprint
    x, y, z = symbols('x y z')
    solution = x + 2*y + z*x
    pprint(solution)
    solution2 = solution * x
    pprint(solution2)
    print()

def example05():
    from sympy import expand, symbols, pprint
    x, y, z = symbols('x y z')
    pprint(expand((x + 2*y + z*x)* x))
    print()
    
def example06():
    from sympy.abc import x,y
    from sympy import solve, pprint
    solution = solve(x**2 - y, x, dict=True)
    pprint(solution)
    print()

def example07():
    from sympy.abc import x,y,z
    from sympy import solve, pprint
    solution = solve([x**2 + y - 2*z, y + 4*z], x, y, dict=True)
    pprint(solution)
    print()

def example08():
    from sympy import solveset, pprint
    from sympy.abc import x,y
    solution = solveset(x**2 - y, x)
    pprint(solution)
    print()

def example09():
    from sympy import solveset, pprint, sin
    from sympy.abc import x
    solution = solveset(sin(x), x)
    pprint(solution)
    print()
    
def example10():
    from sympy import solveset, pprint, S
    from sympy.abc import x
    solution = solveset(x**4 - 256, x, domain=S.Reals)
    pprint(solution)
    print()

def example11():
    from sympy import pprint, diff, sin, exp
    from sympy.abc import x
    solution = diff(sin(x)*exp(x), x)
    pprint(solution)
    print()

def example12():
    from sympy import pprint, integrate, sin, oo
    from sympy.abc import x
    solution = integrate(sin(x**2), (x, -oo, oo))
    pprint(solution)
    print()

def example13():
    from sympy import pprint, limit, sin
    from sympy.abc import x
    solution = limit(sin(x)/x, x, 0)
    pprint(solution)
    print()

def example14():
    from sympy import pprint, symbols
    from sympy.matrices import Matrix
    c, d, e = symbols("c, d, e")
    pprint(Matrix([[c, d],[1, -e]]))
    print()
    
def example15():
    from sympy import pprint
    from sympy.matrices import Matrix
    pprint(Matrix([[1, 2],[2, 2]]).eigenvals())
    print()

def example16():
    from sympy import pprint, symbols, exp, diff
    x = symbols("x")
    sympy_tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
    pprint(sympy_tanh)
    print()
    solution = diff(sympy_tanh, x)
    pprint(solution)
    print()

example01()
example02()
example03()
example04()
example05()
example06()
example07()
example08()
example09()
example10()
example11()
example12()
example13()
example14()
example15()
example16()