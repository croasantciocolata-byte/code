
total_score = 10
def increase_score(score):
    score = input("Enter number: ")
    score = int(score) + 10
    return score 


score = increase_score(total_score)
print(total_score)
print(increase_score(score))
    