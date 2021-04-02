class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h % self.MAX

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                found=True
                
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        arr_index=self.get_hash(key)
        for element in self.arr[arr_index]:
            if element[0]==key:
                return element[1]


    def __delitem__(self,key):
        arr_index=self.get_hash(key)
        for index ,kv in enumerate(self.arr[arr_index]):
            if kv[0]==key:
                print("del",index)
                del self.arr[arr_index][index]

t=HashTable()    
t['march 6'] = 310
t['march 1']=20
t['dec 17']=27
t["march 6"]= 78
t["march 17"]= 63457

print(t.arr)
del t["march 1"]
print(t.arr)

