X=int(input())

stick=64
answer=1
for _ in range(6):
  if(stick>X):
    stick /= 2
  if(stick==X):
    print(answer)
    break
  if(stick<X):
    X-=stick
    answer+=1