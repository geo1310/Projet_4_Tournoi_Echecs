import os
players = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']
index = 0
os.system('cls')
while True:
    try:
        print(f"Match : {players[index]} - {players[index+1]}")
    except:
        print()
        break
    else:
        index += 2
