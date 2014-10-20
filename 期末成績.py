# 期末成績計算

score1 = int(input("enter first test score:"))
score2 = int(input("enter second test score:"))
score3 = int(input("enter third test score:"))

score = [score1, score2, score3]

score.sort()

print (score[0]*0.2 + score[1]*0.3 + score[2]*0.5)
