# Jacky Zhou
# Mr. David Park - ICS 4U
# 2024/05/29
# AOL 5 - user login system

# The first window include register function, login function
# After user login, it will create a new window, which include change password function, change screen size function, change bg color function

# import libraries
import tkinter as tk
import json

# Loading files
with open("user.json", "r+") as file:
    users = json.load(file)
with open("user_settings.json", "r") as file:
    settings = json.load(file)

#register user
def register_user(user_name,password):
    # Reset error
    output_variable.set("")
    output.grid_forget()
    for i in users["users"]:
        if user_name == i["username"]:
            output.grid(row=1, column=4, sticky="wnse", padx=10)
            output_variable.set("This user name has already exited, try another one")  # Change text
            output.config(bg="red")
            return
        elif user_name == "":
            output.grid(row=1, column=4, sticky="wnse", padx=10)
            output_variable.set("User name cannot be blanked")  # Change text
            output.config(bg="red")
            return
    # Register
    output.grid(row=3, column=4, sticky="wnse", padx=10)
    users["users"].append({"username":user_name,"password": password}) # update user info within codes
    with open("user.json", "w") as file:
        json.dump(users, file)                            # Change the info within file
    output_variable.set("Registered Success")  # Change text
    output.config(bg="light green")
    settings["settings"].append({"username":user_name,"bg_color": "light cyan","font":["Times New Roman", 26, "bold"], "geometry": "1000x600"})
    with open("user_settings.json", "w") as file:
        json.dump(settings, file)
# Login user
def login_user(user_name,password): # login system function
    # Reset error
    output_variable.set("")
    output.grid_forget()
    for i in users["users"]:
        if user_name == i["username"]:
            if password == i["password"]:
                output.grid(row=4, column=4, sticky="wnse", padx=10)
                output_variable.set("Login Success")   # Change text
                output.config(bg="light green")                      # Change color
                after_login(user_name)
                return
            else:
                output.grid(row=2, column=4, sticky="wnse", padx=10)
                output_variable.set("Password Incorrect") # Change text
                output.config(bg="red")  # Change color
                return
    # If it doesn't find the user's name, then the user's name doesn't exit
    output.grid(row=1, column=4, sticky="wnse", padx=10)
    output_variable.set("User Name Doesn't Exit")
    output.config(bg="red")     # Change color

def change_password(user_name,old_password,new_password):
    # Reset error
    output_variable_1.set("")
    output_1.config(bg = user_settings["bg_color"])
    output_1.grid_forget()
    # Find the password of login user's name
    for i in users["users"]:
        if user_name == i["username"]:
            user_old_password = i["password"]
            if user_old_password == new_password:
                output_1.grid(row=2, column=2, sticky="wnse", padx=10)
                output_variable_1.set("Old password cannot be same with the new password")
                output_1.config(bg="red")
                return
            elif user_old_password == old_password:
                output_1.grid(row=3, column=2, sticky="wnse", padx=10)
                # update info into the general user settings within the codes
                i["password"] = new_password
                output_variable_1.set("Password Change Success")  # Change text
                output_1.config(bg="light green")  # Change color
                # update info into the file
                with open("user.json" , "w") as file:
                    json.dump(users, file)
                return
    # Output error
    output_1.grid(row=1, column=2, sticky="wnse", padx=10)
    output_variable_1.set("Old Password Incorrect")  # Change text
    output_1.config(bg="red")  # Change color
# Change screen size function
def change_screen_size(screen_size,user_name):
    # Reset
    output_variable_1.set("")
    output_1.config(bg=user_settings["bg_color"])
    output_1.grid_forget()
    # Check if screen size is blanked
    if screen_size == "":
        output_1.grid(row=4, column=2, sticky="wnse", padx=10)
        output_1.config(bg="red")
        output_variable_1.set("The screen size cannot be nothing")
        return
    # Check if the screen size format is recognized by computer
    try:
        window_1.geometry(screen_size)
    except:
        output_1.config(bg="red")
        output_variable_1.set("The screen size format is incorrect")
        return
    # update info in personal user settings
    user_settings["geometry"] = screen_size
    # update info in general user settings
    for i in settings["settings"]:
        if user_name == i["username"]:
            i["geometry"] = user_settings["geometry"]
    # update info in the file
    with open("user_settings.json", "w") as file:
        json.dump(settings,file)
# Change background color
def change_screen_color(change_color,user_name):
    # Reset
    output_variable_2.set("")
    output_2.config(bg=user_settings["bg_color"])
    # Check if the color name is recognized by computer
    try:
        window_1.config(bg=change_color)
        output_2.config(bg=change_color)
    except:
        output_2.config(bg="red")
        output_variable_2.set("This color doesn't exit in library")
        return
    # update info in personal user settings
    user_settings["bg_color"] = change_color
    # update info in general user settings
    for i in settings["settings"]:
        if user_name == i["username"]:
            i["bg_color"] = user_settings["bg_color"]
    # update info in file
    with open("user_settings.json", "w") as file:
        json.dump(settings,file)
def after_login(user_name):
    # make sure other function can use all of the variables
    global output_variable_1 , output_1, output_2
    global window_1
    # Reset the previous typing and error
    user_old_password.set("")
    user_new_password.set("")
    change_color.set("")
    screen_size.set("")
    output_variable_1.set("")
    output_variable_2.set("")

    # create personal user settings
    for i in settings["settings"]:
        if user_name == i["username"]:
            global user_settings
            user_settings = i
    # Create a connected window to previous window
    window_1 = tk.Toplevel(window)
    # Showing custom settings
    window_1.title(user_settings["username"])
    window_1.geometry(user_settings["geometry"])
    window_1.config(bg=user_settings["bg_color"])
    # Output define
    output_1 = tk.Label(window_1, textvariable=output_variable_1, bg=user_settings["bg_color"],
                    font=("Times New Roman", 16, "bold"))  # set a combing output label
    output_2 = tk.Label(window_1,textvariable=output_variable_2,bg=user_settings["bg_color"], font=("Times New Roman", 16, "bold"))
    # Title
    title_label_1 = tk.Label(window_1, text=f"{user_settings["username"]}'s window", font=("Times New Roman", 26, "bold"))
    # Change password
    old_password_entry = tk.Entry(window_1, textvariable=user_old_password, font=("Times New Roman", 16, "bold"),show="*")
    new_password_entry = tk.Entry(window_1, textvariable=user_new_password, font=("Times New Roman", 16, "bold"), show="*")
    old_password_label = tk.Label(window_1, text="old password:", bg="gray",font=("Times New Roman", 16, "bold"))
    new_password_label = tk.Label(window_1, text="new password:", bg="gray",font=("Times New Roman", 16, "bold"))
    change_password_button = tk.Button(window_1, text="Change Password", command= lambda :change_password(user_name,old_password=user_old_password.get(),new_password=user_new_password.get()), font=("Times New Roman", 16, "bold"))
    # Exit
    exit_button_1 = tk.Button(window_1, text="Exit", command=window_1.destroy, font=("Times New Roman", 16, "bold"))
    # Change screen size
    screen_size_entry = tk.Entry(window_1, textvariable=screen_size, font=("Times New Roman", 16, "bold"))
    change_screen_size_button = tk.Button(window_1, text="Change Screen Size", font=("Times New Roman", 16, "bold"),command=lambda :change_screen_size(screen_size.get(),user_name))
    screen_size_label = tk.Label(window_1, text="Screen Size(ex. 800x600):", font=("Times New Roman", 16, "bold"), bg="gray")
    # Change screen color
    change_color_entry = tk.Entry(window_1,textvariable=change_color, font=("Times New Roman", 16, "bold"))
    change_screen_color_button = tk.Button(window_1, text="Change Background Color", font=("Times New Roman", 16, "bold"),command=lambda: change_screen_color(change_color.get(), user_name))
    change_color_label = tk.Label(window_1, text="Color Change:", font=("Times New Roman", 16, "bold"), bg="gray")

    # Grid
        # Title
    title_label_1.grid(row=0,column=1, sticky="wnse",pady=10)
        # Change password
    old_password_label.grid(row=1, column=0, sticky="wnse", padx=10)
    new_password_label.grid(row=2, column=0, sticky="wnse", padx=10)
    old_password_entry.grid(row=1, column=1, sticky="wnse", padx=10)
    new_password_entry.grid(row=2, column=1, sticky="wnse", padx=10)
    change_password_button.grid(row=3, column=1, sticky="wnse", padx=10,pady=10)
        # Change screen Size
    screen_size_label.grid(row=4, column=0, sticky="wnse", padx=10)
    screen_size_entry.grid(row=4, column=1, sticky="wnse", padx=10)
    change_screen_size_button.grid(row=5, column=1, sticky="wnse", padx=10,pady=10)
        # Change screen color
    change_color_label.grid(row=6, column=0, sticky="wnse", padx=10)
    change_color_entry.grid(row=6, column=1, sticky="wnse", padx=10)
    change_screen_color_button.grid(row=7, column=1, sticky="wnse", padx=10,pady=10)
        # Exit window
    exit_button_1.grid(row=8, column=1, sticky="wnse", padx=10,pady=20)
        # An output only for change color function, since gird_forget can only apply two objects
    output_2.grid(row=6, column=2, sticky="wnse", padx=10)
    # mainloop
    window_1.mainloop()

# The first window
# Initializing - create a window, name the title, set the size of the window
window = tk.Tk()
window.title("User Login System")
window.geometry("1200x600")
window.configure(bg="light cyan")

# Variables
# First window variables
# Login system function's arguments
user_name = tk.StringVar()
password = tk.StringVar()
output_variable = tk.StringVar()  # set a text variable that can be changed if user typing correct or wrong
output_color = tk.StringVar()
# Second window variables
user_old_password = tk.StringVar()
user_new_password = tk.StringVar()
screen_size = tk.StringVar()
change_color =tk.StringVar()
output_variable_1 = tk.StringVar()  # set a text variable that can be changed if user typing correct or wrong
output_variable_2 = tk.StringVar()

# Title
title = tk.Label(window, text = "Welcome To User Login System",bg = "skyblue",font = ("Times New Roman", 26, "bold"))
# Label
user_name_label = tk.Label(window, text="User Name Login/Create A User Name:",bg = "skyblue",font = ("Times New Roman", 16, "bold"))
password_label = tk.Label(window, text="Password Login/Create A Password:",bg = "skyblue",font = ("Times New Roman", 16, "bold"))
# User's name entry - let user type the exited user's name to log in
user_name_entry = tk.Entry(window, textvariable = user_name, font = ("Times New Roman", 16, "bold"))
# Password entry - let user type the correct password to log in
password_entry = tk.Entry(window, textvariable = password, font = ("Times New Roman", 16, "bold"), show = "*")
# Login button - process login function
login_button = tk.Button(window,text = "Sign in",command = lambda: login_user(user_name.get(),password.get()), font = ("Times New Roman", 16, "bold"))  # lambda: makes the function can get arguments
# Registered button - register new account function
register_button = tk.Button(window, text = "Sign up", command = lambda : register_user(user_name.get(),password.get()), font = ("Times New Roman", 16, "bold"))
# Exit program button
exit_button = tk.Button(window, text = "Exit", command = window.destroy, font = ("Times New Roman", 16, "bold"))
# output
output = tk.Label(window, textvariable=output_variable, bg="light cyan",font=("Times New Roman", 16, "bold"))  # set a combing output label


# Putting all the things on the screen
title.grid(row=0,column=1,padx=10,pady=10)
user_name_entry.grid(row=1,column=1,sticky='wnse',padx=1,pady=5)
password_entry.grid(row=2,column=1,sticky='wnse',padx=1,pady=5)
login_button.grid(row=3,column=1,sticky="wnse",padx=10)
register_button.grid(row=4, column=1, sticky="wnse",padx=10)
exit_button.grid(row=5, column=1,sticky="wnse",padx=10,pady=20)
user_name_label.grid(row=1,column=0,sticky='wnse',padx=1,pady=5)
password_label.grid(row=2,column=0,sticky='wnse',padx=1,pady=5)

# Mainloop - make sure the window keep showing on the screen
window.mainloop()
