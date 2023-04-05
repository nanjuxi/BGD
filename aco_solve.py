

class AcolSolve(object):
    def InitInforMatrix(self,n,m):
        self.t = []
        k = m*n+1
        for i in range(0,k):
            self.t.append([1]*k)

    def DistanceMatrix(self,n,m,Times):
        k = m*n+1
        self.eta = [0]*k         
        for i in range(0,m):
            for j in range(0,n):
                z =  n*i+j+1
                self.eta[z] = Times[i][j]
        

    def __init__(self,a,b,rou,q,ant_count,num_count,jp:Jssp):
        self.jp = jp
        #初始化信息素浓度矩阵
        self.InitInforMatrix(jp.n, jp.m)        
        # 初始化距离矩阵
        self.DistanceMatrix(jp.n, jp.m, jp.times)

        self.a = a # 信息素因子
        self.b = b # 启发因子
        self.rou = rou # 信息素衰减因子
        self.q = q # 信息素常数

        self.ant_count = ant_count # 蚂蚁数量
        self.num_count = num_count # 迭代次数
    
    def CalPDenominator():
        result = 0
        row = len(self.tau)
        col = len(self.tau[0])

        for i in range(row):
            for j in range(col):
                result += (self.tau[i][j]**self.a) * (self.eta[j]**self.b)
        return result

    # 计算Pij矩阵
    def CommutePij(i,j):
        return (self.tau[i][j]**self.a)*(self.eta[j]**self.b)/self.pd



    def AntPathGenerate():
        pass
    def AntPathToX(path):
        pass

    # 生成蚂蚁行走路径path 与 x矩阵
    def AntX():
        path = self.AntPathGenerate()
        x = self.AntPathToX(path)
        return path,x

    # 计算蚂蚁的动作，包括求解x矩阵以及makespan
    # 输出：
    #     1. 蚂蚁的路径
    #     2. x矩阵
    #     3. makespan
    def AntAction():
        # 1. 得到x矩阵
        path,x  = self.AntX()
        # 2. Jssp计算
        makespan = self.jp.jssp_solve(x)
        return path,x,makespan

    def TauUpdate(ant_result):

        pass

    def run():
        x_best = []
        makespan_best = 100000000000
        for i in range(self.num_count):
            # 1.计算P的分母
            self.pd =  self.CalPDenominator()
            # 2. 计算所有蚂蚁的加工矩阵x以及对于jssp的求解结果
            ant_result = []
            for j in range(self.ant_count):
                path,x,makespan = self.AntAction()
                if(makespan< makespan_best):
                    makespan_best = makespan
                    x_best = x
                ant_result.append([path,x,makespan])
            # 3. 更新信息素浓度矩阵
            self.TauUpdate(ant_result)
        return x_best,makespan_best


