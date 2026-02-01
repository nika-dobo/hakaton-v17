# ფაილი: task9.py
# შესაფასებელი ქულა: 0-4
# შექმენი ფუნქცია accum და უნდა გადმოგეცეს რაიმე სიტყვა 
# მაგალითი : accum("abcd") -> "A-Bb-Ccc-Dddd"

def accum(random1):
    res = ""

    for i in range(len(random1)):
        res += f"{random1[i].upper()}{random1[i].lower() * i}-"


    return res[:-1]