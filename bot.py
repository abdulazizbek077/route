from config import API_TOKEN
from aiogram.dispatcher.filters import Text
from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import *
from aiogram.dispatcher import FSMContext
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from enum import Enum, auto


bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class States(Enum):
    AWAITING_NAME = auto()
    AWAITING_DATE = auto()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS words (
                    "name" TEXT,
                    "date" TEXT,
                    "Разработка грунта вручную м3" TEXT,
                    "Планировка площадей механизированным способом м2" TEXT,
                    "Планировка площадей вручную м2" TEXT,
                    "Устройство подстилающих слоев из ГПС/Щебня м3" TEXT,
                    "Устройство подстилающих слоев из ГПС/щебня вручную м3" TEXT,
                    "Устройство подстилающих слоев из песка м3" TEXT,
                    "Устройство грунтовой подушки м3" TEXT,
                    "Обратная засыпка механизированным способом м3" TEXT,
                    "Обратная засыпка вручную м3" TEXT,
                    "Разработка грунта механизированным способом м3" TEXT,
                    "Устройство бетонной подготовки м3" TEXT,
                    "Устройство железобетонного крыльца м3" TEXT,
                    "Устройство отмостки м3" TEXT,
                    "Опалубочные работы м2" TEXT,
                    "Бетонирование фундаментов м3" TEXT,
                    "Устройство бетонных полов м3" TEXT,
                    "Изготовление арматурных изделий тн" TEXT,
                    "Армирование тн" TEXT,
                    "Изготовление закладных деталей тн" TEXT,
                    "Установка закладных деталей тн" TEXT,
                    "Гидроизоляция обмазочная биткмом/пленка м2" TEXT,
                    "Изготовление металлоконструкций тн" TEXT,
                    "Монтаж металлоконструкций каркасов тн" TEXT,
                    "Монтаж стеновых сэндвинч панелей м2" TEXT,
                    "Монтаж кровельных сэндвинч панелей м2" TEXT,
                    "Монтаж стенового профлиста м2" TEXT,
                    "Монтаж кровельного профлиста м2" TEXT,
                    "Установка металлических оград: Устройство ограждений м" TEXT,
                    "Монтаж металлических ворот и калиток шт" TEXT,
                    "Устройство перегородок гипсокартоном м2" TEXT,
                    "Устройство подвесного потолка гипсокартоном м2" TEXT, 
                    "Облицовка стен гипсокартоном м2" TEXT,
                    "Шпаклевка стен и потолка м2" TEXT,
                    "Окраска стен и потолка водоэмульсионными составами м2" TEXT,
                    "Устройство пола линолеумом м2" TEXT,
                    "Устройство пола керамической плиткой м2" TEXT,
                    "Облицовка стен керамической плиткой м2" TEXT,
                    "Устройство подвесного потолка пластиком/Армстронгом м2" TEXT,
                    "Установка дверных и оконных блоков м2" TEXT,
                    "Кладка кирпичных перегородок м2" TEXT,
                    "Кладка кирпичных стен м3" TEXT,
                    "Устройство стяжек м3" TEXT,
                    "Установка перегородок из типа Akfa м2" TEXT,
                    "Укладка полиэтиленового трубопровода до D40 м" TEXT,
                    "Укладка полиэтиленового трубопровода до D90 м" TEXT,
                    "Укладка полиэтиленового трубопровода до D160 м" TEXT,
                    "Укладка полиэтиленового трубопровода до D450 м" TEXT,
                    "Монтаж сантехприборов шт" TEXT,
                    "Установка смесителей шт" TEXT,
                    "Установка трапов шт" TEXT,
                    "Прокладка кабеля весом до 1 кг с заделкой м" TEXT,
                    "Прокладка кабеля весом до 3 кг с заделкой м" TEXT,
                    "Прокладка кабеля весом до 9 кг с заделкой м" TEXT,
                    "Монтаж заземляющего проводника м" TEXT,
                    "Монтаж прибора: Указатель, Табло шт" TEXT,
                    "Монтаж прибора: Светильник, Лампа, Выключатель, Переключатель, Розетка шт" TEXT,
                    "Монтаж коробки распаячной, ответвительной шт" TEXT,
                    "Монтаж автомата выключателя шт" TEXT,
                    "Монтаж электрического щита шт" TEXT,
                    "Монтаж пластмассового короба м" TEXT,
                    "Прокладка гофрированной трубы до D25 мм м" TEXT
                )''')
conn.commit()

    



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Assalomu alaykum, Ulugbek yaratgan Enter VZIS botimizga xush kelibsiz! Bu bot orqali siz bir kun ichida qilingan hisobotlarni tayyorlash usullari boycha taqdim etishga, imko'niz bo'ladi!", reply_markup=reply_name)

@dp.message_handler(state='*')
async def input_handler(message: types.Message, state: FSMContext):
    if message.text == "Меню":
        await message.reply("Вы зашли в меню",reply_markup=replywork)

    elif message.text == "⬅️Назад в меню":
        await message.answer("Вы вернулись назад в меню!", reply_markup=replywork)

    elif message.text == "Земляные работы":
        await message.answer("Земляные работы", reply_markup=reply_zem_buttons)

    elif message.text == "Бетонные работы":
        await message.answer("Бетонные работы", reply_markup=reply_bet_buttons)

    elif message.text == "Гидроизоляционные работы":
        await message.answer("Гидроизоляционные работы", reply_markup=reply_gid_buttons)

    elif message.text == "Металлоконструкция":
        await message.answer("Металлоконструкция", reply_markup=reply_metal_buttons)

    elif message.text == "Отделочные работы":
        await message.answer("Отделочные работы", reply_markup=reply_otdel_buttons)

    elif message.text == "Трубопроводы":
        await message.answer("Трубопроводы", reply_markup=reply_trubo_buttons)

    elif message.text == "Электромонтажные работы":
        await message.answer("Электромонтажные работы", reply_markup=reply_elect_buttons)

    text = message.text
    if text in ['Разработка грунта вручную м3', 'Планировка площадей механизированным способом м2', 'Планировка площадей вручную м2', 'Устройство подстилающих слоев из ГПС/Щебня м3', 'Устройство подстилающих слоев из ГПС/щебня вручную м3', 'Устройство подстилающих слоев из песка м3', 'Устройство грунтовой подушки м3', 'Обратная засыпка механизированным способом м3', 'Обратная засыпка вручную м3', 'Разработка грунта механизированным способом м3', 'Устройство бетонной подготовки м3', 'Устройство железобетонного крыльца м3', 'Устройство отмостки м3', 'Опалубочные работы м2', 'Бетонирование фундаментов м3', 'Устройство бетонных полов м3', 'Изготовление арматурных изделий тн', 'Армирование тн', 'Изготовление закладных деталей тн', 'Установка закладных деталей тн', 'Гидроизоляция обмазочная биткмом/пленка м2', 'Изготовление металлоконструкций тн', 'Монтаж металлоконструкций каркасов тн', 'Монтаж стеновых сэндвинч панелей м2', 
                
                    "Монтаж кровельных сэндвинч панелей м2",
                    "Монтаж стенового профлиста м2",
                    "Монтаж кровельного профлиста м2",
                    "Установка металлических оград: Устройство ограждений м",
                    "Монтаж металлических ворот и калиток шт",
                    "Устройство перегородок гипсокартоном м2",
                    "Устройство подвесного потолка гипсокартоном м2",
                    "Облицовка стен гипсокартоном м2",
                    "Шпаклевка стен и потолка м2",
                    "Окраска стен и потолка водоэмульсионными составами м2",
                    "Устройство пола линолеумом м2",
                    "Устройство пола керамической плиткой м2",
                    "Облицовка стен керамической плиткой м2",
                    "Устройство подвесного потолка пластиком/Армстронгом м2",
                    "Установка дверных и оконных блоков м2",
                    "Кладка кирпичных перегородок м2",
                    "Кладка кирпичных стен м3",
                    "Устройство стяжек м3",
                    "Установка перегородок из типа Akfa м2",
                    "Укладка полиэтиленового трубопровода до D40 м",
                    "Укладка полиэтиленового трубопровода до D90 м",
                    "Укладка полиэтиленового трубопровода до D160 м",
                    "Укладка полиэтиленового трубопровода до D450 м",
                    "Монтаж сантехприборов шт",
                    "Установка смесителей шт",
                    "Установка трапов шт",
                    "Прокладка кабеля весом до 1 кг с заделкой м",
                    "Прокладка кабеля весом до 3 кг с заделкой м",
                    "Прокладка кабеля весом до 9 кг с заделкой м",
                    "Монтаж заземляющего проводника м",
                    "Монтаж прибора: Указатель, Табло шт",
                    "Монтаж прибора: Светильник, Лампа, Выключатель, Переключатель, Розетка шт",
                    "Монтаж коробки распаячной, ответвительной шт",
                    "Монтаж автомата выключателя шт",
                    "Монтаж электрического щита шт",
                    "Монтаж пластмассового короба м",
                    "Прокладка гофрированной трубы до D25 мм м"

                ]:
        column_name = text
        await message.answer(f"Вы выбрали столбец {column_name}. Пожалуйста, отправьте слово для добавления.")
        # Устанавливаем состояние столбца
        await state.update_data(column_name=column_name)
    elif text == "Закончил ввод📥":
        # Формируем SQL-запрос, чтобы проверить, есть ли хотя бы одно заполненное значение в столбцах
        cursor.execute("SELECT * FROM words WHERE "
                       "\"Разработка грунта механизированным способом м3\" IS NOT NULL OR "
                       "\"Разработка грунта вручную м3\" IS NOT NULL OR "
                       "\"Планировка площадей механизированным способом м2\" IS NOT NULL OR "
                       "\"Планировка площадей вручную м2\" IS NOT NULL OR "
                       "\"Устройство подстилающих слоев из ГПС/Щебня м3\" IS NOT NULL OR "
                       "\"Устройство подстилающих слоев из ГПС/щебня вручную м3\" IS NOT NULL OR "
                       "\"Устройство подстилающих слоев из песка м3\" IS NOT NULL OR "
                       "\"Устройство грунтовой подушки м3\" IS NOT NULL OR "
                       "\"Обратная засыпка механизированным способом м3\" IS NOT NULL OR "
                       "\"Обратная засыпка вручную м3\" IS NOT NULL OR "
                       "\"Разработка грунта механизированным способом м3\" IS NOT NULL OR "
                       "\"Устройство бетонной подготовки м3\" IS NOT NULL OR "
                       "\"Устройство железобетонного крыльца м3\" IS NOT NULL OR "
                       "\"Устройство отмостки м3\" IS NOT NULL OR "
                       "\"Опалубочные работы м2\" IS NOT NULL OR "
                       "\"Бетонирование фундаментов м3\" IS NOT NULL OR "
                       "\"Устройство бетонных полов м3\" IS NOT NULL OR "
                       "\"Изготовление арматурных изделий тн\" IS NOT NULL OR "
                       "\"Армирование тн\" IS NOT NULL OR "
                       "\"Изготовление закладных деталей тн\" IS NOT NULL OR "
                       "\"Установка закладных деталей тн\" IS NOT NULL OR "
                       "\"Гидроизоляция обмазочная биткмом/пленка м2\" IS NOT NULL OR "
                       "\"Изготовление металлоконструкций тн\" IS NOT NULL OR "
                       "\"Монтаж металлоконструкций каркасов тн\" IS NOT NULL OR "
                       "\"Монтаж стеновых сэндвинч панелей м2\" IS NOT NULL OR "
                       "\"Монтаж кровельных сэндвинч панелей м2\" IS NOT NULL OR "
                       "\"Монтаж стенового профлиста м2\" IS NOT NULL OR "
                       "\"Монтаж кровельного профлиста м2\" IS NOT NULL OR "
                       "\"Установка металлических оград: Устройство ограждений м\" IS NOT NULL OR "
                       "\"Монтаж металлических ворот и калиток шт\" IS NOT NULL OR "
                       "\"Устройство перегородок гипсокартоном м2\" IS NOT NULL OR "
                       "\"Устройство подвесного потолка гипсокартоном м2\" IS NOT NULL OR "
                       "\"Облицовка стен гипсокартоном м2\" IS NOT NULL OR "
                       "\"Шпаклевка стен и потолка м2\" IS NOT NULL OR "
                       "\"Окраска стен и потолка водоэмульсионными составами м2\" IS NOT NULL OR "
                       "\"Устройство пола линолеумом м2\" IS NOT NULL OR "
                       "\"Устройство пола керамической плиткой м2\" IS NOT NULL OR "
                       "\"Облицовка стен керамической плиткой м2\" IS NOT NULL OR "
                       "\"Устройство подвесного потолка пластиком/Армстронгом м2\" IS NOT NULL OR "
                       "\"Установка дверных и оконных блоков м2\" IS NOT NULL OR "
                       "\"Кладка кирпичных перегородок м2\" IS NOT NULL OR "
                       "\"Кладка кирпичных стен м3\" IS NOT NULL OR "
                       "\"Устройство стяжек м3\" IS NOT NULL OR "
                       "\"Установка перегородок из типа Akfa м2\" IS NOT NULL OR "
                       "\"Укладка полиэтиленового трубопровода до D40 м\" IS NOT NULL OR "
                       "\"Укладка полиэтиленового трубопровода до D90 м\" IS NOT NULL OR "
                       "\"Укладка полиэтиленового трубопровода до D160 м\" IS NOT NULL OR "
                       "\"Укладка полиэтиленового трубопровода до D450 м\" IS NOT NULL OR "
                       "\"Монтаж сантехприборов шт\" IS NOT NULL OR "
                       "\"Установка смесителей шт\" IS NOT NULL OR "
                       "\"Установка трапов шт\" IS NOT NULL OR "
                       "\"Прокладка кабеля весом до 1 кг с заделкой м\" IS NOT NULL OR "
                       "\"Прокладка кабеля весом до 3 кг с заделкой м\" IS NOT NULL OR "
                       "\"Прокладка кабеля весом до 9 кг с заделкой м\" IS NOT NULL OR "
                       "\"Монтаж заземляющего проводника м\" IS NOT NULL OR "
                       "\"Монтаж прибора: Указатель, Табло шт\" IS NOT NULL OR "
                       "\"Монтаж прибора: Светильник, Лампа, Выключатель, Переключатель, Розетка шт\" IS NOT NULL OR "
                       "\"Монтаж коробки распаячной, ответвительной шт\" IS NOT NULL OR "
                       "\"Монтаж автомата выключателя шт\" IS NOT NULL OR "
                       "\"Монтаж электрического щита шт\" IS NOT NULL OR "
                       "\"Монтаж пластмассового короба м\" IS NOT NULL OR "
                       "\"Прокладка гофрированной трубы до D25 мм м\" IS NOT NULL")
        result = cursor.fetchone()
        if result:
            # Получаем данные из столбцов name и date
            cursor.execute("SELECT name FROM words")
            name = cursor.fetchone()
            name = name[0] if name is not None else "не указано"
            cursor.execute("SELECT date FROM words")
            date = cursor.fetchone()
            date = date[0] if date is not None else "не указана"
            
            # Получаем список столбцов из базы данных
            cursor.execute("SELECT * FROM words")
            columns = [description[0] for description in cursor.description]
            
            # Формируем сообщение со всеми данными из заполненных столбцов
            data = ""
            for column in columns[2:]:
                cursor.execute(f"SELECT \"{column}\" FROM words WHERE \"{column}\" IS NOT NULL")
                result = cursor.fetchone()
                if result:
                    data += f"✔️ {column}: {result[0]}\n"
                    
            # Отправляем сообщение с данными
            await message.answer(f"Ежедневный отчет СМР ВЗиС по проекту {name} за {date} \n \n {data}", reply_markup=reply_name)
        else:
            await message.answer("К сожалению, все столбцы пусты.")
    elif 'column_name' in (data := await state.get_data()):
        word = text
        cursor.execute(f"INSERT INTO words (\"{data['column_name']}\") VALUES (?)", (word,))
        conn.commit()
        await state.finish()
        await message.answer(f"'{word}' добавлено в {data['column_name']}.")
    elif text == "Удалить предедуший отчёт":
        # Удаляем все строки из таблицы
        cursor.execute("DELETE FROM words")
        conn.commit()
        await message.answer("Все данные удалены.", reply_markup=reply_name)
    elif text == "Добавить название проекта(обязательно)":
        await state.update_data(waiting_for_name=True)
        await message.answer("Введите имя проекта:")

    elif 'waiting_for_name' in (data := await state.get_data()):
        name = text
        cursor.execute("INSERT INTO `words` (`name`) VALUES (?)", (name,))
        conn.commit()
        await state.finish()
        await message.answer(f"Имя проекта '{name}' добавлено!")

    elif text == "Добавить дату(обязательно)":
        await state.update_data(waiting_for_date=True)
        await message.answer("Введите дату:")

    elif 'waiting_for_date' in (data := await state.get_data()):
        date = text
        cursor.execute("UPDATE words SET date = ?", (date,))
        conn.commit()
        await state.finish()
        await message.answer(f"Дата '{date}' добавлена!", reply_markup=replymenu)



    
    


    




    
            






async def main():
    # Запуск бота
    await dp.start_polling()
    # Блокировка до остановки бота
    await asyncio.sleep(1000000)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())




async def main():
    # Запуск бота
    await dp.start_polling()
    # Блокировка до остановки бота
    await asyncio.sleep(1000000)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())