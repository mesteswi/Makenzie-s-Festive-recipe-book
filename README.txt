Makenzie Estes Williams
CSE20
3 December 2021
			Festive Drink Book

Repository Link: https://github.com/mesteswi/Makenzie-s-Festive-recipe-book

The purpose of this class is to create a small recipe book to compile all your favorite festive drink recipes. The book primarily intakes ingredients since it is a drink recipe book but it does have the option of adding additional instructions if the drink calls for it. This class also has the option to add drinks into the recipe book or even create a text file of the recipe book that you can share with your friends for the Holidays!

Class and Data Variables:
The class variable is a list of five drinks along with their ingredients that are separated by commas. This variable is used within the create_recipes( ) method. The first Data variable is self.__recipes which is the dictionary created in the create_recipes( ) function, this variable is used in many different methods so it is important to make it private. Another data attribute is self.__drink which is separate from the class variable drinks. This variable is used in the separate functions as well so it is made private.

Create_recipes( ):
This function creates the recipe book that can be added onto by the user. There are five drinks in a list to start the recipe book. The function takes the name of the drink and makes it a key in the dictionary that will store all the drinks. The list of ingredients is the values in the dictionary.

Get_recipe(drink):
	This function intakes a drink as an argument, iterates through the list of drinks in the book, and then returns the list of ingredients. If the drink inputted as an argument doesn’t exist in the recipe book, then it will print an error message that prompts the user to add the drink into the book.

Set_new_recipe(drink):
	This function intakes a list as an argument that contains the name of the drink as the first item and then ingredients as well. The function then stores the name of the drink as a key and the ingredients as the value in the recipe book.

Get_drink_list( ):
	This function has no arguments; instead, it returns a list of the drinks within the recipe book. This method can be used to create a table of contents or just to take a look at what drinks you have stored.

Set_added_instructions(Instructions):
This method intakes one argument of instructions for the drink in the form of a list or string. The method will then create a separate dictionary that stores the instructions and adds them to the drink. You can use the get_recipe(drink) function to return the list of ingredients and added instructions for a specific drink.

Create_book( ):
The create book function formats the dictionary that has all the drink recipes into a text file that can be shared with friends and family.

__str__( ):
This method has no input arguments and returns all the drinks with the ingredients that are separated by new lines and a tab.

Directions for Demo Script:
	For the demo script, all of the class methods are already implemented into the main function. The main function has a line for each method to showcase how each one works. All the user needs to do is uncomment which method they would like to use by either deleting the hashtag or highlighting the line and using ctrl + /, and then input the correct parameters. Lines 106,109, and 110 do not require any arguments, so you can run them without having to edit anything. In Line 105, the get_recipe( ) method takes in one argument, this will be the name of a drink within the recipe book. If the drink is in the book then it will return back the list of ingredients, if not then it will return back an error message.For Line 107, the set_new_recipe( ) function takes in a drink as an argument. This should be a comma separated string or list that has the name of the drink and the ingredients, make sure that the drink name is the first item in the string or list. Lastly, in line 108 the set_added_instructions method intakes two arguments a drink and then a list or string of instructions. The drink name should be one of the existing drinks in the recipe book, if it does not exist then it will return a custom error message.

