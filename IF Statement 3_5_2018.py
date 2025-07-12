from random import randint

num = randint(1,10)
guess = eval(input('Enter Your Guess: '))
a=num-guess
b=guess-num
if guess==num:
    print('You Got It!')
elif guess>num:
    print('You are ',b,' number higher')
    print('The num is: ', num)
elif guess<num:
    print('Your are ',a,' number lower')
    print('The num is: ', num)

