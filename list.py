import random
furniture=["table","chair","sofa","shelf"]
print(furniture)
print(furniture[0])
print(furniture[1])
print(furniture[:2])
for item in furniture:
    if item=="sofa":
        print("Found the sofa!")
        
throwDiceNumbers=[0,0,0,0,0]
for i in range(5):
    throwDiceNumbers[i]=random.randint(1,6)
print("Dice throw results:", throwDiceNumbers)
total=sum(throwDiceNumbers)
print("Total of dice throws:", total)
highest=max(throwDiceNumbers)
print("Highest dice throw:", highest)
