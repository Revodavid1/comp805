"""
lab2.py
Oreva David Omu
1/30/2018
"""
def squared(num_list):
	"""
	Squares numbers in num_list
	num_list:list of numbers
	Returns:list of these numbers squared
	"""
	squarenumlist = [ ] #define result list
	for nums in num_list: #iterate through num_list
		squarenum = pow(nums,2) #square the numbers
		squarenumlist.append(squarenum) #add the number to the result list
	return squarenumlist

def check_title(title_list):
	"""
	Removes strings in title_list aren't title case
	title_list: list of strings
	Returns: list of strings that are titles
	"""

	newstrlist = [ ]
	for strs in title_list:
		if strs.istitle(): #checks if if string in the list is title case
			newstrlist.append(strs)
	return newstrlist
