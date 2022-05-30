

class Stack:
    
    def __init__(self, max_num_items:int = None):
        self.items = []
        
        if max_num_items is None:
            max_num_items = 10^6
        else:
            self.max_num_items = max_num_items
        
    def IsEmpty(self):
        return (self.items == [])
    
    def IsFull(self):
        return (len(self.items) - 1 == self.max_num_items)
    
    def Push(self, item):
      if (len(self.items) + 1) > self.max_num_items:
        return False
      else:
        return self.items.append(item)
    
    def Pop(self):
        if self.IsEmpty():
            return self.items
        else:
            return self.items.pop()
    
    def PeekTop(self):
        if self.IsEmpty():
            return self
        else:
            return (self.items[len(self.items)-1])
    
    def PrintStack(self):
        print(self.items)
      
    def ReturnStack(self):
        return self.items
        
    def CurrentSize(self):
        return len(self.items) - 1

    def SetMaxCapacity(self, new_max_capacity):
        self.max_num_items = new_max_capacity

    def Clear(self):
      self.items.clear()
      

    
