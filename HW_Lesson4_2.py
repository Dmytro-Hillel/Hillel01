mylist = [0, 1, 7, 2, 4, 8]
##mylist = [1, 3, 5]
#mylist = [6]
#mylist = []

if len(mylist) > 0:
    mysum=0
    for it in range(0,len(mylist),2):
        mysum=mysum+mylist[it]
        #print(mysum)

    print(mysum*mylist[-1])
else:
    print(0)