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


#Ashanti's code starts here

def bsearch(list,x):
	if list != None:
		hi = len(list)
		lo = 0
		n = (hi+lo)/2
		a = 0
		while list[n] != x and a < len(list):
			if list[n] < x:
				lo = n
			elif list[n] > x:
				hi = n
			n = (hi+lo)/2
			a += 1
		
		if list[n] == x:
			print n
		else:
			print -1
	else:
		print -1	


   
        
            
    
    

                 
    
  



    
    
   

