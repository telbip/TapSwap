import asyncio
import argparse
from itertools import cycle
import glob
from pyrogram import Client, compose
import os
from better_proxy import Proxy
from bot.config import settings
from bot.utils import logger
from bot.core.tapper import run_tapper
from bot.utils.accounts import Accounts
from bot.core.registrator import register_sessions
banner = """

▀▀█▀▀ █▀▀█ █▀▀█ ░█▀▀▀█ █   █ █▀▀█ █▀▀█ ░█▀▀█ █▀▀█ ▀▀█▀▀
 ░█   █▄▄█ █  █  ▀▀▀▄▄ █▄█▄█ █▄▄█ █  █ ░█▀▀▄ █  █   █
 ░█   ▀  ▀ █▀▀▀ ░█▄▄▄█  ▀ ▀  ▀  ▀ █▀▀▀ ░█▄▄█ ▀▀▀▀   ▀

"""

options = """
Select an action:

    1. Create session
    2. Run clicker
    3. Run via Telegram (Beta)
"""


global tg_clients

def get_proxy(raw_proxy: str) -> Proxy:
    return Proxy.from_str(proxy=raw_proxy).as_url if raw_proxy else None
    
def get_session_names() -> list[str]:
    session_names = sorted(glob.glob("sessions/*.session"))
    session_names = [
        os.path.splitext(os.path.basename(file))[0] for file in session_names
    ]

    return session_names


async def get_tg_clients() -> list[Client]:
    global tg_clients

    session_names = get_session_names()

    if not session_names:
        raise FileNotFoundError("Not found session files")

    if not settings.API_ID or not settings.API_HASH:
        raise ValueError("API_ID and API_HASH not found in the .env file.")

    tg_clients = [
        Client(
            name=session_name,
            api_id=settings.API_ID,
            api_hash=settings.API_HASH,
            workdir="sessions/",
            plugins=dict(root="bot/plugins"),
        )
        for session_name in session_names
    ]

    return tg_clients

async def get_proxies() -> list[str]:
    accounts = Accounts()
    account_list = await accounts.get_accounts()
    return [account['proxy'] for account in account_list if 'proxy' in account]

async def process() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", type=int, help="Action to perform")

    print(banner)

    logger.info(f"Detected {len(get_session_names())} sessions | {len(await get_proxies())} proxies")

    action = parser.parse_args().action

    if not action:
        print(options)

        while True:
            action = input("> ")

            if not action.isdigit():
                logger.warning("Action must be number")
            elif action not in ["1", "2", "3"]:
                logger.warning("Action must be 1, 2 or 3")
            else:
                action = int(action)
                break

    if action == 1:
        await register_sessions()
    elif action == 2:
        tg_clients = await get_tg_clients()

        await run_tasks(tg_clients=tg_clients)
    elif action == 3:
        tg_clients = await get_tg_clients()

        logger.info("Send /help command in Saved Messages\n")

        await compose(tg_clients)


async def run_tasks(tg_clients: list[Client]):
    lock = asyncio.Lock()
    accounts = await Accounts().get_accounts()

    session_proxies = {account["session_name"]: account.get("proxy", None) for account in accounts}
    tasks = [
        asyncio.create_task(
            run_tapper(
                tg_client=tg_client,
                proxy=session_proxies.get(tg_client.name, None),
                lock=lock,
            )
        )
        for tg_client in tg_clients
    ]

    await asyncio.gather(*tasks)
