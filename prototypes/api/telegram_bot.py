from collections.abc import Callable


def run_bot(reply: Callable[[int, str], str]) -> None:
    """Точка подключения Telegram. Задачи A1–A3 описаны в инструкции."""
    raise SystemExit("Telegram ещё не подключён. Для проверки скелета вызовите gemini.reply.")
