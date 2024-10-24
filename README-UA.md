# PinEye

[![Static Badge](https://img.shields.io/badge/Telegram-BOT-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/PinEye_Bot/pineye?startapp=r_352437152)

[![Static Badge](https://img.shields.io/badge/My_Telegram_Сhannel-@CryptoCats__tg-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/CryptoCats_tg)

![img1](.github/images/demo.png)

[![Static Badge](https://img.shields.io/badge/README_in_Ukrainian_available-README_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%8E_%D0%BC%D0%BE%D0%B2%D0%BE%D1%8E-blue.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjgwMCI+DQo8cmVjdCB3aWR0aD0iMTIwMCIgaGVpZ2h0PSI4MDAiIGZpbGw9IiMwMDU3QjciLz4NCjxyZWN0IHdpZHRoPSIxMjAwIiBoZWlnaHQ9IjQwMCIgeT0iNDAwIiBmaWxsPSIjRkZENzAwIi8+DQo8L3N2Zz4=)](README-UA.md)
[![Static Badge](https://img.shields.io/badge/README_in_russian_available-README_%D0%BD%D0%B0_%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5-blue?style=for-the-badge)](README-RU.md)


## Функціонал
| Функціонал																| Підтримується |
|---------------------------------------------------------------------------|:---------:|
| Багатопоточність															|     ✅     |
| Прив'язка проксі до сесії													|     ✅     |
| Авто-виконання завдань🔥													|     ✅     |
| Авто-купівля предметів за наявності монет (tap, energy, charge)			|     ✅     |
| Рандомний час сну між кліками												|     ✅     |
| Рандомна кількість кліків за запит										|     ✅     |
| Підтримка tdata / pyrogram .session / telethon .session					|     ✅     |


## [Налаштування](https://github.com/CatSnowdrop/TapSwap/blob/main/.env-example)
| Налаштування             | Опис                                                                                  		   |
|--------------------------|-----------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**    | Дані платформи, з якої запускати сесію Telegram _(сток - Android)_                    		   |
| **MIN_AVAILABLE_ENERGY** | Мінімальна кількість доступної енергії, при досягненні якої буде затримка _(напр. 100)_       |
| **SLEEP_BY_MIN_ENERGY**  | Затримка при досягненні мінімальної енергії в секундах _(напр. [1800,2400])_                  |
| **ADD_TAPS_ON_TURBO**    | Скільки тапів буде додано під час активації турбо _(напр. 2500)_                              |
| **AUTO_TASK**			   | Автовиконання завдань _(True / False)_                            						   	   |
| **MAX_TASK_ITERATIONS**  | Кількість завдань за 1 цикл _(напр. 4)_													   |
| **AUTO_UPGRADE_TAP**     | Чи покращувати тап _(True / False)_														   |
| **MAX_TAP_LEVEL**        | Максимальний рівень прокачування тапа _(до 20)_                                               |
| **AUTO_UPGRADE_ENERGY**  | Чи покращувати енергію _(True / False)_                                                       |
| **MAX_ENERGY_LEVEL**     | Максимальний рівень прокачування енергії _(до 20)_                                            |
| **AUTO_UPGRADE_CHARGE**  | Чи покращувати заряд енергії _(True / False)_                                                 |
| **MAX_CHARGE_LEVEL**     | Максимальний рівень прокачування заряду енергії _(до 5)_                                      |
| **APPLY_DAILY_ENERGY**   | Чи використовувати щоденний безкоштовний буст енергії _(True / False)_                        |
| **APPLY_DAILY_TURBO**    | Чи використовувати щоденний безкоштовний буст турбо _(True / False)_                          |
| **RANDOM_CLICKS_COUNT**  | Рандомна кількість тапів _(напр. [50,200])_                                                   |
| **SLEEP_BETWEEN_TAP**    | Рандомна затримка між тапами в секундах _(напр. [10,25])_                                     |
| **USE_PROXY_FROM_FILE**  | Чи використовувати проксі з файлу `bot/config/proxies.txt` _(True / False)_                   |

## Швидкий старт 📚
1. Щоб встановити бібліотеки в Windows, запустіть INSTALL.bat.
2. Для запуску бота використовуйте `START.bat` (або в консолі: `python main.py`).

## Попередні умови
Перш ніж почати, переконайтеся, що у вас встановлено таке:
- [Python](https://www.python.org/downloads/) версії 3.10 або 3.11.

## Отримання API ключів
1. Перейдіть на сайт [my.telegram.org](https://my.telegram.org) і увійдіть у систему, використовуючи свій номер телефону.
2. Виберіть **"API development tools »** і заповніть форму для реєстрації нового додатка.
3. Запишіть `API_ID` та `API_HASH` в файлі `.env`, надані після реєстрації вашого застосунку.

## Встановлення
Ви можете завантажити [**Репозиторій**](https://github.com/CatSnowdrop/TapSwap) клонуванням на вашу систему і встановленням необхідних залежностей:
```shell
~ >>> git clone https://github.com/CatSnowdrop/TapSwap.git 
~ >>> cd TapSwap

# Linux
~/TapSwap >>> python3 -m venv venv
~/TapSwap >>> source venv/bin/activate
~/TapSwap >>> pip3 install -r requirements.txt
~/TapSwap >>> cp .env-example .env
~/TapSwap >>> nano .env  # Тут ви обов'язково маєте вказати ваші API_ID і API_HASH, решта береться за замовчуванням
~/TapSwap >>> sh install.sh
~/TapSwap >>> python3 main.py

# Windows
~/TapSwap >>> python -m venv venv
~/TapSwap >>> venv\Scripts\activate
~/TapSwap >>> pip install -r requirements.txt
~/TapSwap >>> copy .env-example .env
~/TapSwap >>> # Вказуєте ваші API_ID і API_HASH, решта береться за замовчуванням
~/TapSwap >>> python main.py
```

Також для швидкого запуску ви можете використовувати аргументи, наприклад:
```shell
~/TapSwap >>> python3 main.py --action (1/2/3)
# Або
~/TapSwap >>> python3 main.py -a (1/2/3)

# 1 - Створює сесію
# 2 - Запускає клікер
# 3 - Запуск через Telegram
```