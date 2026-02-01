# ფაილი: task8.py
# შესაფასებელი ქულა: 0-4
# შექმენი ფუნქცია get_count და ფუნქციას უნდა გადაეცემოდეს არგუმენტი წინადადება და თქვენი დავალებაა დაითვალოს ხმოვნები “a, e, i, o, u”

def get_count(random):
    letters = "aeiou"
    count = 0

    for i in random.lower():
        if i in letters:
            count += 1

    return count