from .__init__ import *


def permutationFunc(maxlength=20):
    a = random.randint(10, maxlength)
    b = random.randint(0, 9)

    solution = int(math.factorial(a) / (math.factorial(a - b)))
    problem = "Number of Permutations from {} objects picked {} at a time =  ".format(a, b)
    return problem, solution
