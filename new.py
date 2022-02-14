max_score =[0]
n = len(max_score)
if max_score[-1] !=None:
    print("maximum score is : ",max_score[-1])

score = int(input("whats your score? "))

if score > max_score[-1]:
    max_score.append(score)
    print(f"now {score} is the new max score")