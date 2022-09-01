"""Game "Predict the number!".
Compute hide and guess the number himself
"""

import numpy as np
def random_predict(number: int = 1) -> int:
    """Random guess the number

    Args:
        number (int, optional): hide number. Defaults to 1.

    Returns:
        int: count attempts
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) #генерируем предполагаемое число
        if number == predict_number:
            break #выход, если число угадали
    return count
print(f'Count attempts - {random_predict()}')

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches our algorithm guesses

    Args:
        random_predict (_type_): predict function

    Returns:
        int: mean attempts
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

#RUN
if __name__ == '__maim__':
    score_game(random_predict)
