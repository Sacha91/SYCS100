#Hezekiah
#Michelle
#Sacha
#Eboni
#Ashanti
#Tyler

#Eboni's code start's here

def bsearch (itemB, bList):
    lo = 0
    high = len(bList) - 1
   
    while lo <= high:
        mid = (lo + high)//2

        if bList[mid] == itemB:
            return mid
        elif bList[mid] < itemB:
            lo = mid + 1
        else:
            high = mid - 1
    return -1





   
        
            
    
    

                 
    
  



    
    
   

