class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        if data==self.data:
            return # node already exist

        if data<self.data:
            #add data in left subtree
            if self.left:#if there is already a second level parent
                self.left.add_child(data)# it will call again the whole method.if there is already a node.this process is called recurssion
            else:#if there is no parent in second level then create it 
                self.left=BinarySearchTreeNode(data)#if there is no node this will create a node 

        else:#if the data is greater than parent(self.data)
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)


    def search(self,val):
        if self.data==val:
            return True
        
        if val<self.data:
            if self.left:
                return self.left.search(val)#this search will runs repeatedly untill it finds number
            else:
                return False

        if val>self.data:
            if self.right:
                return self.right.search(val)#this process is called recurssion
            else:
                return False


    def in_order_traversal(self):#while using this method all the random nums in list we provided were listed in a order as inside code in order traversal mode 
        elements=[]

        #visit left tree
        if self.left:
            elements+=self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements+=self.right.in_order_traversal()
        
        
        return elements


#Simply put, you cannot assign anything to self. In Python, self is a reference to the object that you called the method on. It would not be None (so you don't need the if self is None check), and you cannot assign some other value to it.
# Simply put, you cannot assign anything to self. In Python, self is a reference to the object that you called the method on. It would not be None (so you don't need the if self is None check), and you cannot assign some other value to it.  
    def elete(self,val):
        if val<self.data:
            if self.left:
                self.left=self.left.elete(val)
        elif val>self.data:
            if self.left:
                self.right=self.right.elete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.elete(min_val)

        return self

         

            


    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def count(self):
        elements=[]

        #visit left tree
        if self.left:
            elements+=self.left.in_order_traversal()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements+=self.right.in_order_traversal()

        return sum(elements)


        

def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree=build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.min())
    print(numbers_tree.max())
    print(numbers_tree.count())
    print(numbers_tree.search(1))

    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))


    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.elete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]
