total_sec = input("Enter the total number of seconds: ")

total_sec = int(total_sec)
if total_sec < 0 or total_sec > 8640000:
    print("Невірне число")
    exit()

q_d = total_sec // 86400


if q_d % 100 >= 11  and q_d % 100 <= 14:
    word_days = "днів"
elif q_d % 10 == 1:
    word_days = "день"
elif q_d % 10 >= 2 and q_d % 10 <= 4:
    word_days = "дні"
else:
    word_days = "днів"

q_h = total_sec % 86400 // 3600
q_m = total_sec % 3600 // 60
q_s = total_sec % 60

print(f"{q_d} {word_days}, {q_h:02}:{q_m:02}:{q_s:02}")


