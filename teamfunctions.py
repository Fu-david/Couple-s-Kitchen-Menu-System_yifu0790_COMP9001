import json
import math

class Team_login:
    def __init__(self, username:str, teamname:str, teammate:str) :
        self.username = username
        self.teamname = teamname
        self.teammate = teammate
        
        self.menu_user = {} # dish : [ingredents]
        self.refrigerator = [] #ingredents list
        self.menu_teammate = {} # dish : [ingredents]
        
        self.order_dish_dictionary = {} # dish_ordered_in : [] , dish_ordered_other : []
    
    def __str__(self) -> str:
        return f"teamname: {self.teamname}, member: {self.username} , {self.teammate}"
    
    def inittialize_menu_and_refrigerator(self): #load ....... 初始化
        file_name_menu_user = f"{self.teamname}_{self.username}_menu.json" 

        file_name_menu_teammate = f"{self.teamname}_{self.teammate}_menu.json"
        
        file_name_refrigerator = f"{self.teamname}_refrigerator.json"
        #print(file_name_menu_user)
        #print(file_name_menu_teammate)
        #print(file_name_refrigerator)
        try:  
            with open(file_name_menu_user, 'r', encoding='utf-8') as f:
                self.menu_user = json.load(f)
        except FileNotFoundError:
            self.menu_user = {}
        try:   
            with open(file_name_menu_teammate, 'r', encoding='utf-8') as f:
                self.menu_teammate = json.load(f)
        except FileNotFoundError:
            self.menu_teammate = []
        try:
            with open(file_name_refrigerator, 'r', encoding='utf-8') as f:
                self.refrigerator = json.load(f)
        except FileNotFoundError:
            self.refrigerator= {}
        print("Successfully load menu and refrigerator!\n")
        return self.menu_user, self.menu_teammate, self.refrigerator
        
    
    
    def add_dish(self,dish_name: str, ingredients: str):
        if dish_name.strip().lower() in self.menu_user:
            print("This dish already exists in your menu.\n")
            return False
        else:
            input_ingredients = ingredients.strip().split(",")
            ingredients_list = [item.strip().lower() for item in input_ingredients if item.strip()]
            self.menu_user[dish_name.strip().lower()] = ingredients_list
            print(F"{dish_name} successfully added to your menu.\n")

            file_name_menu_user = f"{self.teamname}_{self.username}_menu.json" 
            with open(file_name_menu_user, 'w+', encoding='utf-8') as f:
                json.dump(self.menu_user, f, ensure_ascii=False, indent=4)
            return True

    def delete_dish(self,dish_name:str):
        if dish_name.strip().lower() in self.menu_user:
            self.menu_user.pop(dish_name.strip().lower())
            print(f"{dish_name} is successfully deleted from your menu.\n")

            file_name_menu_user = f"{self.teamname}_{self.username}_menu.json" 
            with open(file_name_menu_user, 'w+', encoding='utf-8') as f:
                json.dump(self.menu_user, f, ensure_ascii=False, indent=4)
            return True
        else:
            print("This dish is not found in your menus.\n")
            return False

    def update_dish(self,dish_name:str, new_ingredients:list): #更新菜
        if dish_name.strip().lower() in self.menu_user:
            new_ingredients = new_ingredients.strip().split(",")
            ingredients_list = [item.strip().lower() for item in new_ingredients if item.strip()]
            self.menu_user[dish_name.strip().lower()] = ingredients_list
            print(F"{dish_name} is successfully updated.\n")

            file_name_menu_user = f"{self.teamname}_{self.username}_menu.json" 
            with open(file_name_menu_user, 'w+', encoding='utf-8') as f:
                json.dump(self.menu_user, f, ensure_ascii=False, indent=4)
            return True
        else:
            print(f"{dish_name} is not found in your menu.\n")
            return False

    def add_ingredent_refrigerator(self, ingredients: str): #可以加一列
        
        input_ingredients = ingredients.strip().split(",")
        ingredients_list = [item.strip().lower() for item in input_ingredients if item.strip()]
        self.refrigerator = sorted(set(self.refrigerator) ^ set(ingredients_list))
        print(f"{ingredients} succefully added to your refregerator.\n")

        file_name_refrigerator = f"{self.teamname}_refrigerator.json"
        with open(file_name_refrigerator, 'w+', encoding='utf-8') as f:
            json.dump(self.refrigerator, f, ensure_ascii=False, indent=4)
        return True
    
    def check__ingredent_refrigerator(self) ->list: 
        if self.refrigerator == []:
            print("Your refrigerator is empty!\n")
            return []
        else:
            print("Your refrigerator contains the following ingredients:")
            for ingredient in self.refrigerator:
                print(f"    {ingredient}")
            print()
            return self.refrigerator

    def use_ingredent_refrigerator(self, ingredent_name: str): #只能一个个减
        if ingredent_name.strip().lower() in self.refrigerator:
            self.refrigerator.remove(ingredent_name.strip().lower())
            print(f"{ingredent_name} is successfully deleted from your refrigerator.\n")

            file_name_refrigerator = f"{self.teamname}_refrigerator.json"
            with open(file_name_refrigerator, 'w+', encoding='utf-8') as f:
                json.dump(self.refrigerator, f, ensure_ascii=False, indent=4)
            return True
        else:
            print(f"{ingredent_name} is not found in your refrigerator.\n")
            return False

    def print_user_menu(self): #print your teammate --> order dish
        if len(self.menu_user) == 0:
            print("your menu is empty!\n")
            return 0,[]
        dish_list = []
        count = 0 
        for dish, ingredents in self.menu_user.items():
            count += 1
            print(f"{count}. {dish} : {','.join(ingredents)}")
            dish_list.append(dish)
        print()
        return count,dish_list


    def print_teammate_menu(self): #print your teammate --> order dish
        if len(self.menu_teammate) == 0:
            print("your teammate has no dish in the menu!\n")
            return 0,[]
        dish_list = []
        count = 0 
        for dish, ingredents in self.menu_teammate.items():
            count += 1
            print(f"{count}. {dish} : {','.join(ingredents)}")
            dish_list.append(dish)
        print()
        return count,dish_list

    def order_dish(self):
        if self.order_dish_dictionary == {}:
            dish_ordered_in = []
            dish_ordered_other = []
        else:
            dish_ordered_in = self.order_dish_dictionary['dish_ordered_in']
            dish_ordered_other = self.order_dish_dictionary['dish_ordered_other']

        print("menu:")
        count,dish_list = self.print_teammate_menu()
        if count == 0:
            #print("Your teammate has no dish in the menu to order.\n")
            return False
        while True:
            dish_name = input("please enter the dish name you want to order(enter 'end' to finish or 'other' to order the dish not in the menu)(if you forget the menu,enter'menu') ").strip()
            try:
                if dish_name.lower() == 'end':
                    break
                elif dish_name.lower() == 'menu':
                    print("menu:")
                    self.print_teammate_menu()
                elif dish_name.lower() == 'other':
                    other_dish = input("please enter the dish name you want to order: ").strip()
                    double_confirm = input(f"do you want to order {other_dish}?(yes/no) ").strip()
                    while True:
                        try:
                            if double_confirm.lower() == "yes":
                                dish_ordered_other.append(other_dish.strip())
                                print(f"You have successfully ordered {other_dish}.\n")
                                break
                            elif double_confirm.lower() == "no":
                                break
                        except TypeError:
                            print("Invalid input. Please enter 'yes' or 'no'.")
                elif dish_name.lower() in self.menu_teammate:
                    dish_ordered_in.append(dish_name.lower())
                    print(f"You have successfully ordered {dish_name}.\n")
                else:
                    print("Dish not found in the menu. Please try again.")
            except TypeError:
                print("Invalid input. Please try again.")
        #save
        self.order_dish_dictionary['dish_ordered_in'] = dish_ordered_in
        self.order_dish_dictionary['dish_ordered_other'] = dish_ordered_other
        if len(self.order_dish_dictionary['dish_ordered_in']) == 0 and len(self.order_dish_dictionary['dish_ordered_other']) == 0:
            return False
        
        filename_order_dish = f"{self.username}_ordered_dish.json"
        with open(filename_order_dish,'w+',encoding='utf-8') as f:
            json.dump(self.order_dish_dictionary,f,ensure_ascii=False,indent=4)
        print("Your order have been forwarded to your teammate!\n")
        return True

    def recommend_dish(self) -> dict:
        # 标准化冰箱材料并去重
        fridge_set = {x for x in self.refrigerator if isinstance(x, str)}

        recommendations = {}

        for dish_name, ingredients in self.menu_user.items():
            # 跳过非列表或空菜谱

            if not isinstance(ingredients, list) or len(ingredients) == 0:
                continue

            # 标准化原材料并去重
            ing_set = {x for x in ingredients if isinstance(x, str)}
            total = len(ing_set)
            if total == 0:
                continue

            # 计算匹配数量与阈值（至少三分之一）
            matched = len(ing_set & fridge_set)
            threshold = math.ceil(total / 3)

            if matched >= threshold:
                missing = sorted(list(ing_set - fridge_set))
                # 返回缺少的原材料
                recommendations[dish_name] = missing

        return recommendations # --> dish_name : missing ingredients list



#test
if __name__ == "__main__":
    t = Team_login("anson", "teamA", "joe")
    t.add_dish("pasta", ["noodles", "sauce", "cheese"])
