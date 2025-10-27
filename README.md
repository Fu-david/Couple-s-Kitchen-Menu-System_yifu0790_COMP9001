
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

...

**Enjoy cooking together!** 👩🏻‍❤️‍💋‍👨🏻🍳
