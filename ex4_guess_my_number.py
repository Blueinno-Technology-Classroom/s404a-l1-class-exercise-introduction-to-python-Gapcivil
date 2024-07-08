import random

answer=random.randint(0,1000)

print("This number is between 0-1000 for your information")

while True:

    user_input=int(input('Enter a number: '))
    print(f'You have entered: {user_input}')
    if user_input==answer:
        print('Correct!')
        break
    elif user_input>answer:
        print('Too High')
    else:
        print('Too Low')
  