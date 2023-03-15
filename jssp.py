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
        while(row2<20+n):
            line = linecache.getline(path, row2).split()
            machines[row2-20,:]=line[:]
            row2+=1
        self.m = m
        self.n = n
        self.times = times
        self.machines = machines

    def jssp_solve(self,x):
        work_machine = []
        for i in range(self.m):
            work_machine.append([])
        for i in range(self.n):
            for j in range(self.m):
                k = int(self.machines[i][j])
                work_machine[k-1].append([i,j,self.times[i][j]])


        makespan=0

        return makespan

if __name__=="__main__":
    j = Jssp("./Tailard15_15.txt")
    # makespan = j.jssp_solve([[1,2,3],[1,2,3],[1,2,3]])
    # print(makespan)
    x = 0
    i = j.jssp_solve(x)
   

# machine1的工作队列[
# [(1,14,t),(2,11)(),(),()],
# [()()()()],
# [()()()],
# ]

