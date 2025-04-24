import pytest
from television import Television

def test_initial_state():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_toggle():
    tv = Television()
    tv.power()
    assert str(tv).startswith("Power = True")
    tv.power()
    assert str(tv).startswith("Power = False")

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Volume = 0" in str(tv)
    tv.mute()
    assert "Volume = 1" in str(tv)

def test_channel_up_wrap():
    tv = Television()
    tv.power()
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_down_wrap():
    tv = Television()
    tv.power()
    tv._Television__channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert f"Channel = {Television.MAX_CHANNEL}" in str(tv)

def test_volume_up_limit():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()  # should not exceed MAX_VOLUME
    assert f"Volume = {Television.MAX_VOLUME}" in str(tv)

def test_volume_down_limit():
    tv = Television()
    tv.power()
    tv.volume_down()  # already at MIN_VOLUME
    assert f"Volume = {Television.MIN_VOLUME}" in str(tv)

def test_volume_unmutes_tv():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert "Volume = 1" in str(tv)

def test_channel_change_when_off():
    tv = Television()
    tv.channel_up()
    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)

def test_volume_change_when_off():
    tv = Television()
    tv.volume_up()
    assert "Volume = 0" in str(tv)
