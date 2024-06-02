from aiogram import Router, F, types

from loader import db

lessons = Router()


def extracter(all_medias, delimiter):
    empty_list = []
    for e in range(0, len(all_medias), delimiter):
        empty_list.append(all_medias[e:e + delimiter])
    return empty_list


@lessons.callback_query(F.data.startswith("table:"))
async def lessons_hr_one(call: types.CallbackQuery):
    table_id = int(call.data.split(":")[1])
    select_table = await db.select_all_media(table_name=f"medias_table{table_id}")
    print(select_table)
