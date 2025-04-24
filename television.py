#class
class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

#initial TV settings
    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

# set power
    def power(self) -> None:
        self.__status = not self.__status

# mute status
    def mute(self) -> None:
        if self.__status:
            self.__muted = not self.__muted

# move up channel
    def channel_up(self) -> None:
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

# move down channel
    def channel_down(self) -> None:
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

#turn volume up
    def volume_up(self) -> None:
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            if self.__muted:
                self.__muted = False

#turn volume down
    def volume_down(self) -> None:
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            if self.__muted:
                self.__muted = False

#return to initial settings
    def __str__(self) -> str:
        vol = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {vol}"
