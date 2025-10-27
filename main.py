from main_loop import *

if __name__ == "__main__":
    print("welcome to Couple's Kitchen Menu System\n")

    login_True_False , username , teamname , teammate = main_login()
    if login_True_False:
        team = Team_login(username , teamname , teammate)
        team.inittialize_menu_and_refrigerator()

        #check order message
        message_T_F , content = show_order(teammate, username , teamname)
        if message_T_F:
            show_order_window(content)
        
        #main program loop
        main_loop(team)
        
        

