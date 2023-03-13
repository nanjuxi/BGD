#
import linecache
import numpy as np

class Jssp:
    def __init__(self, path):
        self.path = path
        # self.read_dataset(path)

    
    def txt_to_matrix(path):
        file=open(path)
        lines=file.readlines()
        #print lines
        #['0.94\t0.81\t...0.62\t\n', ... ,'0.92\t0.86\t...0.62\t\n']形式
        rows=len(lines)#文件行数
 
        datamat=np.zeros((rows,15))#初始化矩阵
  
        row=0
        for line in lines:
            line=line.strip().split('\t')#strip()默认移除字符串首尾空格或换行符
            datamat[row,:]=line[:]
            row+=1
        return datamat
    

    def read_dataset(path):

        f = open(path)
        text = linecache.getline(path, 2)
        n = text[1]
        print(text)

        m1 = []


        m=0
        n=0
        machine = [[1,2,3],[1,2,3]]
        time =[]
        return m,n,machine,time



    def jssp_solve(x):
        makespan=0
        return makespan

if __name__=="__main__":
    j = Jssp.txt_to_matrix("./Tailard15_15.txt")
    print(j)
    # makespan = j.jssp_solve([[1,2,3],[1,2,3],[1,2,3]])
    # print(makespan)
   



