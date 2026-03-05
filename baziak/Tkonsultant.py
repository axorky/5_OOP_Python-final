import tkinter as tk

def get_recommendation():
    # получаем требуемый бюджет пользователя, изначальная сумма 20000
    b_input = budget_entry.get()
    b = 0
    if b_input.isdigit():
        b = int(b_input)
    else:
        b = 20000
    if b <= 0:
        b = 20000

    # выбор предпочтения, для чего нужен телефон пользователю
    purp_input = purpose_entry.get()
    purp = 1
    if purp_input == "1":
        purp = 1
    elif purp_input == "2":
        purp = 2
    elif purp_input == "3":
        purp = 3
    elif purp_input == "4":
        purp = 4
    else:
        purp = 1

    # получаем предпочтение пользователя по бренду
    brand = brand_entry.get()
    if brand == "":
        brand = "любой"

    # на основе бюджета выбираем категорию телефона пользователя
    level = ""
    if b < 15000:
        level = "бюджетный"
    elif b <= 35000:
        level = "средний"
    else:
        level = "премиум"

    # вводим данные в ткинтер
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, f"Ваш бюджет: {b} р.\n")
    text_area.insert(tk.END, f"Категория: {level}\n")
    text_area.insert(tk.END, f"Предпочитаемый брэнд: {brand}\n")

    # выбор бренда на основе предпочтения пользователя, учитываются разные наборы бренда, если он не указан то допускаются другие модели "любой"
    if brand != "любой":
        text_area.insert(tk.END, f"Учитываем ваш выбор бренда: {brand}\n")
        if "xia" in brand.lower() or "ксиа" in brand.lower() or "сяо" in brand.lower():
            if level == "бюджетный":
                text_area.insert(tk.END, "Рекомендуем: Xiaomi Redmi Pad SE\nЦена: около 10600 р.\nПочему?: Планшет с диагональю 8.7, 64 ГБ память, Частота 90 ГЦ\n")
            elif level == "средний":
                text_area.insert(tk.END, "Рекомендуем: Телефон Xiaomi 14T\nЦена: около 32400 р.\nПочему?: Невероятная камера, Минимальные рамки экрана, 12 Гб ОЗУ\n")
            else:
                text_area.insert(tk.END, "Рекомендуем: Смартфон realme GT7 Pro\nЦена: около 69000 р.\nПочему?: Full HD, 512 ГБ памяти, Высокая производительность\n")
        elif "iph" in brand.lower() or "айф" in brand.lower() or "app" in brand.lower() or "эпл" in brand.lower():
            if level == "бюджетный":
                text_area.insert(tk.END, "Рекомендуем: Apple iPhone 7\nЦена: около 11000 р.\nПочему?: 128 ГБ Память, Отличная камера для своей цены, Чистый звук\n")
            elif level == "средний":
                text_area.insert(tk.END, "Рекомендуем: Apple iPhone 13 mini\nЦена: около 35000 р.\nПочему?: Ёмкость батареи 2438 мА/ч, 256 ГБ памяти, OLED-дисплей\n")
            else:
                text_area.insert(tk.END, "Рекомендуем: Apple iPhone 16\nЦена: около 67000 р.\nПочему?: 50 мп камера, Видеосъёмка 4к, 8 ГБ ОЗУ, До 40 часов работы\n")
        elif "sams" in brand.lower() or "самс" in brand.lower():
            if level == "бюджетный":
                text_area.insert(tk.END, "Рекомендуем: Samsung Galaxy A16\nЦена: около 15000 р.\nПочему?: 6.7 диагональ, Быстрая зарядка, FHD+ Super AMOLED Дисплей\n")
            elif level == "средний":
                text_area.insert(tk.END, "Рекомендуем: Смартфон Samsung Galaxy A56\nЦена: около 35200 р.\nПочему?: Аккумулятор 5000 мА/ч, камера 50+12Мп, Частота 120 ГЦ\n")
            else:
                text_area.insert(tk.END, "Рекомендуем: Samsung Galaxy S25 Ultra\nЦена: около 74900 р.\nПочему?: 12 ГБ ОЗУ, Ультрапрочный, Мощный процессор Snapdragon\n")
        else:
            text_area.insert(tk.END, f"К сожалению - {brand}, не входит в число наших рекомендуемых телефонов, но мы это исправим!\n")
    else:
        # если бренд не выбран выбираются эти модели, по бюджету и предпочтению пользователя
        text_area.insert(tk.END, "Наше предложение:\n")
        if level == "бюджетный":
            if purp == 4:
                text_area.insert(tk.END, "Рекомендуем: TECNO POVA 7 - Для ваших игр\nЦена: около 15000 р.\nПочему?: Большой экран, 8 ГБ ОЗУ\n")
            elif purp == 3:
                text_area.insert(tk.END, "Рекомендуем: OPPO A5\nЦена: около 10000 р.\nПочему?: 2 Камеры 50 Мп, 256 ГБ\n")
            elif purp == 2:
                text_area.insert(tk.END, "Рекомендуем: REDMI 15\nЦена: около 13000 р.\nПочему?: Надежный, лёгкий, NFC\n")
            else:
                text_area.insert(tk.END, "Рекомендуем: Xiaomi Redmi Note 14\nЦена: около 15000 р.\nПочему?: Отличный телефон в соотношении цена=качество\n")
        elif level == "средний":
            if purp == 4:
                text_area.insert(tk.END, "Рекомендуем: Xiaomi Poco X7 Pro 5G\nЦена: около 25600 р.\nПочему?: Сильный процессор на базе mediatek, 12 ГБ ОЗУ\n")
            elif purp == 3:
                text_area.insert(tk.END, "Рекомендуем: HONOR 200\nЦена: около 32000 р.\nПочему?: Лучшая камера в своем классе, 3 Камеры, 512 ГБ памяти\n")
            elif purp == 2:
                text_area.insert(tk.END, "Рекомендуем: Samsung Galaxy S24 FE\nЦена: около 36000 р.\nПочему?: Частота 120 Гц, 6.7 Диагональ, Время работы до 21 часа\n")
            else:
                text_area.insert(tk.END, "Рекомендуем: HONOR X9d\nЦена: около 32600 р.\nПочему?: Прочный, Стильный, Защита от падений, пыли и влаги\n")
        else:
            if purp == 4:
                text_area.insert(tk.END, "Рекомендуем: Realme GT7\nЦена: около 51300 р.\nПочему?: Частота 120 Гц, 2к Разрешение, 7700 мм2 Система охлаждения\n")
            elif purp == 3:
                text_area.insert(tk.END, "Рекомендуем: Apple iPhone 16\nЦена: около 62900 р.\nПочему?: Лучшая камера 48+12 Мп, Зум до 25х\n")
            elif purp == 2:
                text_area.insert(tk.END, "Рекомендуем: Google Pixel 9\nЦена: около 57500 р.\nПочему?: Чёткий OLED-дисплей, Ёмкость аккумулятора 4700 мА/ч\n")
            else:
                text_area.insert(tk.END, "Рекомендуем: Huawei Mate 70 Pro\nЦена: около 64900 р.\nПочему?: Новый дизайн, встроенный ИИ-помощник, 6.9 диагональ\n")

    # если пользователя не утроило, или он ошибся в выборе то может начать заного
    text_area.insert(tk.END, "-"*30 + "\n")
    text_area.insert(tk.END, "Хотите изменить ввод? (да/нет):\n")

    # предотвращает слишком большое количество полей ввода
    global change_entry, change_button
    if 'change_entry' in globals():
        change_entry.destroy()
    if 'change_button' in globals():
        change_button.destroy()

    # подтверждаем ввод
    change_entry = tk.Entry(root)
    change_entry.pack()
    change_button = tk.Button(root, text="Подтвердить", command=confirm_change)
    change_button.pack()

def confirm_change():
    change = change_entry.get().lower()
    if change == "да" or change == "yes":
        text_area.insert(tk.END, "-"*30 + "\nПерезапустите программу для нового ввода.\n")
        # выбор на перезапуск программы
        change_entry.config(state='disabled')
        change_button.config(state='disabled')
    else:
        # всё ли устроило пользователя?
        text_area.insert(tk.END, "Вас всё устроило в нашем обслуживании?:\n")

        # предотвращает слишком большое количество полей ввода
        global mean_entry, mean_button
        if 'mean_entry' in globals():
            mean_entry.destroy()
        if 'mean_button' in globals():
            mean_button.destroy()

        # подтверждаем ввод
        mean_entry = tk.Entry(root)
        mean_entry.pack()
        mean_button = tk.Button(root, text="Отправить отзыв", command=send_feedback)
        mean_button.pack()

    # фидбек пользователя, если его устроило и не устроило
def send_feedback():
    mean = mean_entry.get().lower()
    if mean == "да" or mean == "yes":
        text_area.insert(tk.END, "-"*30 + "\nСпасибо за использование нашего консультанта!\nУдачных покупок!\n")
    else:
        text_area.insert(tk.END, "-"*30 + "\nМы учтём ваше мнение, спасибо за отзыв!\nУдачных покупок!\n")

# вывод всё на отдельное окно вывода, финальный этап
root = tk.Tk()
root.title("Консультант по смартфонам")

tk.Label(root, text="Добрый день! Сегодня я ваш консультант по выбору смартфона!").pack()
tk.Label(root, text="-"*30).pack()

tk.Label(root, text="Введите ваш бюджет в рублях:").pack()
budget_entry = tk.Entry(root)
budget_entry.pack()

tk.Label(root, text="Для чего нужен телефон?").pack()
tk.Label(root, text="1 - Для постоянного использования").pack()
tk.Label(root, text="2 - Для работы и учебы").pack()
tk.Label(root, text="3 - Для фото и видео").pack()
tk.Label(root, text="4 - Для игр").pack()
tk.Label(root, text="Введите номер (1-4):").pack()
purpose_entry = tk.Entry(root)
purpose_entry.pack()

tk.Label(root, text="Какой бренд вы бы хотели у своего телефона? (Ничего не пишите, если ничего не предпочитаете):").pack()
brand_entry = tk.Entry(root)
brand_entry.pack()

text_area = tk.Text(root, height=20, width=80)
text_area.pack()

tk.Button(root, text="Получить рекомендацию", command=get_recommendation).pack()

root.mainloop()
