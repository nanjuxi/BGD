from jssp import Jssp 
import itertools

def DiGui(n):
    if n==1:
        return 1
    return n*DiGui(n-1)

class ExhausivelSolve(object):
    def __init__(self,jp:Jssp):
        self.p_iter = []
        self.x = []
        self.jp = jp
        for i in range(0,jp.m):
            self.p_iter.append(itertools.permutations([i for i in range(1,jp.n + 1)]))
            self.x.append(next(self.p_iter[i]))


    def solve(self):
        jp =self.jp
        t_min = 99999999999
        x_fal = []
        k = DiGui(jp.n)
        p = [0 for i in range(0,jp.m)]
        count = 0
        count_sum = k**jp.m
        while(True):
            count = count +1
            t = jp.jssp_solve(self.x)
            # print(self.x)
            if t < t_min:
                t_min = t
                x_fal = self.x
            
            
            p[jp.m-1]=p[jp.m-1]+1
            inv=0 # 进位标志
            idx = jp.m-1 # 正在处理的p的下标
            while idx >=0:
                p[idx] = p[idx]+inv
                if p[idx] >= k:
                    inv =1 
                    p[idx] = p[idx]-k 
                    self.p_iter[idx] = itertools.permutations([i for i in range(1,jp.n + 1)])
                    self.x[idx] = next(self.p_iter[idx])
                    idx = idx-1
                else:
                    self.x[idx] = next(self.p_iter[idx])
                    inv = 0
                    break
            
            if p == [0 for i in range(0,jp.m)]:
                break
            if count % 100 == 0:
                print(f"穷举进度: {count}/{count_sum}",end='\r')
        
        # print(f"总共有{count}个x矩阵")
        # print(x_fal,t_min)
        return x_fal,t_min

        x_all = itertools.permutations([i for i in range(1,jssp.n + 1)])
       
        return x,t


if __name__ == "__main__":
    j = Jssp("./Tailard15_15.txt")
    # j = Jssp("./test.txt")
    solver = ExhausivelSolve(j)

    x,t =  solver.solve()
    # print(x)
    # print(t)
