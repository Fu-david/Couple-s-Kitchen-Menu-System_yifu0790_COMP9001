import json

def account_list_load():
    try:
        with open('account_list.json', 'r', encoding='utf-8') as f:
            account_list = json.load(f)
    except FileNotFoundError:
        account_list = [] # account information --> {username: , password:, teamname: , teammate: , message: <kind of message> <……>} 
    return account_list

def save_account_list(account_list): #save account list
    with open('account_list.json', 'w', encoding='utf-8') as f:
        json.dump(account_list, f, ensure_ascii=False, indent=4)




def login_test_n_p(username , password): # login fuction
    account_list = account_list_load()
    for account in account_list:
        if account["username"] == username and account["password"] == password:
            return True,account["teamname"],account["teammate"],account["message"]
    return False,False,False,False

def add_account(username, password): # add account
    account_list = account_list_load()
    account_information = {
        "username" : username,
        "password" : password,
        "teamname" : "",
        "teammate" : "",
        "message" : ""
    }
    account_list.append(account_information)
    save_account_list(account_list)
    return

def form_team(applicant_username): #apply a team
    account_list = account_list_load()
    for account in account_list:
        if account["username"] == applicant_username:
            if account["teamname"] != "":
                print("You have already formed a team")
                return False

    teammate_username = input("please enter your teammate's username:").strip()
    while True:
        teammate_username_error = False
        for account in account_list:        
            if account["username"] == teammate_username:
                if account['teamname'] != "":
                    print("Teammate has already formed a team")
                    teammate_username = input("please enter another Teammate:").strip()
                    teammate_username_error = True
                    break
                else:
                    teamname = input("please enter your team name:").strip()
                    while True:
                        count = 0
                        for account_1 in account_list:
                            if account_1["teamname"] == teamname:
                                print("Team name already taken")
                                teamname = input("please enter another team name:").strip()
                                break
                            else:
                                count += 1
                        if count == len(account_list):    
                            message = f"fromteam {applicant_username} {teamname}"
                            account["message"] = message
                            print("successfully send request! please wait for response.")
                            for account in account_list:
                                if account["username"] == applicant_username:
                                    message = f"waiting please waiting for {teammate_username} response"
                                    account["message"] = message
                            save_account_list(account_list)
                            return True
                    
        if not teammate_username_error:                
            print("Teammate account not found")
            teammate_username = input("please enter another Teammate:").strip()
    
def team_response(message,username): # respond to team invitation 
    account_list = account_list_load()
    if message.startswith("reject"):
        print(message[7:])
        for account in account_list:
            if account["username"] == username:
                account["message"] = ""
                save_account_list(account_list)
                break
        return False,""
    elif message.startswith("waiting"):
        print(message[8:])
        return False,""
    elif message.startswith("fromteam"):
        message_part = message.split(" ")
        applicant_username = message_part[1]
        teamname = message_part[2]
    elif message == "":
        return "",""
    
    while True:
        response = input(f"{applicant_username} invites you to join team {teamname}. Do you accept? (yes/no): ").strip()
        if response.lower() == "yes":
            task = 0
            for account in account_list:
                if account["username"] == username:
                    account["teamname"] = teamname
                    account["teammate"] = applicant_username
                    account["message"] = ""
                    task +=1
                if account["username"] == applicant_username:
                    account["teamname"] = teamname
                    account["teammate"] = username
                    account["message"] = ""
                    task +=1
                if task ==2:
                    break
            print("You have joined the team")
            save_account_list(account_list)
            return True,teamname
        elif response.lower() == "no":
            print("You have declined the invitation")
            message = f"reject {username} has declined your team invitation"
            for account in account_list:
                task =0
                if account["username"] == applicant_username:
                    account["message"] = message
                    task += 1
                if account["username"] == username:
                    account["message"] = ""
                    task += 1
                if task ==2:
                    break
            save_account_list(account_list)
            return False,""
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")


def main_login(): # main login function
    while True:
        action = input("Do you want to <Register, Login, Exit> ? ").strip()
        login_success = False
        if action ==  "register":
            username = input("Enter new username: ").strip()
            password = input("Enter new password: ").strip()
            print("Registration successful.")

        elif action.lower() == "login":
            for i in range(3):
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                login_success,teamname,teammate,message = login_test_n_p(username, password)
                if login_success:
                    print("successfully login!\n")
                    break 
                else:
                    print(f"wrong username or password, you have {2-i} chance left!")
                    if 2 - i ==  0:
                        return False,"","",""
            
        elif action.lower() == "exit":
            print("Exiting the program.")
            return False,"","",""
        else:
            print("Invalid option. Please try again.")

        if login_success:
            break
    
    team_response_T_F = False
    if message.startswith("reject") or message.startswith("waiting"):
        team_response_T_F , message = team_response(message,username)
    elif len(message) >0:
        team_response_T_F , teamname = team_response(message,username)

    if teamname == ""  and not team_response_T_F and not message.startswith("waiting"):
        want_to_form = input("Do you want to form a team?(yes/no)").strip().lower()
        while True:
            if want_to_form == "yes":
                form_team(username)
                return False,"","",""
            elif want_to_form == "no":
                return False,"","",""
            else:
                want_to_form = input("Invalid input. Do you want to form a team?(yes/no)").strip().lower()
    return True,username,teamname,teammate