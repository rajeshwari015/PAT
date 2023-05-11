class greater:
    def __init__(self,lst):
        self.lst=lst
    def __getitem__(self,index):
        return self.lst[index]
    def __setitem__(self,index,val):
        self.lst[index]=val
numlst= greater([1,2,3,4,5,6,7,8,9])
print(numlst[3])
numlst[3]=10
print(numlst.lst)
