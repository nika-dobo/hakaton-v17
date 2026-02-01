# ფაილი: extra_task.py
# შესაფასებელი ქულა: 0-4
# ამოცანა:
# შექმენით ფუნქცია user_password_guess ჩვენ გადმოგვეცემა პაროლი და 
# თქვენი დალვალებაა:
# 3 ცდაში გამოიცნოთ პაროლი
# თუ 3 ცდა ამოგეწურათ მაშინ პაროლის შეყვანა უნდა შეგეძლოს 5 წამში

import time

def user_password_guess():
    user = input("enter pass:")
    count = 0

    while True:
        my_guess = input("my guess is:")
        if my_guess == user:
            print("you guessed it")
            break

        count += 1
        if count == 3:
            time.sleep(5)


user_password_guess()