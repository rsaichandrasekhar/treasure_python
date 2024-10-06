print("Welcome to treasure island ")
choice=input("Choose left or right ").lower()
if(choice=='left'):
  print("NICE CHOICE SHERLOCK!!")
  choice2=input("swim or wait ").lower()
  if(choice2=='wait'):
    print("NICE CHOICE BATMAN!!")
    choice3=input("Pick a door [red, blue, yellow] ").lower()
    if choice3=='yellow':
      print("YOU WIN. YOU ARE GOD. GOD IS GREAT. WINNER!!!")
    elif choice3=='blue':
      print("YOU WERE EATEN BY DEMONS. game over. LOSER!!!")
    else:
      print("YOU KILLED YOURSELF. game over. LOSER!!!")
  else:
    print("ATTACKED BY A TROUT!!! game over. LOSER!!!")
else:
  print("FELL INTO A HOLE!!!! game over. LOSER!!!")
