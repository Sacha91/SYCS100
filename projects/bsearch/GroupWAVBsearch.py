#Hezekiah
#Michelle
#Sacha
#Eboni
#Ashanti
#Tyler

#Hezekiah's code starts here

def bsearch(horribleBandShirtList, name):
	searchFor = raw_input ("Who are you trying to find? Please enter their name followed by an ampersand (Ex. Tina&): ")
	firstName = 0
	lastName = len(horribleBandShirtList)
	found = False
	
	while firstName < lastName and horribleBandShirtList != 0 and not found:
		middle = ((firstName + lastName) // 2)
		
		if horribleBandShirtList [middle] < searchFor:
			firstName = middle
		
		elif horribleBandShirtList [middle] > searchFor:
			lastName = middle
		
		else:
			found = True
	
	if found == True:
		return middle 
	else:
		return -1


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
			return n
		else:
			return -1
	else:
		return -1	


#Sacha's code starts here

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
         return halfElement
   else:
         return -1
   
        
            
    
    

                 
    
  



    
    
   

