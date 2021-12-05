"""
Makenzie Estes Williams
Assignment 10.1: Your own class
Description: Use the skills that we have learned about OOP to create a class that models a real world object."""

class Drink_Recipe_Book:
    #class variable
    drinks=["Eggnog, 4 large eggs, separated, 1/3 cup plus 1 tablespoon sugar, 1 pint whole milk, 1 cup heavy cream, 1 1/4 fluid ounces bourbon, 1 1/4 fluid ounces dark rum, 1 teaspoon freshly grated nutmeg,",
        "Christmas Punch, 8 oz pomegranate seeds, 2 oranges, 1 cup orange juice fresh squeezed if possible, 16 oz pomegranate juice, 16 oz 100 percent cranberry juice, 2 tsp vanilla extract, 20 oz 7Up or similar soda",
        "Mulled wine, 1(750 ml) Bottle red wine, 2 Oranges, 3 Cinnamon sticks, 5 star anise, 10 Whole cloves, 3/4 cup Brown Sugar","White Grape Punch, 24 mint leaves, 2 cups White grape juice, 3 cups seltzer, 1/4 cup lime juice",
        "Pumpkin smoothie, 1 can (15 oz. size) pumpkin pie filling, 3 c. whole milk (more if needed), 1/2 c. vanilla yogurt (up to 1 cup), A few dashes of ground cinnamon, 4 cinnamon graham crackers (crushed)"]
    #__init__ function saves the dictionary from the create recipes function as a class variable
    def __init__(self):
        self.__recipes= self.create_recipes()
     
    def create_recipes(self):
        #Empty dictionary to store the drinks and recipes
        self.recipes={}
        for i in self.drinks:
            #makes each recipe a string so i can use the split method
            recipe= str(i)
            #splits at the comma
            recipe= list(recipe.split(','))
            #stores the ingredients into small dictionary 
            ingredients= {"Ingredients":i.split(',',1)[1]}
            #updates the dictionary so the drink is the key and the dictionary with the ingredients is the value
            self.recipes[recipe[0]]=ingredients
        #returns the dictionary
        return (self.recipes)

    
    def get_recipe(self,drink):
        #Try and except loop that will prints custom error message if the drink doesn't exist in the dictionary
        try:
            self.__drink = str(drink) 
            #gets the ingredient list for the specified drink
            recipe = self.__recipes[self.__drink]["Ingredients"]
            return f"Ingredients:\n\t{recipe}\n" 
        except KeyError:   
            return ("This drink is not in this recipe book yet :( Please update the recipe book if you would like to add this drink.")

    def set_new_recipe(self,new_drink):
        new_drinkk= str(new_drink)
        #splits the list from the drink by the commas
        new_drink_name= list(new_drinkk.split(','))
        #makes a dictionary that will store the ingredients
        ingredients= {"Ingredients":new_drinkk.split(',',1)[1]}
        #updates the existing dictionary to add the new drink
        self.__recipes[new_drink_name[0]]=ingredients
        return self.__recipes


    def get_drink_list(self):
        #empty list to add drink names
        drinklist = []
        #creates loop that iterates through each drink in the list
        for drink in self.__recipes:
        #adds each drink name into the list
            drinklist.append(drink)
        
        return drinklist

    def set_added_instructions(self,drink,instructions):
        #creates a dictionary with the instructiond
        instructions ={"Additional Instructions":instructions}
        #creates a loop that goes through each key
        for i in self.__recipes:
            #will retunr error if drink doesnt exist
            try:
                self.__drink = str(drink) 
                #adds the instructions to the value of the drink
                recipe = f'{self.__recipes[self.__drink]}, {instructions}'
                self.__recipes[i]= recipe
                return self.__recipes
            except KeyError:   
                return ("This drink is not in this recipe book yet :( Please update the recipe book if you would like to add this drink.")   
        
    def __str__(self):
        #loop that goes through each key
        for i in self.__recipes:
            #gets the ingredient list
            ingredients= self.__recipes[i]["Ingredients"]
            #prints the ingredient list for each key in the dictionary
            print(f"{i}\n\tINGREDIENTS:\n\t{ingredients}")
        
    def create_book(self):
        #writes a new file and stores it as the variable recipe_book
        with open("Festive_Drink_Recipes.txt","w") as recipe_book:
            #writes message onto first line
            recipe_book.write("Welcome to the Festive Drink Recipe book. Here you can find all the ingredients to make the perfect holiday drink!")
            #does two new lines before next message
            recipe_book.write("\n\nTable of contents:")
            #creates loop for each key
            for drink in self.__recipes.keys():
                #writes out the name of the drinks with a new line seperating them and tabbed underneath the other message
                recipe_book.writelines(f"\n\t{drink}")
                #does an identical loop
            for drink in self.__recipes.keys():
                #writes out the name and ingredient list if each drink seperated by new lines and tabs
                recipe_book.writelines(f"\n\n{drink}\n\t{Drink_Recipe_Book.get_recipe(self, drink)}")

def main():
    x=Drink_Recipe_Book()
    # print(x.get_recipe(drink))
    # print(x.get_drink_list())
    # print(x.set_new_recipe(new_drink))
    # print(x.set_added_instructions(drink,instructions))
    print(x.__str__())
    # print(x.create_book())
  

if __name__== "__main__":
    main() 
