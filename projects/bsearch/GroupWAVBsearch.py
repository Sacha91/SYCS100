#Hezekiah

horribleBandShirtList = ["Aaron&", "Blake&", "Chett&", "Dave&", "Eric&", "Fred&", "Gordon&", "Harry&", "Ian&", "Jack&", "Kris&", "Lawrence&", "Mike Too"]

def bsearch():
   
	searchFor = raw_input ("Who are you trying to find? Please enter their name followed by an ampersand (Ex. Tina&): ")
	firstName = 0
	lastName = len(horribleBandShirtList) 
	found = False
	
	while firstName < lastName and not found:
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

bsearch()






#Michelle
#Sacha
#Eboni
#Ashanti
#Tyler


sList = ['Appricot', 'Brown', 'Green', 'Purple', 'Sun', 'Teal', 'Yellow']  
def bSearch():
   hi = len(sList)
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
        
