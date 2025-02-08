from values import Values

class Dynamic(Values):
    def __init__(self):
        super().__init__()
        self.Length = 0
        self.Memory = []

    def initialize(self):
        self.Length = len(self.Values)
        self.Memory = [[-1] * (self.TotalWeight + 1) for _ in range(self.Length + 1)]

    def Calculate(self, n, w):
        if n == 0 or w == 0:
            return 0

        if self.Memory[n][w] != -1:
            return self.Memory[n][w]

        if self.Weights[n - 1] > w:
            self.Memory[n][w] = self.Calculate(n - 1, w)
        else:
            include = self.Values[n - 1] + self.Calculate(n - 1, w - self.Weights[n - 1])
            exclude = self.Calculate(n - 1, w)
            self.Memory[n][w] = max(include, exclude)
        
        return self.Memory[n][w]

# Example usage
dy = Dynamic()
dy.setValue([1, 2, 4, 5]) \
   .setWeight([3, 2, 4, 5]) \
   .setTotalWeight(15) \
   .initialize()

print(dy.Calculate(dy.Length, dy.TotalWeight))
