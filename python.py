score = list (map(int,input().split()))
average = sum(score)/len(score)
count = len(list(x for x in score if x >=60))
print ('average = {}'.format(average))
print('count = {}'.format(count))
