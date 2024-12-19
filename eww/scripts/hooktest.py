from libqtile import hook
from time import sleep


@hook.subscribe.focus_change
def hook_trigger(x):
    print("hook triggered")


while True:
    sleep(0.1)
