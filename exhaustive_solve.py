from jssp import Jssp 
import itertools
class ExhausivelSolve(object):
    def __init__(self):
        pass

    def solve(self,jp:Jssp):
        t_min = 99999999999
        x_fal = []
        x = []

        x_all_iter= itertools.permutations([i for i in range(1,jp.n + 1)])
        x_all = []
        for i in x_all_iter:
            x_all.append(i)
        k = len(x_all)

        p = [0 for i in range(0,jp.m)]
        count = 0
        count_sum = k**jp.m
        while(True):
            x = []
            for i in p:
                x.append(x_all[i])
            count = count +1
            t = jp.jssp_solve(x)

            if t < t_min:
                t_min = t
                x_fal = x
            
            
            p[jp.m-1]=p[jp.m-1]+1
            inv=0 # 进位标志
            idx = jp.m-1 # 正在处理的p的下标
            while idx >=0:
                p[idx] = p[idx]+inv
                if p[idx] >= k:
                    inv =1 
                    p[idx] = p[idx]-k 
                    idx = idx-1
                else:
                    inv = 0
                    break
            
            if p == [0 for i in range(0,jp.m)]:
                break
            if count % 100 == 0:
                print(f"穷举进度: {count}/{count_sum}",end='\r')
        
        print(f"总共有{count}个x矩阵")
        print(x_fal,t_min)
        return x_fal,t_min

        x_all = itertools.permutations([i for i in range(1,jssp.n + 1)])
       
        return x,t


if __name__ == "__main__":
    j = Jssp("./Tailard15_15.txt")
    solver = ExhausivelSolve()

    x,t =  solver.solve(j)
    print(x)
    print(t)
