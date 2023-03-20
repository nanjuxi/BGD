#
import linecache
import numpy as np

class Jssp(object):
    def __init__(self, path):
        self.path = path
        self.read_dataset(path)

    def read_dataset(self,path):

        # f = open(path)
        text = linecache.getline(path, 2).split()
        n = int(text[0])
        m = int(text[1])
        times=np.zeros((n,m))
        row1=4
        while(row1<4+n):
            line = linecache.getline(path, row1).split()
            times[row1-4,:]=line[:]
            row1+=1
        machines=np.zeros((n,m))
        row2=5+n
        while(row2<5+2*n):
            line = linecache.getline(path, row2).split()
            machines[row2-(5+n),:]=line[:]
            row2+=1
        self.m = m
        self.n = n
        self.times = times
        self.machines = machines

    def jssp_solve(self,x):
        #获取work_machine工作队列
        #k表示machie_k
        # (i,j,time)表示job i 的第  j  道 工序 及其时间,work_machine[i][j][0]
        work_machine = []
        for i in range(self.m):
            work_machine.append([]) # 规模1*m
        for i in range(self.n):
            for j in range(self.m):
                k = int(self.machines[i][j])
                work_machine[k-1].append([i,j,self.times[i][j]])
        
        #对x矩阵进行转置
        
        x = np.array(x)
        x = x.T
        x = x.tolist()


        # 将work_machine工作队列按照xT矩阵排序
        # x(i,j)=y,表示machinei的第j道工序是joby的
        # temp[i](1*n)
        # 循环 判断x[i,j] == work_machines[i][j]三元组中的i值，将它赋值给temp[i]
        #将work_machines的第i行用temp[]代替。
        for i in range(self.m):
            temp = []
            for j in range(self.n): # X矩阵的
                for b in range(self.n): #work_machine 矩阵的
                    if  (x[i][j] - 1) == work_machine[i][b][0]:
                        temp.append(work_machine[i][b])
            work_machine[i] = temp
        
        # 初始化辅助矩阵H【15】，用H[i】表示job i 的前序工作
        H = [-1 for x in range(0,self.n)]
        makespan = 0
        S = [] #S表示正在运行的工序的集合  
        S1 = [] # S1表示集合S中时间最小的工序
        ts1 = 0 # ts1表示S1中工序的时间

        while(True):

            # 获取最小工序加入S1
            x_min = 999999999
            x_fal = []
            for x in S: # x表示三元组，x[2]表示工序的剩余加工时间
                if x[2] < x_min:
                    x_min = x[2]
                    x_fal = x
            S1 = x_fal

            # 判断S1是否为空，如果是，则将ts1=0；否则ts1=t1
            if S1 == []:
                ts1 = 0
            else:
                ts1 = S1[2]

            # 从S中删除S1，同时H【i】++，将S中剩余工序时间减掉ts1,makespan+=ts1
            makespan = makespan + ts1
            for x in S:
                if x == S1:
                    i = x[0]
                    H[i] = H[i]+1
                    del x
                else:
                    x[2] = x[2] - ts1
            
            

        return makespan

    def find_set(self,work_machine,H,S): #找出可执行的序列
        for i in range(0,self.m):





if __name__=="__main__":
    # j = Jssp("./test.txt")
    j = Jssp("./Tailard15_15.txt")
    # makespan = j.jssp_solve([[1,2,3],[1,2,3],[1,2,3]])
    # print(makespan)
    i = j.jssp_solve(x)
   

# machine1的工作队列[
# [(1,14,t),(2,11)(),(),()],
# [()()()()],
# [()()()],
# ]

