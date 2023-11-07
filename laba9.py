
file_name = "TF13_1.txt"
golosni = "AEIOUaeiou"
text = [
    "Apple orange banana.",
    "Cat dog elephant.",
    "Python programming language.",
    "Artificial intelligence is fascinating.",
    "Umbrella xylophone house.",
]

try:
    with open(file_name, "w") as file:
        for line in text:
            file.write(line + "\n")
    print(f"Файл '{file_name}' успішно створено.")
except Exception as e:
    print(f"Виникла помилка: {e}")


file_name2 = "TF13_2.txt"

try:
    with open(file_name, "r") as file1, open(file_name2, "w") as file2:
        for line in file1:
            words = line.split()
            for word in words:
                if word[0] in golosni:
                    file2.write(word + "\n")
    print(f"Слова з голосних літер в файлі '{file_name2}' успішно записано.")
except Exception as e:
    print(f"Виникла помилка: {e}")

try:
    with open(file_name2, "r") as file:
        print(f"Вміст файла '{file_name2}':")
        for line in file:
            print(line.strip())
except Exception as e:
    print(f"Виникла помилка: {e}")
