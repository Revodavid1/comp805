"""
lab2.py
Oreva David Omu
1/30/2018
"""
def squared(num_list):
	"""
	Squares numbers in num_list
	squarenumlist:list of numbers
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
		if strs.istitle() and strs.isalpha(): #checks if if string in the list is title case
			newstrlist.append(strs)
	return newstrlist

def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictionary by 10
	inventory: a dictionary with:
		key: string that is the name of the inventory item
		value: integer that equals the number of that item currently on hand
	Returns: updated dictionary where each inventory item is restocked
	"""
	new_inventory = {}
	for key,val in invetory.items():
		new_inventory[key] = val + 10
	return new_inventory

def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: dictionary with:
		key: string that is the name of the inventory item
		value: integer that equals the number of that item currently on hand
	Returns: the same inventory_dict with any item that had 0 quantity removed
	"""
	newinventory = inventory.copy()
        for inventoryitem in inventory.keys():
            if newinventory[inventoryitem] == 0:
                del newinventory[inventoryitem]

	return newinventory

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    avgofdict = {}
    #gets each dictionary and finds it's average
    for i,j in grades.items(): 
        avgofdict[i] = sum(j)/ float(len(j))
    return avgofdict
