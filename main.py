from stack02 import Stack

mystack = Stack()
print("\nIs stack Empty ? ",mystack.isEmptyStack())
print("Stack Size : " , mystack.size())
mystack.push(10)
mystack.push(20)
mystack.push(30)
print("Stack Top element is ", mystack.top())
mystack.push(40)
mystack.push(50)
mystack.push(60)

print(" Stack Top element is : ", mystack.top())
print(" Stack Size : ", mystack.size())
print(" Is stack Full ? ", mystack.isFullStack())
