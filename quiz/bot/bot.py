from abc import ABC, abstractmethod
from typing import Any, Iterable, Callable
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from quiz.bot.message.voice import BotVoiceMessage, VoiceMessage
from quiz.config import Config


class Bot(ABC):
    """Abstract interface for a bot."""

    @abstractmethod
    def message_handler(
        self,
        commands: Iterable[str] = None,
        regexp: str = None,
        func: Callable = None,
        content_types: Iterable[str] = "text",
        **kwargs: Any,
    ) -> Any:
        pass

    @abstractmethod
    def send_message(
        self,
        chat_id: int,
        text: str,
        disable_web_page_preview: bool = None,
        reply_to_message_id: int = None,
        reply_markup: ReplyKeyboardRemove = None,
        parse_mode: str = None,
        disable_notification: bool = None,
    ) -> Message:
        pass

    @abstractmethod
    def send_voice(
        self,
        chat_id: int,
        voice: Any,
        caption: str = None,
        duration: int = None,
        reply_to_message_id: int = None,
        reply_markup: ReplyKeyboardMarkup = None,
        parse_mode: str = None,
        disable_notification: bool = None,
        timeout: int = None,
    ) -> VoiceMessage:
        pass

    @abstractmethod
    def polling(self, none_stop: bool = False, interval: int = 0, timeout: int = 20) -> None:
        pass


class QuizBot(Bot):
    """Quiz melody bot implementation."""

    def __init__(self) -> None:
        self._bot: TeleBot = TeleBot(Config.token)

    def message_handler(
        self,
        commands: Iterable[str] = None,
        regexp: str = None,
        func: Callable = None,
        content_types: Iterable[str] = "text",
        **kwargs: Any,
    ) -> Any:

        return self._bot.message_handler(commands, regexp, func, content_types, **kwargs)

    def send_message(
        self,
        chat_id: int,
        text: str,
        disable_web_page_preview: bool = None,
        reply_to_message_id: int = None,
        reply_markup: ReplyKeyboardRemove = None,
        parse_mode: str = None,
        disable_notification: bool = None,
    ) -> Message:

        return self._bot.send_message(
            chat_id, text, disable_notification, reply_to_message_id, reply_markup, parse_mode, disable_notification
        )

    def send_voice(
        self,
        chat_id: int,
        voice: Any,
        caption: str = None,
        duration: int = None,
        reply_to_message_id: int = None,
        reply_markup: bool = None,
        parse_mode: str = None,
        disable_notification: bool = None,
        timeout: int = None,
    ) -> VoiceMessage:

        return BotVoiceMessage(
            self._bot.send_voice(
                chat_id,
                voice,
                caption,
                duration,
                reply_to_message_id,
                reply_markup,
                parse_mode,
                disable_notification,
                timeout,
            )
        )

    def polling(self, none_stop: bool = False, interval: int = 0, timeout: int = 20) -> None:
        self._bot.polling(none_stop, interval, timeout)
