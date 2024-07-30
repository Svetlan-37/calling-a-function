def send_email(message, recipient, sender="university.help@gmail.com"):
    my_list = [sender, recipient]

# пожалуйста, исправьте задание
    for i in my_list:
        if '@' not in i:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
            return
    for i in my_list:
        if '.com' in i:
            continue
        elif '.ru' in i:
            continue
        elif '.net' in i:
            continue
        else:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
            return

# напоминаю самому себе
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return

# это сообщение для проверки связи
# как лучший студент
    if sender == "university.help@gmail.com":
        print('Письмо уcпешно отправлено с адреса', sender, 'на адрес ', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес ', recipient)


send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
