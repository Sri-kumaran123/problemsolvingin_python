from values import Values

class Greedy(Values):
    Max_value = 0

    def __init__(self):
        super().__init__()
        
    def SetItems(self):
        self.Items = sorted(zip(self.Values,self.Weights),key = lambda x:x[0]/x[1],reverse=True)
        return self
    
    def Arrange(self):
        for v,w in self.Items:
            if(self.TotalWeight > w):
                self.TotalWeight -=w
                self.Max_value +=v
            else:
                self.Max_value += v *(self.TotalWeight/w)
                break
        return self.Max_value

    
    

gr = Greedy()
print(gr.Max_value)
gr.setValue([1,1,1]) \
    .setWeight([2,4,6]) \
    .setTotalWeight(7)  \
    .SetItems() 

print(gr.Arrange())

