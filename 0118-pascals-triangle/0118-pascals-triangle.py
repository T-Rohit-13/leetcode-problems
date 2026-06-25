class Solution(object):
    def generate(self, numRows):
        pas=[[1,0]]
        for i in range(numRows-1):
            ip=[1]
            for j in range(len (pas)-1):
                s=(pas[i][j]+pas[i][j+1])
                ip.append(s)
            ip.append(1)
            pas.append(ip)
        del pas[0][1]
        return pas
        