"""Створіть модуль vacations_calendar який повинен містити глобально обʼявлену змінну зі списком всіх 
українських державних свят (дати і назва).
Повинен бути створений модуль vacations_calendar. Технічно це файл vacations_calendar.py.
В модулі vacations_calendar повинна бути створена глобальна змінна calendar.
Змінна calendar повинна містити словник (dict) всіх українських державних свят. дата -> назва або назва ->
 дата - що буде ключом ви обираєте самостійно. Обидва варіанти будуть зараховані.
Словник calendar повинен бути типу dict, але типи внутрішніх данних ви обираєте самостійно. Будь який 
варіант вважається допустимим. Головне досягти працездатності функції check (дивіться наступну умову).
В модулі vacations_calendar заборонено писати будь яку глобальну логіку. Якщо ви хочете протестувати ваш код,
 ви повинні це робити в іншому модулі, або прибрати логіку перед пушом в репозиторій."""

calendar = {
    '01/01': 'Новий рік',
    '07/01': 'Різдво Христове',
    '08/03': 'Міжнародний жіночий день',
    '01/05': 'Міжнародний день праці',
    '09/05': 'День перемоги над нацизмом у Другій світовій війні',
    '28/06': 'День Конституції України',
    '28/07': 'День Української Державності',
    '24/08': 'День Незалежності України',
    '14/10': 'День захисника та захисниці України'
}