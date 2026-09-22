# hundred_cats/async_download_cats.py

from datetime import datetime
import asyncio

import aiohttp

URL = 'https://api.thecatapi.com/v1/images/search'


# Асинхронная функция для получения нового изображения.
async def get_new_image_url():
    # Создать асинхронную сессию для выполнения HTTP-запроса.
    async with aiohttp.ClientSession() as session:
        # Выполнить асинхронный GET-запрос на указанный URL.
        response = await session.get(URL)
        # Асинхронно получить тело ответа в формате JSON.
        data = await response.json()
        # Извлечь URL случайного изображения из ответа.
        random_cat = data[0]['url']
        # Напечатать URL изображения.
        print(random_cat)
        # Вернуть URL изображения.
        return random_cat


# Главная асинхронная функция.
async def main():
    # Создать список задач для асинхронного выполнения.
    tasks = [
        # Асинхронно выполнить функцию get_new_image_url() 100 раз.
        asyncio.ensure_future(get_new_image_url()) for _ in range(100)
    ]
    # Подождать, пока выполнятся все задачи.
    await asyncio.wait(tasks)

# Точка входа в программу.
if __name__ == '__main__':
    # Записать текущее время начала выполнения программы.
    start_time = datetime.now()

    # Получить текущий событийный цикл.
    loop = asyncio.get_event_loop()
    # Запустить основную корутину и подождать, пока она завершится.
    loop.run_until_complete(main())

    # Записать текущее время окончания выполнения программы.
    end_time = datetime.now()
    # Напечатать время выполнения программы.
    print(f'Время выполнения программы: {end_time - start_time}.')
