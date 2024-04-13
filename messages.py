start_message = 'Привет, бот электронный дневник!\nДавайте начнём с вопроса: Вы преподаватель или родитель?'

error_choice_message = 'Нажмите на одну из двух кнопок ниже (ошибка выбора состояний)'

invalid_surname_or_birth_message = 'Неверные данные. Проверьте доступность выбранного предмета и дату рождения. Либо учащегося с такой фамилией нет.'
invalid_surname_or_grade_message = 'Неверные данные. Проверьте корректность введённой оценки. Либо учащегося с такой фамилией нет.'

incorrect_password_message = 'Введён неверный пароль.'
incorrect_grade_message = 'Введена некорректная оценка. Она должна быть от 2 по 5.'

parent_choice_message = 'Отлично! Для получения оценок Вашего ребёнка введите сообщение в таком формате:\n\n' \
                        'Сидоров 05.03.2008 Физика\n\nИ в случае, если все данные введены верно - бот пришлёт Вам оценки по нужному предмету.\n' \
                        'Доступные предметы: Математика, Физика, Информатика'

teacher_enter_password_message = 'Прекрасно! Введите пароль от клиента учителя.'
teacher_work_message = 'Пароль верный! Для добавления новой оценки напишите сообщение в таком формате:\n\n' \
                       'Терешков Математика 3\n\nИ в случае, если все данные введены верно - бот напишет, что всё успешно записано.\n' \
                       'Доступные предметы: Математика, Физика, Информатика'
add_grade_message = 'Оценка успешно добавлена!'

MESSAGES = {
    'start': start_message,

    'error_choice': error_choice_message,

    'invalid_surname_or_birth': invalid_surname_or_birth_message,
    'invalid_surname_or_grade': invalid_surname_or_grade_message,

    'incorrect_password': incorrect_password_message,
    'incorrect_grade': incorrect_grade_message,

    'parent_choice': parent_choice_message,

    'teacher_enter_password': teacher_enter_password_message,
    'teacher_work': teacher_work_message,
    'add_grade': add_grade_message,
}