from pyrogram import Client
from pyrogram.types import CallbackQuery
from ... import custom_filters
from ..common import list_active_torrents, send_menu


@Client.on_callback_query(custom_filters.list_filter & custom_filters.check_user_filter)
async def list_callback(client: Client, callback_query: CallbackQuery) -> None:
    await list_active_torrents(client, callback_query.from_user.id, callback_query.message.id)


@Client.on_callback_query(custom_filters.list_by_status_filter & custom_filters.check_user_filter)
async def list_by_status_callback(client: Client, callback_query: CallbackQuery) -> None:
    status_filter = callback_query.data.split("#")[1]
    await list_active_torrents(client, callback_query.from_user.id, callback_query.message.id, status_filter=status_filter)

@Client.on_callback_query(custom_filters.list_page_down_filter & custom_filters.check_user_filter)
async def list_page_down_callback(client: Client, callback_query: CallbackQuery) -> None:
    current_range_info = callback_query.data.split("#")[1].split(",")
    show_range = [int(current_range_info[1]), min(int(current_range_info[1])+10, int(current_range_info[2]))] #show next 10 or remaining
    #show_range = [show_range[0], show_range[1]]
    await list_active_torrents(client, callback_query.from_user.id, callback_query.message.id, show_range=show_range)

@Client.on_callback_query(custom_filters.list_page_up_filter & custom_filters.check_user_filter)
async def list_page_up_callback(client: Client, callback_query: CallbackQuery) -> None:
    current_range_info = callback_query.data.split("#")[1].split(",")
    # show_range = [max(current_range_info[0]-10, 0), current_range_info[1]-1]
    show_range = [max(int(current_range_info[0])-10, 0), int(current_range_info[0])]
    pass
    await list_active_torrents(client, callback_query.from_user.id, callback_query.message.id, show_range=show_range)

@Client.on_callback_query(custom_filters.menu_filter & custom_filters.check_user_filter)
async def menu_callback(client: Client, callback_query: CallbackQuery) -> None:
    await send_menu(client, callback_query.message.id, callback_query.from_user.id)
