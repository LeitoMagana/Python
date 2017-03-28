List = [1, 2, 1, 5, 0, 3]
def Promedio(plist):
    if len(plist)>0:
     return reduce(lambda x,y:x+y,plist)/len(plist)
     return 0
 
print 'Promedio:',Promedio(List)
Promedio()
