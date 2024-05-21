
#IN Operator
names = ['jon', 'kalob', 'Filip']
print ('jon' in names) #returns as true
if 'kalob' in names:
    print('Kalob is in the list of names')

key = 'name'
person = {
    'name': 'doug'
}
if key in person:
    print('Can use IN operator to check for an object key')   

fruit = 'apple'
myset = {"apple", "banana", "cherry"}
if fruit in myset:
    print('Yes In op works for Python sets too.')     

#Python Playground for review
for i in range(10):
    print(i)
