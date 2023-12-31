menu = ['Главное меню', 
        'Открыть файл', 
        'Сохранить файл', 
        'Показать контакты', 
        'Создать контакт', 
        'Найти контакт', 
        'Изменить контакт', 
        'Удалить контакт', 
        'Выход']
input_menu = 'Выберите пункт меню: '
input_menu_error = f'Ввести нужно ЧИСЛО (от 1 до {len(menu) - 1})'

load_successful = 'Телефонная книга загружена успешно!'
save_successful = 'Телефонная книга сохранена успешно!'

empty_book_error = 'Телефонная книга пуста или не открыта'

def input_contact(new: bool = False) -> list[str]:
    add = ' или ENTER, чтоб оставить без изменений' if new else ''
    return [f'Введите имя нового контакта{add}: ', 
            f'Введите номер телефона{add}: ',
            f'Введите комментарий{add}: ']

input_search_word = 'Введите ключевое слово для поиска: '

input_edit_contact_id = 'Введите ID контакта, который хотите изменить: '
input_del_contact_id = 'Введите ID контакта, который хотите удалить: '

operation = ['создан', 'изменен', 'удален']

confirm_changes = 'У вас есть несохраненные изменения! Сохранить? (y/n)'
exit_program = 'До свидания! До новых встреч!'

def contact_action(name: str, action: str) -> str:
    return f'Контакт {name} успешно {action}!'

def not_find(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'