import random
def guessing_game():
       
       print("\n WELCOME TO THR ROCK,PAPER,SCISOOR GAME")
       print("CHOICES: ROCK , PAPER , SCCISSOR\n")

       items = ["paper","rock","scissor"]

       rand=random.choice(items)
       attempts=0
       while True:
              user_choice=input("enter your choice: ").lower()
              if user_choice=="exit":
                     print("GAME ENDED")
                     break
              
              elif user_choice ==rand :
                     print("CONGRATULATIONS YOU WON")
                     print(f"you won the game by guessing the correct output {user_choice} and in {attempts+1}attempts\n")
                     play_again = input("If you want to play again , enter 'yes' , else type 'exit' to quit ").lower()

                     if play_again != 'yes':
                            print("THANKS FOR PLAYING")
                     else:
                            guessing_game()
                
              else:
                     print("try again")
                     attempts=attempts+1
       
guessing_game()
