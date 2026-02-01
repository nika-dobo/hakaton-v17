# ფაილი: task6.py
# შესაფასებელი ქულა: 0-3
# ამოცანა:
# დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებელს წინადადებას

# პროგრამამ უნდა:
# დათვალოს თითოეული ასო რამდენჯერ მეორდება წინადადებაში.
# დაბეჭდოს მხოლოდ ის ასოები, რომლებიც 3–ჯერ ან მეტი მეორდება წინადადებაში..

def task6():
    sentence = input("შეიყვანეთ წინადადება: ")
    
    checked_chars = "" 

    for i in sentence:
        if i not in checked_chars:
            
            raodenoba = sentence.count(i)

            if raodenoba >= 3:
                print(i, raodenoba)
            
            checked_chars += i

task6()