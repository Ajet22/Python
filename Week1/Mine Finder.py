print("  Welcome to Mine finder game  \n    Have Fun with it   ")
import random
import time

print('''
  __   __  ___   __    _  _______          _______  ___   __    _  ______   _______  ______   
|  |_|  ||   | |  |  | ||       |        |       ||   | |  |  | ||      | |       ||    _ |  
|       ||   | |   |_| ||    ___|        |    ___||   | |   |_| ||  _    ||    ___||   | ||  
|       ||   | |       ||   |___         |   |___ |   | |       || | |   ||   |___ |   |_||_ 
|       ||   | |  _    ||    ___|        |    ___||   | |  _    || |_|   ||    ___||    __  |
| ||_|| ||   | | | |   ||   |___         |   |    |   | | | |   ||       ||   |___ |   |  | |
|_|   |_||___| |_|  |__||_______|        |___|    |___| |_|  |__||______| |_______||___|  |_|
''')

# Map creation with using list
line1 = ["⬜️", "️⬜️", "️⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "️⬜️", "️⬜️", "️⬜️", "️⬜️"]
line3 = ["⬜️", "️⬜️", "️⬜️", "️⬜️", "️⬜️"]
line4 = ["⬜️", "️⬜️", "️⬜️", "️⬜️", "️⬜️"]
line5 = ["⬜️", "️⬜️", "️⬜️", "️⬜️", "️⬜️"]

map = [line1, line2, line3, line4, line5]
print("This is the actual MAP\n")
print("    A     B     C     D     E")
print(f"1{line1}\n2{line2}\n3{line3}\n4{line4}\n5{line5}\n\n")
#Getting user input
position = input("Please enter value for row and column for finding Mine\n")
if len(position) == 2:
  letter = position[0].lower()
  abc = ["a", "b", "c", "d", "e"]
  if letter in abc and position[1].isdigit() and int(position[1]) < 6 and int(
      position[1]) > 0:

    letter_index = abc.index(letter)
    number_index = int(position[1]) - 1

    if letter_index < 5 and number_index < 5:
      map[number_index][letter_index] = " X"

      # Map based on user input
      print(f"\n{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n")

      print(
          f"\n\nLets find out Mine is present  in the position {position} or not\n"
      )

      time.sleep(5)

      # Random Mine position

      list = ["A", "B", "C", "D", "E"]
      random_letter = random.randint(0, 4)
      random_number = random.randint(0, 4)
      map[random_number][random_letter] = " M"
      mine_position = list[random_letter] + str(random_number + 1)

      print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n")
      print("\n\nMine is present in the position " + mine_position + "\n\n")

      if position[0] == mine_position[0]:
        if position[1] == mine_position[1]:
          print("You found Mine \n \n You Win \n\n")
        else:
          print("Just Miss \n\n try again !\n\n")
      else:
        print("Mine exploded \n\n You Lose\n\n")
    else:
      print("Please enter valid input")
  else:
    print("Please enter valid input")

else:
  print("Please enter valid input with proper length")
