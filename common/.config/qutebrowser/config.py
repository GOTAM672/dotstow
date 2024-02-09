# import subprocess
# import os
# from qutebrowser.api import interceptor

# Autogenerated config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)


# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set("content.cookies.accept", "all", "chrome-devtools://*")

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set("content.cookies.accept", "all", "devtools://*")

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set("content.headers.accept_language", "", "https://matchmaker.krunker.io/*")

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
    "https://web.whatsapp.com/",
)

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0",
    "https://accounts.google.com/*",
)

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36",
    "https://*.slack.com/*",
)

# Which method of blocking ads should be used.  Support for Adblock Plus
# (ABP) syntax blocklists using Brave's Rust library requires the
# `adblock` Python package to be installed, which is an optional
# dependency of qutebrowser. It is required when either `adblock` or
# `both` are selected.
# Type: String
# Valid values:
#   - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
#   - adblock: Use Brave's ABP-style adblocker
#   - hosts: Use hosts blocking
#   - both: Use both hosts blocking and Brave's ABP-style adblocker
c.content.blocking.method = "both"

# Load images automatically in web pages.
# Type: Bool
config.set("content.images", True, "chrome-devtools://*")

# Load images automatically in web pages.
# Type: Bool
config.set("content.images", True, "devtools://*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "chrome-devtools://*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "devtools://*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "chrome://*/*")

# Enable JavaScript.
# Type: Bool
config.set("content.javascript.enabled", True, "qute://*/*")

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set("content.notifications.enabled", False, "https://www.reddit.com")


# config.set('colors.webpage.darkmode.enabled', True)
config.set("zoom.default", 120)
# config.bind(',sl','set colors.webpage.darkmode.enabled true')
# c.content.user_stylesheets = ['~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css']
config.bind("M", "hint links spawn mpv --ytdl-format=best {hint-url}")
# config.bind('M', "hint links spawn zsh -c \"mpv --audio-file=<(yt-dlp '{hint-url}' -o -) <(yt-dlp '{hint-url}' -o -)\"")
config.bind("Z", "hint links spawn kitty -e yt-dlp {hint-url}")
config.bind("t", "cmd-set-text -s :open -t")
config.bind("xb", "config-cycle statusbar.show always never")
config.bind("xt", "config-cycle tabs.show always never")
config.bind(
    "xx",
    "config-cycle statusbar.show always never;; config-cycle tabs.show always never",
)
# config.bind(',ap', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""')
# config.bind(',dr', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""')
# config.bind(',gr', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""')
# config.bind(',sd', 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""')
config.bind(
    ",sl",
    'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-light-all-sites.css ""',
)
config.bind("<Ctrl-g>", "mode-leave", mode="insert")
config.bind("<Ctrl-g>", "mode-leave", mode="hint")
config.bind("<Ctrl-g>", "mode-leave", mode="command")
config.bind("<Ctrl-g>", "mode-leave", mode="caret")
config.bind("<Ctrl-r>", "config-source")
# config.bind('<Ctrl-g>', 'mode-enter normal', mode='insert')
# config.bind('<Ctrl-g>', 'mode-enter normal', mode='hint')

# for enabling and disabling darkmode
c.aliases["dr"] = "spawn --userscript darkreader.py enable domain"
c.aliases["drd"] = "spawn --userscript darkreader.py disable domain"
c.aliases["darkreader"] = "spawn --userscript darkreader.py"
config.bind(",d", "cmd-set-text -s :darkreader enable '{url}*' 100 100 0")
config.bind(",r", "cmd-set-text -s :darkreader disable '{url}*'")
c.url.default_page = "file:///home/swaroop/.config/qutebrowser/homepage/homepage.html"
c.url.start_pages = "file:///home/swaroop/.config/qutebrowser/homepage/homepage.html"
c.auto_save.session = True


c.url.searchengines = {
    "DEFAULT": "https://google.com/search?hl=en&q={}",
    "!a": "https://www.amazon.com/s?k={}",
    "!d": "https://duckduckgo.com/?ia=web&q={}",
    "!dd": "https://thefreedictionary.com/{}",
    "!gh": "https://github.com/search?o=desc&q={}&s=stars",
    "!gist": "https://gist.github.com/search?q={}",
    "!gi": "https://www.google.com/search?tbm=isch&q={}&tbs=imgo:1",
    "!m": "https://www.google.com/maps/search/{}",
    "!p": "https://pry.sh/{}",
    "!r": "https://www.reddit.com/search?q={}",
    "!w": "https://en.wikipedia.org/wiki/{}",
    "yt": "https://www.youtube.com/results?search_query={}",
}

config.source('themes/gruvbox.py')
# config.source('themes/custom1.py')
# config.source("themes/citylights.py")

c.colors.webpage.preferred_color_scheme = "dark"
# c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.darkmode.algorithm = "brightness-rgb"
# c.colors.webpage.darkmode.contrast = 0.0
c.colors.webpage.darkmode.contrast = 0.9
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.grayscale.all = False
c.colors.webpage.darkmode.grayscale.images = 0.0
c.colors.webpage.darkmode.policy.images = "smart"
c.colors.webpage.darkmode.policy.page = "smart"
# c.colors.webpage.darkmode.threshold.background = 128
c.colors.webpage.darkmode.threshold.background = 128
c.colors.webpage.darkmode.threshold.text = 128



config.bind(
    "]", "jseval --quiet document.querySelector('video, audio').playbackRate += 0.5"
)
config.bind(
    "[", "jseval --quiet document.querySelector('video, audio').playbackRate -= 0.5"
)
# config.bind('p', "jseval --quiet document.getElementsByTagName('video')[0].pause()", mode="insert")
# config.bind('k', "jseval --quiet document.getElementsByTagName('video')[0].play()", mode="insert")
# config.bind('k', "jseval --quiet document.querySelectorAll('video').forEach((video) => { video.addEventListener('keydown', function (keypressed)  if (this.paused && keypressed.keyCode==75){  this.play(); }else if (this.playing && keypressed.keyCode==75){  this.pause();});});", mode="insert")

# config.bind('|', "jseval --quiet document.querySelector('video, audio').pause")


# ======================= Redline Insert Mode ============= {{{
# Awesome way to open vim from qutebrowser
# c.editor.command = [
#     os.environ["TERMINAL"],
#     "-e",
#     os.environ["EDITOR"],
#     "-f",
#     "{file}",
#     "-c",
#     "normal {line}G{column0}1",
# ]

# Binds for moving through completion items
config.bind("<Ctrl-j>", "completion-item-focus next", mode="command")
config.bind("<Ctrl-k>", "completion-item-focus prev", mode="command")
config.bind("<Shift-k>", "tab-next", mode="normal")
config.bind("<Shift-j>", "tab-prev", mode="normal")

config.bind("<Ctrl-h>", "fake-key <Backspace>", "insert")
config.bind("<Ctrl-a>", "fake-key <Home>", "insert")
config.bind("<Ctrl-e>", "fake-key <End>", "insert")
config.bind("<Ctrl-b>", "fake-key <Left>", "insert")
# config.bind("<Mod1-b>", "fake-key <Ctrl-Left>", "insert")
config.bind("<Ctrl-Shift-b>", "fake-key <Ctrl-Left>", "insert")
config.bind("<Ctrl-f>", "fake-key <Right>", "insert")
# config.bind("<Mod1-f>", "fake-key <Ctrl-Right>", "insert")
config.bind("<Ctrl-Shift-f>", "fake-key <Ctrl-Right>", "insert")
config.bind("<Ctrl-p>", "fake-key <Up>", "insert")
config.bind("<Ctrl-n>", "fake-key <Down>", "insert")
# config.bind("<Mod1-d>", "fake-key <Ctrl-Delete>", "insert")
config.bind("<Ctrl-Shift-d>", "fake-key <Ctrl-Delete>", "insert")
config.bind("<Ctrl-d>", "fake-key <Delete>", "insert")
config.bind("<Ctrl-w>", "fake-key <Ctrl-Backspace>", "insert")
config.bind("<Ctrl-u>", "fake-key <Shift-Home><Delete>", "insert")
config.bind("<Ctrl-k>", "fake-key <Shift-End><Delete>", "insert")
config.bind("<Ctrl-x><Ctrl-e>", "open-editor", "insert")



