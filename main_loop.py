from account import *
from teamfunctions import *
from other_functions import *

def main_loop(team):
    menu_1 = f"\n1.manage your menu.\n2.manage your refrigerator\n3.order dish\n4.recommend dish\n5.exit\n6.help\nPlease input the number of the instruction: "
    menu_menu = f"\n1.add dish\n2.delete dish\n3.update your dish\n4.view your menu\n5.go back to main menu\n6.help\nPlease input the number of the instruction: "
    menu_refrigerator = f"\n1.add ingredient\n2.use ingredient\n3.check ingredients in refrigerator\n4.go back to main menu\n5.help\nPlease input the number of the instruction: "
    
    while True:
        menu_1_command = input(menu_1).strip()
        
        if menu_1_command == "1":#turn to menu manage
            while True:
                menu_menu_command = input(menu_menu).strip()
                
                if menu_menu_command == "1": #add dish
                    while True:
                        dishname = input("What is the name of your dish? ")
                        dish_ingredients = input("What is it made of? (Please separate ingredients with commas) ")
                        add_successfully = team.add_dish(dishname,dish_ingredients)
                        if add_successfully:
                            break
                
                elif menu_menu_command == "2":#delete dish
                    while True:
                        dishname = input("Which dish you want to delete? ")
                        delete_successfully = team.delete_dish(dishname)
                        if delete_successfully:
                            break        
                
                elif menu_menu_command == "3":#update your menu
                    while True:
                        dishname = input("Which dish you want to update? ")
                        dish_new_ingredients = input("What is its new formula? (Please separate ingredients with commas) ")
                        upgrate_successfully = team.update_dish(dishname,dish_new_ingredients)
                        if upgrate_successfully:
                            break
                
                elif menu_menu_command == "4":#view your menu
                    team.print_user_menu()
                
                elif menu_menu_command == "5":#exit to main menu
                    break
                
                elif menu_menu_command == "6":#help
                    print(f"\nCommand list\n1.add dish\n2.delete dish\n3.upgrate your menu\n4.view your menu\n5.go back to main menu\n6.help\n")
                
                else:
                    print("Invalid command. Please try again.\n")

        elif menu_1_command == "2":#turn to refrigerator manage
            while True:
                menu_refrigerator_command = input(menu_refrigerator).strip()
                if menu_refrigerator_command == "1": #add ingredient
                    new_ingredients = input("What did you buy that you want to put in the refrigerator?(Please separate ingredients with commas) ")
                    team.add_ingredent_refrigerator(new_ingredients)
                
                elif menu_refrigerator_command == "2":#delete ingredient
                    while True:
                        used_ingredient = input("which ingredient you want to use?(only delete one by one) ")
                        used_successfully = team.use_ingredent_refrigerator(used_ingredient)
                        if used_successfully:
                            break
                
                elif menu_refrigerator_command == "3":#check ingredients in refrigerator
                    team.check__ingredent_refrigerator()
                
                elif menu_refrigerator_command == "4":#exit
                    break
                
                elif menu_refrigerator_command == "5":#help
                    print(f"\nCommand list\n1.add ingredient\n2.use ingredient\n3.check ingredients in refrigerator\n4.go back to main menu\n5.help\n")
                
                else:
                    print("Invalid command. Please try again.\n")
        
        elif menu_1_command == "3":#order dish
            team.order_dish()
        
        elif menu_1_command == "4":#recommend dish
            dish_dict = team.recommend_dish()
            if dish_dict:
                show_recommend_window(dish_dict)
            else:#no recommend
                print("There is not enough food in your refrigerator to recommend any dish. How about going to resturant?\n")
        
        elif menu_1_command == "5":#exit
            print("Thank you for using Couple's Kitchen Menu System. Goodbye!\n")
            exit()
        
        elif menu_1_command == "6":#help
            print(f"\nCommand list\n1.manage your menu.\n2.manage your refrigerator\n3.order dish\n4.recommend dish\n5.exit\n6.help\n")
        
        else:
            print("Invalid command. Please try again.\n")
