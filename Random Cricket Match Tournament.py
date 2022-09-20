import pandas as pd
import random
import time


print("------- Welcome to ICC T20 Cricket World Cup 2022 ! -------")
# time.sleep(3)
print('\nYou are allowed to change team and player profiles before the start of the tournament!\n')
# time.sleep(3)

Sri_Lanka = pd.read_excel("Z:\Desktop\CW\GroupA\Sri_Lanka.xlsx")
India = pd.read_excel("Z:\Desktop\CW\GroupA\India.xlsx")
Pakistan = pd.read_excel("Z:\Desktop\CW\GroupA\Pakistan.xlsx")
Australia = pd.read_excel("Z:\Desktop\CW\GroupA\Australia.xlsx")
New_Zealand = pd.read_excel("Z:\Desktop\CW\GroupB\_New_Zealand.xlsx")
England = pd.read_excel("Z:\Desktop\CW\GroupB\England.xlsx")
South_Africa = pd.read_excel("Z:\Desktop\CW\GroupB\South_Africa.xlsx")
West_Indees = pd.read_excel("Z:\Desktop\CW\GroupB\West_Indees.xlsx")



def editSriLanka():
    print(Sri_Lanka)
    row = int(input("\nEnter the row number for your edit: "))
    column = input("Enter the column name for your edit: ")
    value = input("Enter the new value here:  ")
    df = Sri_Lanka
    df.at[row, column] = value
    df.to_excel("Z:\Desktop\CW\GroupA\Sri_Lanka.xlsx", index=False)
    print(df)
    print("\nYou have edited successfully!")

def editIndia():
    print(India)
    df = India
    row = int(input("\nEnter the row number for your edit: "))
    column = input("Enter the column name for your edit: ")
    value = input("Enter the new value here:  ")
    df.at[row, column] = value
    df.to_excel("Z:\Desktop\CW\GroupA\India.xlsx", index=False)
    print(df)
    print("\nYou have edited successfully!")

def editPakistan():
    print(Pakistan)
    df = Pakistan
    row = int(input("\nEnter the row number for your edit: "))
    column = input("Enter the column name for your edit: ")
    value = input("Enter the new value here:  ")
    df.at[row, column] = value
    df.to_excel("Z:\Desktop\CW\GroupA\Pakistan.xlsx", index=False)
    print(df)
    print("\nYou have edited successfully!")

def editAustralia():
    print(Australia)
    df = Australia
    row = int(input("\nEnter the row number for your edit: "))
    column = input("Enter the column name for your edit: ")
    value = input("Enter the new value here:  ")
    df.at[row, column] = value
    df.to_excel("Z:\Desktop\CW\GroupA\Australia.xlsx", index=False)
    print(df)
    print("\nYou have edited successfully!")

def editNewZealand():
    print(New_Zealand)
    df = New_Zealand
    row = int(input("\nEnter the row number for your edit: "))
    column = input("Enter the column name for your edit: ")
    value = input("Enter the new value here:  ")
    df.at[row, column] = value
    df.to_excel("Z:\Desktop\CW\GroupB\_New_Zealand.xlsx", index=False)
    print(df)
    print("\nYou have edited successfully!")

def editEngland():
    print(England)
    df = England
    row = int(input("\nEnter the row number for your edit: "))
    column = input("Enter the column name for your edit: ")
    value = input("Enter the new value here:  ")
    df.at[row, column] = value
    df.to_excel("Z:\Desktop\CW\GroupB\England.xlsx", index=False)
    print(df)
    print("\nYou have edited successfully!")

def editSouthAfrica():
    print(South_Africa)
    df = South_Africa
    row = int(input("\nEnter the row number for your edit: "))
    column = input("Enter the column name for your edit: ")
    value = input("Enter the new value here:  ")
    df.at[row, column] = value
    df.to_excel("Z:\Desktop\CW\GroupB\South_Africa.xlsx", index=False)
    print(df)
    print("\nYou have edited successfully!")

def editWestIndees():
    print(West_Indees)
    df = West_Indees
    row = int(input("\nEnter the row number for your edit: "))
    column = input("Enter the column name for your edit: ")
    value = input("Enter the new value here:  ")
    df.at[row, column] = value
    df.to_excel("Z:\Desktop\CW\GroupB\West_Indees.xlsx", index=False)
    print(df)
    print("\nYou have edited successfully!")


print('Do you want to edit team/player profiles?')

e=1
while e==1:
     try:
         edit_profiles = int(input('If YES enter 1. If NO enter 0\n: '))
         e=2
     except ValueError:
         print('Invalid input!')
         print(ValueError)
         e=1
     else:
         if edit_profiles == 1:
             pass
         elif edit_profiles == 0:
             pass
         else:
              print('Invalid input!')
              e=1


while edit_profiles == 1:
      try:
         edit_team =int(input('\n1.Sri Lanka'
                              '\n2.India'
                              '\n3.Pakistan'
                              '\n4.Australia'
                              '\n5.New Zealand'
                              '\n6.England'
                              '\n7.South Africa'
                              '\n8.West Indees'
                              '\nEnter the team number to go forward & edit'
                              '\nEnter 0 if you have done your edit\n: '))

         if edit_team == 1:
             EditAgain = 1
             while EditAgain == 1:
                editSriLanka()
                EditAgain = int(input('Enter 1 to continue editing in the same team. Enter 0 to SKIP : '))

         elif edit_team == 2:
             EditAgain = 1
             while EditAgain == 1:
                 editIndia()
                 EditAgain = int(input('Enter 1 to continue editing in the same team. Enter 0 to SKIP : '))

         elif edit_team == 3:
             EditAgain = 1
             while EditAgain == 1:
                 editPakistan()
                 EditAgain = int(input('Enter 1 to continue editing in the same team. Enter 0 to SKIP : '))

         elif edit_team == 4:
             EditAgain = 1
             while EditAgain == 1:
                 editAustralia()
                 EditAgain = int(input('Enter 1 to continue editing in the same team. Enter 0 to SKIP : '))

         elif edit_team == 5:
             EditAgain = 1
             while EditAgain == 1:
                 editNewZealand()
                 EditAgain = int(input('Enter 1 to continue editing in the same team. Enter 0 to SKIP : '))

         elif edit_team == 6:
             EditAgain = 1
             while EditAgain == 1:
                 editEngland()
                 EditAgain = int(input('Enter 1 to continue editing in the same team. Enter 0 to SKIP : '))

         elif edit_team == 7:
             EditAgain = 1
             while EditAgain == 1:
                 editSouthAfrica()
                 EditAgain = int(input('Enter 1 to continue editing in the same team. Enter 0 to SKIP : '))

         elif edit_team == 8:
             EditAgain = 1
             while EditAgain == 1:
                 editWestIndees()
                 EditAgain = int(input('Enter 1 to continue editing in the same team. Enter 0 to SKIP : '))

         elif edit_team == 0:
             edit_profiles = 0

         else:
              print('Invalid input! Please enter the correct team number.')

      except ValueError:
          print('Invalid input! Only numbers are allowed.')
          pass



if edit_profiles == 0:
    print("Now you can't change player/team profiles. ")
    x = 1
    while x==1:

      try:
        tournament = int(input("Enter 1 to start the tournament. Enter 0 to Exit.\n: "))
        x = 2

      except ValueError:
        x = 1
        print('Wrong input!')
        print(ValueError)


if tournament == 0:
    pass

matchNO = 0
#tournament = 1
while tournament == 1:

 groupA = {'Sri Lanka' : "Z:\Desktop\CW\GroupA\Sri_Lanka.xlsx",
          'India' : "Z:\Desktop\CW\GroupA\India.xlsx",
          'Pakistan' : "Z:\Desktop\CW\GroupA\Pakistan.xlsx",
          'Australia' : "Z:\Desktop\CW\GroupA\Australia.xlsx"}

 groupB = {'New Zealand' : "Z:\Desktop\CW\GroupB\_New_Zealand.xlsx",
          'England' : "Z:\Desktop\CW\GroupB\England.xlsx",
          'South Africa' : "Z:\Desktop\CW\GroupB\South_Africa.xlsx",
          'West Indees' : "Z:\Desktop\CW\GroupB\West_Indees.xlsx"}

 group = ['A','B']
 random.choice(group)

 if random.choice(group)=='A':
    #timesleep(2)
    print('\nGroup A:')
    for team in groupA:
        print(team)

    T1 = random.choice(list(groupA))
    T2 = random.choice(list(groupA))

    while T1 == T2:
        T2 = random.choice(list(groupA))

 else:
    print('\nGroup B:')
    for team in groupB:
        print(team)

    T1 = random.choice(list(groupB))
    T2 = random.choice(list(groupB))

    while T1 == T2:
        T2 = random.choice(list(groupB))

 matchNO += 1
 #timesleep(2)

 print('\nMatch ' + str(matchNO) + ' - ' + str(T1) + ' vs ' + str(T2) + '\n')
 #timesleep(3)


 toss = ['Head','Tail']
 random.choice(toss)
 decision = ['Bat','Ball']

 if random.choice(toss) == 'Head':
    random.choice(decision)

    if random.choice(decision) == 'Bat':
        print(T1+' won the toss & elected to bat first\n')
        bat1st = T1
        bat2nd = T2

    else:
        print(T1+' won the toss & elected to ball first\n')
        bat1st = T2
        bat2nd = T1

 else:
    random.choice(decision)

    if random.choice(decision) == 'Bat':
        print(T2+' won the toss & elected to bat first\n')
        bat1st = T2
        bat2nd = T1

    else:
        print(T2+' won the toss & elected to ball first\n')
        bat1st = T1
        bat2nd = T2


 if bat1st in groupA:
    filename1 = groupA.pop(str(bat1st))
    filename2 = groupA.pop(str(bat2nd))
 else:
    filename1 = groupB.pop(str(bat1st))
    filename2 = groupB.pop(str(bat2nd))


 def load_team1(filename1):
    team1_df = pd.read_excel(filename1)
    global team1_players
    team1_players = []
    team1_players = list(team1_df['Name'])


 def load_team2(filename2):
    team2_df = pd.read_excel(filename2)
    global team2_players
    team2_players = []
    team2_players = list(team2_df['Name'])


 load_team1(filename1)
 load_team2(filename2)

 #timesleep(2)
 print(bat1st + ' Playing 11 : ' + str(team1_players))
 #timesleep(2)
 print(bat2nd + ' Playing 11 : ' + str(team2_players))

 delivery = [0,0,0,0,1,1,1,2,2,3,4,4,6,'WB','NB','W']
 method_of_dismissal = ['Bowled','LBW','Caught','Stumped']

 # 1ST INNINGS

 #timesleep(2)
 print('\n1ST INNINGS')
 #timesleep(3)

 bowlersT2 = team2_players[5:]

 total_score1 = 0

 batsman1_score = 0
 batsman2_score = 0
 batsman1_balls = 0
 batsman2_balls = 0
 batsman_on_strike = team1_players[0]
 wickets = 0
 extras = 0
 wb = 0
 nb = 0
 fall_of_wickets = []

 batting_summary = {}

 for player in team1_players:
    batting_summary[player] = 0

 bowling_summary = {}

 for bowler in bowlersT2:
    bowling_summary[bowler] = 0

 for overs in range(20):
    if wickets == 10:
        print('All out')
        break

    nballer = random.choice(bowlersT2)
    print()
    print('Over '+ str(overs+1) + ' by '+ str((nballer)))
    balls = 0
    over_score = 0

    while balls < 6:

        print(str(overs) + '.' + str(balls+1) + ' ' , end="")
        player_score = random.choice(delivery)

        if player_score == 'WB':
            total_score1+=1
            over_score+=1
            extras+=1
            wb+=1
            print('Wide ball')

        elif player_score == 'NB':
            total_score1+=1
            over_score+=1
            extras+=1
            nb+=1
            print('No ball')

        elif player_score == 0:
            print('No run')
            balls += 1
            if batsman_on_strike == team1_players[0]:
                batsman1_balls+=1
            elif batsman_on_strike == team1_players[1]:
                batsman2_balls+=1

        elif player_score == 1:
            total_score1+=1
            over_score+=1
            print('1 run')
            balls += 1
            if batsman_on_strike == team1_players[0]:
                batsman1_score+=1
                batsman1_balls+=1
                batsman_on_strike = team1_players[1]
            elif batsman_on_strike == team1_players[1]:
                batsman2_score+=1
                batsman2_balls+=1
                batsman_on_strike = team1_players[0]

        elif player_score == 2:
            total_score1+=2
            over_score+=2
            print('2 runs')
            balls += 1
            if batsman_on_strike == team1_players[0]:
                batsman1_score+=2
                batsman1_balls+=1
            elif batsman_on_strike == team1_players[1]:
                batsman2_score+=2
                batsman2_balls+=1

        elif player_score == 3:
            total_score1+=3
            over_score+=3
            print('3 runs')
            balls += 1
            if batsman_on_strike == team1_players[0]:
                batsman1_score+=3
                batsman1_balls+=1
                batsman_on_strike = team1_players[1]
            elif batsman_on_strike == team1_players[1]:
                batsman2_score+=3
                batsman2_balls+=1
                batsman_on_strike = team1_players[0]

        elif player_score == 4:
            total_score1+=4
            over_score+=4
            print('Four!')
            balls += 1
            if batsman_on_strike == team1_players[0]:
                batsman1_score+=4
                batsman1_balls+=1
            elif batsman_on_strike == team1_players[1]:
                batsman2_score+=4
                batsman2_balls+=1

        elif player_score == 6:
            total_score1+=6
            over_score+=6
            print('Six!')
            balls += 1
            if batsman_on_strike == team1_players[0]:
                batsman1_score+=6
                batsman1_balls+=1
            elif batsman_on_strike == team1_players[1]:
                batsman2_score+=6
                batsman2_balls+=1

        else:
            method = random.choice(method_of_dismissal)
            balls += 1
            wickets+=1
            bowling_summary[nballer] = bowling_summary[nballer]+1

            if batsman_on_strike == team1_players[0]:
                batsman1_balls+=1
                print(batsman_on_strike +' Out! '+ str(method) +'! for '+ str(batsman1_score) + '(' + str(batsman1_balls) + ') by ' + str(nballer))

                fall_of_wickets.append(str(total_score1) + '/' + str(wickets) + ' (' + batsman_on_strike + ', ' + str(overs) + '.' + str(balls) + ' ov)')
                batting_summary[team1_players[0]] = batsman1_score

                del team1_players[0]
                batsman1_score = 0
                batsman1_balls = 0
                try:
                    batsman_on_strike = team1_players[0]
                except:
                    break

            elif batsman_on_strike == team1_players[1]:
                batsman2_balls+=1
                print(batsman_on_strike + ' Out! '+ str(method) +'! for '+ str(batsman2_score) + '(' + str(batsman2_balls) + ') by ' + str(nballer))

                fall_of_wickets.append(str(total_score1) + '/' + str(wickets) + ' (' + batsman_on_strike + ', ' + str(overs) + '.' + str(balls) + ' ov)')
                batting_summary[team1_players[1]] = batsman2_score

                del team1_players[1]
                batsman2_score = 0
                batsman2_balls = 0
                try:
                    batsman_on_strike = team1_players[1]
                except:
                    break

        if wickets == 10:
            break
        else:
            pass

    if wickets!=10:
        print('End of the over '+ str(overs+1)+', by '+ str(nballer) +', '+ str(over_score)+' runs conceded.')
    else:
        pass
 if wickets != 10:

    print(str(team1_players[0]) + ' ' +str(batsman1_score)+'(' + str(batsman1_balls) + ')*')
    print(str(team1_players[1]) + ' ' +str(batsman2_score)+'(' + str(batsman2_balls) + ')*')

    batting_summary[team1_players[0]] = batsman1_score
    batting_summary[team1_players[1]] = batsman2_score

 else:

    try:
        print(str(team1_players[0]) + ' ' + str(batsman1_score) + '(' + str(batsman1_balls) + ')*')
        batting_summary[team1_players[0]] = batsman1_score
    except:
        print(str(team1_players[1]) + ' ' + str(batsman2_score) + '(' + str(batsman2_balls) + ')*')
        batting_summary[team1_players[1]] = batsman2_score


 print('\nEnd of 1st innings\n')
 print('Extras ' + str(extras) + ' (NB ' + str(nb) + ', WB ' + str(wb) + ')' )
 print(bat1st + ' ' + str(total_score1) + '/' + str(wickets)+ '\n')
 #timesleep(1)
 print('Fall of Wickets:')
 fall_of_wickets_T1 = print(str(fall_of_wickets)[1:-1])
 #timesleep(2)




 load_team1(filename1)
 load_team2(filename2)

 # 2ND INNINGS

 print('\n2ND INNINGS')
 ##timesleep(3)

 bowlersT1 = team1_players[5:]

 total_score2 = 0
 batsman1_score = 0
 batsman2_score = 0
 batsman1_balls = 0
 batsman2_balls = 0
 batsman_on_strike = team2_players[0]
 wickets = 0
 extras = 0
 wb = 0
 nb = 0
 fall_of_wickets = []

 batting_summary2 = {}

 for player in team2_players:
    batting_summary2[player] = 0

 bowling_summary2 = {}

 for bowler in bowlersT1:
    bowling_summary2[bowler] = 0


 for overs in range(20):
    if wickets == 10:
        print('All out')
        break
    elif total_score2 > total_score1:
        print(bat2nd + ' Won!')
        break
    else:
        pass

    nballer = random.choice(bowlersT1)
    print()
    print('Over '+ str(overs+1) + ' by '+ str((nballer)))
    balls = 0
    over_score = 0

    while balls < 6:

        print(str(overs) + '.' + str(balls+1) + ' ' , end="")
        player_score = random.choice(delivery)

        if player_score == 'WB':
            total_score2+=1
            over_score+=1
            extras+=1
            wb+=1
            print('Wide ball')

        elif player_score == 'NB':
            total_score2+=1
            over_score+=1
            extras+=1
            nb+=1
            print('No ball')

        elif player_score == 0:
            print('No run')
            balls += 1
            if batsman_on_strike == team2_players[0]:
                batsman1_balls+=1
            elif batsman_on_strike == team2_players[1]:
                batsman2_balls+=1

        elif player_score == 1:
            total_score2+=1
            over_score+=1
            print('1 run')
            balls += 1
            if batsman_on_strike == team2_players[0]:
                batsman1_score+=1
                batsman1_balls+=1
                batsman_on_strike = team2_players[1]
            elif batsman_on_strike == team2_players[1]:
                batsman2_score+=1
                batsman2_balls+=1
                batsman_on_strike = team2_players[0]

        elif player_score == 2:
            total_score2+=2
            over_score+=2
            print('2 runs')
            balls += 1
            if batsman_on_strike == team2_players[0]:
                batsman1_score+=2
                batsman1_balls+=1
            elif batsman_on_strike == team2_players[1]:
                batsman2_score+=2
                batsman2_balls+=1

        elif player_score == 3:
            total_score2+=3
            over_score+=3
            print('3 runs')
            balls += 1
            if batsman_on_strike == team2_players[0]:
                batsman1_score+=3
                batsman1_balls+=1
                batsman_on_strike = team2_players[1]
            elif batsman_on_strike == team2_players[1]:
                batsman2_score+=3
                batsman2_balls+=1
                batsman_on_strike = team2_players[0]

        elif player_score == 4:
            total_score2+=4
            over_score+=4
            print('Four!')
            balls += 1
            if batsman_on_strike == team2_players[0]:
                batsman1_score+=4
                batsman1_balls+=1
            elif batsman_on_strike == team2_players[1]:
                batsman2_score+=4
                batsman2_balls+=1

        elif player_score == 6:
            total_score2+=6
            over_score+=6
            print('Six!')
            balls += 1
            if batsman_on_strike == team2_players[0]:
                batsman1_score+=6
                batsman1_balls+=1
            elif batsman_on_strike == team2_players[1]:
                batsman2_score+=6
                batsman2_balls+=1

        elif player_score == 'W':
            method = random.choice(method_of_dismissal)
            balls += 1
            wickets+=1
            bowling_summary2[nballer] = bowling_summary2[nballer]+1

            if batsman_on_strike == team2_players[0]:
                batsman1_balls+=1
                print(batsman_on_strike +' Out! '+ str(method) +'! for '+ str(batsman1_score) + '(' + str(batsman1_balls) + ') by ' + str(nballer))

                fall_of_wickets.append(str(total_score2) + '/' + str(wickets) + ' (' + batsman_on_strike + ', ' + str(overs) + '.' + str(balls) + ' ov)')
                batting_summary2[team2_players[0]] = batsman1_score

                del team2_players[0]
                batsman1_score = 0
                batsman1_balls = 0
                try:
                    batsman_on_strike = team2_players[0]
                except:
                    break

            elif batsman_on_strike == team2_players[1]:
                batsman2_balls+=1
                print(batsman_on_strike + ' Out! '+ str(method) +'! for '+ str(batsman2_score) + '(' + str(batsman2_balls) + ') by ' + str(nballer))

                fall_of_wickets.append(str(total_score2) + '/' + str(wickets) + ' (' + batsman_on_strike + ', ' + str(overs) + '.' + str(balls) + ' ov)')
                batting_summary2[team2_players[1]] = batsman2_score

                del team2_players[1]
                batsman2_score = 0
                batsman2_balls = 0
                try:
                    batsman_on_strike = team2_players[1]
                except:
                    break

        if wickets == 10 or total_score2 > total_score1:
            break
        else:
            pass

    if wickets != 10:
        print('End of the over '+ str(overs+1)+', by '+ str(nballer) +', '+ str(over_score)+' runs conceded.')
    else:
        pass

 if total_score1 > total_score2:
    print(bat1st + ' Won!')


 if wickets != 10: #notout batsmans

    print(str(team2_players[0]) + ' ' +str(batsman1_score)+'(' + str(batsman1_balls) + ')*')
    print(str(team2_players[1]) + ' ' +str(batsman2_score)+'(' + str(batsman2_balls) + ')*')

    batting_summary2[team2_players[0]] = batsman1_score
    batting_summary2[team2_players[1]] = batsman2_score

 else:

    try:
        print(str(team2_players[0]) + ' ' + str(batsman1_score) + '(' + str(batsman1_balls) + ')*')
        batting_summary2[team2_players[0]] = batsman1_score
    except:
        print(str(team2_players[1]) + ' ' + str(batsman2_score) + '(' + str(batsman2_balls) + ')*')
        batting_summary2[team2_players[1]] = batsman2_score


 print('\nEnd of 2nd innings\n')
 print('Extras ' + str(extras) + ' (NB ' + str(nb) + ', WB ' + str(wb) + ')' )
 print(bat2nd +' '+ str(total_score2) + '/' + str(wickets)+ '\n')
 #timesleep(1)
 print('Fall of Wickets:')
 fall_of_wickets_T1 = print(str(fall_of_wickets)[1:-1])
 #time.sleep(1)

 print('\nMatch Summary:--\n')
 if total_score1>total_score2:
    print(bat1st + ' beat ' + bat2nd + ' by ' + str(total_score1 - total_score2) + ' runs!')
 else:
    print(bat2nd + ' beat ' + bat1st + ' by ' + str(10 - wickets) + ' wickets!')
 #time.sleep(2)

 print('\n' + bat1st + ' Batting - Runs scored by each player:\n')
 for batsman, runs in batting_summary.items():
    print(batsman, runs)
 #time.sleep(1)

 print('\n' + bat2nd + ' Bowling - Wickets taken by each player:\n')
 for bowler, wickets in bowling_summary.items():
    print(bowler,wickets)
 #time.sleep(1)

 print('\n' + bat2nd + ' Batting - Runs scored by each player:\n')
 for batsman, runs in batting_summary2.items():
    print(batsman, runs)
 #time.sleep(1)

 print('\n' + bat1st + ' Bowling - Wickets taken by each player:\n')
 for bowler, wickets in bowling_summary2.items():
    print(bowler,wickets)
 time.sleep(1)
 print()
 #time.sleep(2)


 a=1
 while a==1:
     try:
         ask_for_another_Match = int(input('Enter 1 to play the next match. Enter 0 to Exit\n: '))
         a=2
     except ValueError:
         print('Invalid input!')
         print(ValueError)
         a=1
     else:
         if ask_for_another_Match == 1:
             pass

         elif ask_for_another_Match == 0:
             pass

         else:
             print('Invalid input!')
             a=1
             pass

 if ask_for_another_Match == 1:
     pass
 else:
     break

