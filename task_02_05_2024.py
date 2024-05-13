# Task 1
def get_sorted_list():
    user_list = []
    for i in range(1, 6):
        user_input = int(input(f"{i}. sayıyı girin: "))
        user_list.append(user_input)
    sorted_list = sorted(user_list)
    print(f"Sıralı liste: {sorted_list}")

# Task 2
def sort_words():
    sentence = input("Cümleyi girin: ").strip()
    sorted_words = " ".join(["".join(sorted(word)) for word in sentence.split()])
    print(f"Alfabetik sıralı kelimeler: {sorted_words}")

# Task 3
def guess_number():
    target_number = 13
    attempts = []
    while True:
        guess = int(input("Sayıyı tahmin edin: "))
        attempts.append(guess)
        if guess == target_number:
            num_attempts = len(attempts)
            print(f"\nTebrikler! {num_attempts} denemede sayıyı buldunuz.")
            for i, attempt in enumerate(attempts, start=1):
                print(f"{i}. deneme: {attempt}")
            break

# Task 4
def print_prime_numbers():
    prime_numbers = []
    for num in range(1, 101):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            prime_numbers.append(num)
    print(f"Asal sayılar: {prime_numbers}")

#
while True:
    task_choice = input("Görev numarasını girin (1-4) veya çıkmak için 'q' tuşuna basın: ")
    if task_choice == '1':
        get_sorted_list()
    elif task_choice == '2':
        sort_words()
    elif task_choice == '3':
        guess_number()
    elif task_choice == '4':
        print_prime_numbers()
    elif task_choice.lower() == 'q':
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")