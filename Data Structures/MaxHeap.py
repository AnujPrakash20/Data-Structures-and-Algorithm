class Maxheap:
    def __init__(self,values):
        self.heap=[0]
        for i in values:
            self.heap.append(i)
            self.__floatup(self.heap.index(i))


    def push(self,data):
        self.heap.append(data)
        self.__floatup(self.heap.index(data))

    def peek(self):
        if len(self.heap)>=2:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap)>2:
            self.__swap(1,len(self.heap)-1)
            max=self.heap.pop()
            self.__bubbledown(1)

    def __swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def __floatup(self,index):
        parent=index//2
        if index <=1:
            return
        if self.heap[index]>self.heap[parent]:
            self.__swap(index,parent)
            self.__floatup(parent)

    def __bubbledown(self,index):
        parent=index//2
        left=2*index
        right=2*index+1
        largest=index
        if len(self.heap)>left and self.heap[left]>self.heap[largest]:
            largest=left
        if len(self.heap)>right and self.heap[right]>self.heap[largest]:
            largest=right
        if index !=largest:
            self.__swap(index,largest)
            self.__bubbledown(largest)

m = Maxheap([95, 3, 21])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))
