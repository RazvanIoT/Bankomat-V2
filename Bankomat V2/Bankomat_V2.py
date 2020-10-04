accounts = {}
balance = 0
accounts[balance] = 0
saldo = accounts[balance]

def RegisterAccount():
  kontonummer = int(input("Ange kontonumer>: "))
  while kontonummer < 1000 or kontonummer > 9999:
      kontonummer = int(input("\nErr0r.. Försök igen! "))
  if kontonummer in accounts:
        print("Konto redan finns. Försök igen!")
  else:
      accounts[kontonummer] = 0
      
      
def Withdraw():
  amt = int(input("Ange belopp> "))
  if amt > accounts[balance]:
      print("Err0r")
      ManageAccount()
  
 
def Saldo():
  print("Saldo: " + str(saldo))

  

def Deposit():
  amt = int(input("Ange belopp> "))
  saldo = accounts[balance]
  if amt > 0:
      print(f"Your new balance is: {saldo+amt}")



def ManageAccount():
  while True:
      kontonummer = int(input("Ange kontonumer>: "))
      if kontonummer not in accounts:
        print("Finns inte. Försök igen!")
      else:
        break;
  print("****KONTOMENY****")
  print("1. Ta ut pengar")
  print("2. Sätt in pengar")
  print("3. Visa saldo")
  print("4. Avsluta")
  selected = int(input("Ange menyval> "))
  if selected == 1:
    Withdraw()
  if selected == 2:
    Deposit()
  if selected == 3:
    Saldo()
  if selected == 4:
    print("\nGrattis. Dina pengar är borta.")
    
    
    
while True:
    print("****HUVUDMENY****")
    print("1. Skapa konto")
    print("2. Administrera konto")
    print("3. Avsluta")
    selected = int(input("Ange menyval> "))
    if(selected == 3):
        break;
    if(selected == 1):
        RegisterAccount()
    if(selected == 2):
        ManageAccount()
    

