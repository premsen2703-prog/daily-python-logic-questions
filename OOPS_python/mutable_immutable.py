def change(l):
    print(id(l))
    l.append(5)
    print(id(l))

# l1 = [1,2,3,4] #mutable list
# print(id(l1))
# print(l1)#[1,2,3,4]
# print(id(change(l1[:])))
# print(l1)#[1,2,3,4,5,6] main list has changed
# # use cloning for not change { list_name[:] }


#imutable tuple 
l1 = (1,2,3,4)


