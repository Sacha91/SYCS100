#Hezekiah
#Michelle
#Sacha
#Eboni
#Ashanti
#Tyler


sList = ['Appricot', 'Brown', 'Green', 'Purple', 'Sun', 'Teal', 'Yellow']  
def bSearch():
   hi = len(sList)- 1
   lo = sList[0]
   found = False
   desiredElement = sList[4]
   while lo < hi and found == False:
        halfElement = (lo+hi)//2
        if sList[halfElement] < desiredElement:
           lo = halfElement + 1
        elif sList[halfElement] > desiredElement:
           hi = halfElement - 1
        else:
           found = True
   if found:
         print 'found name'
   else:
         print '-1'
bSearch ()
        
