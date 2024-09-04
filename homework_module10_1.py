import time
from time import sleep
from threading import Thread

# Объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:  # Указание кодировки utf-8
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
start_time = time.time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени и расчет времени выполнения
end_time = time.time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Взятие текущего времени
start_time_threads = time.time()

# Создание и запуск потоков с аргументами из задачи
threads = []
threads.append(Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(Thread(target=write_words, args=(100, 'example8.txt')))

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени и расчет времени выполнения потоков
end_time_threads = time.time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")
