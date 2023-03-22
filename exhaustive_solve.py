from jssp import Jssp 

class ExhausivelSolve(object):
    def __init__(self):
        pass

    def solve(self,jssp:Jssp):
        x = []
        t = jssp.jssp_solve(x)
        return x,t


if __name__ == "__main__":
    j = Jssp("./test.txt")
    solver = ExhausivelSolve()

    x,t =  solver.solve(j)
    print(x)
    print(t)