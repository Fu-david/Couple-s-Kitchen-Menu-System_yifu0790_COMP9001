
# Couple's Kitchen Menu System

A collaborative menu management system designed for couples to share recipes, manage ingredients, and order dishes from each other's menus.

## Overview

Couple's Kitchen Menu System is a Python-based application that allows two users to form a team, create personalized menus, manage a shared refrigerator, and coordinate meal planning together. The system features a command-line interface with GUI pop-up windows for order notifications and recipe recommendations.

## Features

1. **Team Formation**: Register accounts and form teams with your partner.  
2. **Personal Menus**: Each team member maintains their own dish recipes.  
3. **Shared Refrigerator**: Track ingredients available to both team members.  
4. **Dish Ordering**: Order dishes from your partner's menu.  
5. **Smart Recommendations**: Get dish suggestions based on available ingredients.  
6. **Order Notifications**: Receive GUI notifications when your partner orders dishes.  
7. **Recipe Links**: Automatic recipe lookup links for dishes not in your menu.

## Requirements

- Python  
- PyQt5  
- tkinter  
- json

## File Structure

```
.
├── main.py                  # Main entry point
├── main_loop.py            # Main program loop and menu system
├── account.py              # User authentication and team management
├── teamfunctions.py        # Core team functionality (menu, refrigerator)
├── other_functions.py      # GUI windows and helper functions
│
├── account_list.json       # User account data (auto-generated)
├── {teamname}_{username}_menu.json       # Individual user menus (auto-generated)
├── {teamname}_refrigerator.json          # Shared refrigerator (auto-generated)
└── {username}_ordered_dish.json          # Order notifications (auto-generated)
```

Demo files for testing:  
- `account_list.json`  
- `loveFamily_david_menu.json`  
- `loveFamily_refrigerator.json`  
- `sam_ordered_dish.json`


## ---------------- Getting Started ----------------
### 1️⃣ Run the Program

--> python main.py

### 2️⃣ Register or Login

- Choose Register to create a new account.
- Choose Login to access your existing account.
- Choose Exit to quit.

### 3️⃣ Form a Team

- 📲On first login, you'll be prompted to form a team:
- 	Enter your teammate's username.
- 	Choose a unique team name.
- 	Wait for your teammate to accept the invitation.

### 4️⃣ Main Menu Options
📌Once logged in, and ❗️after you have completed the team formation❗️
👀you can:

#### 1.🌟 Manage Your Menu 📖:
1. Add new dishes with ingredients.
2. Delete existing dishes.
3. Update dish recipes.
4. View your complete menu.


#### 2.🌟 Manage Your Refrigerator ❄️:

1. Add ingredients (comma-separated).
2. Remove used ingredients.
3. Check current inventory.


#### 3.🌟 Order Dish 🍽️:

1. Browse your partner's menu.
2. Order dishes they've created.
3. Request dishes not in their menu.


#### 4.🌟 Recommend Dish 🍱:

1. Get smart suggestions based on available ingredients.
2. See what ingredients you need to buy.
3. Interactive GUI for browsing recommendations.


#### 5.🌟 Exit:

- 👋 Save and quit the program.


#### 6.🌟 Help

- 🆘 View command list for current menu.


## ---------------- Usage Explanation ----------------
### 1️⃣ About order message:
💗  After you read it,  you just need to click the cross in the upper right corner to close the window and then you can enter the system.

### 2️⃣ Manage dishes in your menu
#### 🔺 add dish:
- What is the name of your dish?  (Enter the name, like Chinese hot pot)
- What is it made of? (Please separate ingredients with commas) (Enter the ingredients, like tomato, egg, milk, noodles)
 
#### 🔺 update dish: (Update ingredients)
- Which dish you want to update? (Enter the name, like Chinese hot pot)
- What is its new formula? (Please separate ingredients with commas) (Enter the ingredients, like tomato, egg, milk, noodles)

#### 🔺 delete dish:
- Which dish you want to delete?  (Enter the dish name, like Chinese hot pot)

### 3️⃣ Manage refrigerator
#### 🔺 add ingredient
- What did you buy that you want to put in the refrigerator?(Please separate ingredients with commas) (Enter the ingredients, like tomato, egg, milk, noodles)
#### 🔺 add ingredient
- which ingredient you want to use?(only delete one by one) (Enter the ingredients, like tomato, egg, milk, noodles)

### 4️⃣ order dishes 
#### 🔺 You can choose to order the dishes that exist in the menu or other dishes that do not exist in the menu

### 5️⃣recommend dishes
#### 🔺 It will pop-up a window, there are two buttons on the window, one is “yes” and another one is “no”. 
#### 🔺 If you click “yes”, it will show you what ingredients you need to buy, and also there is a button “ok”, and then you press “ok”, it will go back to main menu.
#### 🔺 If you click “no”, it will show the next recommendation until all recommendations are shown. If all the recommendations have been shown, it will go back to main menu.


## ---------------- Key Features Explained ----------------
### 1️⃣ Team System

🔴 Each user can only be part of one team.

🔴 Team names must be unique.

🔴 Both members share the same refrigerator.

🔴 Each member maintains their own menu.

🔴 Message system for team invitations.


### 2️⃣ Order Notifications
#### 📝When your partner orders dishes from your menu:

🔴 A pop-up window shows all ordered dishes.

🔴 Missing ingredients are highlighted .

🔴 Recipe links provided for unknown dishes .

🔴 Links are clickable and open in default browser.

🔴 Order file is automatically deleted after viewing.

############################## Example notification:##############################

💗💗💗 sam ORDER 🌹🌹🌹
1. mapo tofu LACK❌: ground pork, doubanjiang, Sichuan peppercorn, ginger, stock
2. fried rice lack nothing.
3. caesar salad LACK❌: romaine lettuce, croutons, Caesar dressing



Your teammate ordered 2 dishes that are not in your menu.
1. Tuna sushi  cooking recipe link 🖥️ : https://www.allrecipes.com/search?q=Tuna+sushi
2. durian pizza  cooking recipe link 🖥️ : https://www.allrecipes.com/search?q=durian+pizza

##################################################################################


### 3️⃣ Smart Recommendations
#### 💖The recommendation system:

🟠 Analyzes your menu and refrigerator contents.

🟠 Suggests dishes where you have ≥1/3 of ingredients.

🟠 Shows missing ingredients for each recommendation.

🟠 Presents suggestions in an interactive GUI.

🟠 Calculates based on ingredient matching threshold.

#### Example: 
- If a dish needs 9 ingredients and you have 3, it will be recommended (3/9 ≥ 1/3).
- If a dish needs 5 ingredients and you have 2, it will be recommended (2/5 ≥ 1/3).


### 4️⃣ Ingredient Management

🟡 All ingredients are stored in lowercase.

🟡 Automatic deduplication when adding to refrigerator.

🟡 Comma-separated input for multiple ingredients.

🟡 Shared between team members.

🟡 Uses symmetric difference for updates.

#### ‼️Tip:

❗️ Use descriptive dish names for better organization.

❗️ Keep your ingredient names consistent (e.g., always use "tomato" not "tomatoes").

❗️ Regularly update your refrigerator inventory.

❗️ Check order notifications when you log in.

❗️ Use the recommendation feature when unsure what to cook.

❗️ Test with sample accounts to understand the workflow.

❗️ The more dishes in your menu, the better the recommendations work.


## ---------------- Troubleshooting ----------------
### 1️⃣ Login fails after 3 attempts

🔺 The program will exit for security

🔺 Restart and try again or register a new account

### 2️⃣ "Teammate has already formed a team"

🔺 Your teammate is already in another team

🔺 Choose a different teammate

### 3️⃣ Empty menu or refrigerator

🔺 No data exists yet - start adding items

🔺 JSON files may not be created until first save

🔺 Use test accounts ("david"/"sam") to see sample data

### 4️⃣ GUI windows not appearing

🔺 Ensure PyQt5 and tkinter are properly installed

🔺 Check if windows are behind other applications

### 5️⃣ Order notification not showing

🔺 Order file is deleted after first view

🔺 Partner must create a new order

🔺 Check for {username}_ordered_dish.json file

### 6️⃣ "Dish not found in menu"

🔺 Dish names are case-insensitive

🔺 Check spelling carefully

🔺 Use 'menu' command to view available dishes


## ---------------- Data Storage ----------------
### 💾 The system automatically creates and manages JSON files:
account_list.json	-->	All user accounts and team information

{teamname}_{username}_menu.json	-->	Individual user menus

{teamname}_refrigerator.json	-->	Shared refrigerator contents

{username}_ordered_dish.json	-->	Temporary order notifications

### JSON File Formats
##### 1🗃️. Account List Structure:
```
[{
    "username": "string",
    "password": "string",
    "teamname": "string",
    "teammate": "string",
    "message": "string"  // Team invitation or notification messages
},
{
......
},
...]
```
##### 2🗃️. Menu Structure:
```
{
    "dish_name1": ["ingredient1", "ingredient2", "..."],
    "dish_name2": ["ingredient1", "ingredient2", "..."],...
}
```
##### 3🗃️. Refrigerator Structure:
```
["ingredient1", "ingredient2", "ingredient3","...",...]
```
##### 4🗃️. Order Structure:
```
{
    "dish_ordered_in": ["dish1", "dish2","...",...],      // From partner's menu
    "dish_ordered_other": ["dish3", "dish4","...",...]    // Custom requests
}
```

## ---------------- Technical Notes ----------------
🔹 All text data is stored in UTF-8 encoding

🔹 Ingredient matching is case-insensitive

🔹 The system uses symmetric difference (XOR) for refrigerator updates

🔹 Recipe links use AllRecipes search functionality

🔹 Recommendation threshold: minimum 1/3 of ingredients must be available

🔹 Order files are temporary and auto-deleted after viewing

🔹 Message system handles: team invitations, waiting status, rejection messages



--------------------------------------------------------

**Enjoy cooking together!** 👩🏻‍❤️‍💋‍👨🏻🍳

(Satisfying your girlfriend's stomach is the key to making your girlfriend meet your demands.) 
