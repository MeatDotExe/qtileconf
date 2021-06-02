from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
     ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "a", lazy.layout.left()),
    ([mod], "s", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "a", lazy.layout.grow()),
    ([mod, "shift"], "s", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # File Explorer
    ([mod], "e", lazy.spawn("nemo")),	

    # Apps
    ([mod], "x", lazy.spawn("discord")),
    	
    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # Compositor 
    ([mod, "shift"], "p", lazy.spawn("xcompmgr -c -t-5 -l-5 -r4.2 -o.55 ")),
    ([mod, "shift"], "o", lazy.spawn("killall xcompmgr")),
    

]]
