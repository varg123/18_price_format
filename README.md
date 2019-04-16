# Форматирование цены

Форматирует цены к более наглядному виду. К примеру из `3245.568000` переведёт в `3 245.57`.
У программы два интерфейса:
- Консольный - для запуска в ручном режиме из консоли
- Программный - чтобы использовать её в программе
Для проверки работоспособности есть тесты в `test.py`.

# Как использовать

1. Консольный интерфейс.
Требуется python 3.5 и выше. 
Для испольпользования в консоли нужно ввести обязательный аргумен `-p` или `--price`.


Пример использования в консоли:

```bash
$ python format_price.py -p 4234.123
Введеная цена: 4234.123
Отформатированая цена: 4 234,12
```
2. Программный интерфейс.

Для использования нужно дописать в начало программного кода:
```python
from format_price import format_price
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)