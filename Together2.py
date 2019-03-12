from Together import Teams

Question = "What NFL teams do you want to compare?"
PromptW = "\nWhat is the winner team? "
Woot = input(PromptW)
PromptL = "\nWhat is the losing team? "
Boo = input(PromptL)
PromptWS = "\nWhat is the winners score? "
High = input(PromptWS)
PromptLS = "\nWhat is the losing score? "
Low = input(PromptLS)

print("\nThe " + Woot + " beat the " + Boo + " With a score of " + High + " to " + Low + "!")
Winning_Message = Teams(Woot, Boo, High, Low)
print(Winning_Message.Get_Message())
