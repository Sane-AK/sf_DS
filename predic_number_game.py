import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    count += 1
    predict_number = int(input('Guess he number from 1 to 100: '))
    if number < predict_number:
        print('The number must be less!')
    elif predict_number < number:
        print('The number must be greater!')
    else:
        print(f"You guessed the number! Number is {number}, {count} attempts")
        break