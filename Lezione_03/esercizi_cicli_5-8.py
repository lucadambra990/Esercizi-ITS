username:list[str] = ["Admin","Silvia","Luca","Matteo","Thomas"]
user:str = input("Log in: ")

if user=="Admin":
    print("Hello Admin, would you like to see a status report?")
if user !="Admin":
    print(f"Hello {user},thank you for logging in again!")