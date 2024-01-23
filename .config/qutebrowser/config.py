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
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

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
config.set('content.cookies.accept', 'all', 'devtools://*')

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

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
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

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
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Allow JavaScript to read from or write to the clipboard. With
# QtWebEngine, writing the clipboard as response to a user interaction
# is always allowed.
# Type: String
# Valid values:
#   - none: Disable access to clipboard.
#   - access: Allow reading from and writing to the clipboard.
#   - access-paste: Allow accessing the clipboard and pasting clipboard content.
c.content.javascript.clipboard = 'access-paste'

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow locally loaded documents to access remote URLs.
# Type: Bool
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/igortxra/.local/share/qutebrowser/userscripts/*')

# Allow locally loaded documents to access other local URLs.
# Type: Bool
config.set('content.local_content_can_access_file_urls', False, 'file:///home/igortxra/.local/share/qutebrowser/userscripts/*')

# CSS border value for hints.
# Type: String
c.hints.border = '1px solid #181825'

# How to behave when the last tab is closed. If the
# `tabs.tabs_are_windows` setting is set, this is ignored and the
# behavior is always identical to the `close` value.
# Type: String
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = 'close'

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://github.com'

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#a6adc8'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#11111b'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#181825'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#a6e3a1'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#1e1e2e'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#9399b2'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#181825'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#cdd6f4'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#585b70'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#585b70'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#585b70'

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = '#f5e0dc'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#cdd6f4'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#585b70'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#11111b'

# Background color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.bg = '#1e1e2e'

# Foreground color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.fg = '#cdd6f4'

# Background color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.bg = '#6c7086'

# Foreground color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.fg = '#f5e0dc'

# Background color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.bg = '#181825'

# Foreground color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.fg = '#6c7086'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#1e1e2e'

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = '#89b4fa'

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = '#1e1e2e'

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = '#a6e3a1'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#1e1e2e'

# Color gradient interpolation system for download text.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.fg = 'none'

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#f38ba8'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#1e1e2e'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#181825'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#fab387'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#bac2de'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#cdd6f4'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#bac2de'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#181825'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#f38ba8'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#6c7086'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#181825'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#fab387'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#6c7086'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#181825'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#cdd6f4'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#6c7086'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#181825'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#cdd6f4'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '1px solid #6c7086'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#181825'

# Foreground color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.fg = '#f5e0dc'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#585b70'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#cdd6f4'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#1e1e2e'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#f5e0dc'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#11111b'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#fab387'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#1e1e2e'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#bac2de'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#181825'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#cdd6f4'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#1e1e2e'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#bac2de'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#1e1e2e'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#fab387'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#1e1e2e'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#fab387'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#1e1e2e'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#1e1e2e'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#cdd6f4'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#f38ba8'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#89dceb'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#94e2d5'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#a6e3a1'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#f9e2af'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#11111b'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#f38ba8'

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#9399b2'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#45475a'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#9399b2'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#585b70'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#cdd6f4'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#1e1e2e'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#cdd6f4'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#1e1e2e'

# Background color for webpages if unset (or empty to use the theme's
# color).
# Type: QtColor
c.colors.webpage.bg = '#1e1e2e'


c.url.searchengines = {'DEFAULT': 'https://start.duckduckgo.com/?q={}', 'aw': 'https://wiki.archlinux.org/?search={}', 'goog': 'https://www.google.com/search?q={}', 're': 'https://www.reddit.com/search?q={}', 'gh': 'https://github.com/search?q={}', 'ghr': 'https://github.com/{unquoted}', 'wiki': 'https://en.wikipedia.org/wiki/{}', 'yt': 'https://www.youtube.com/results?search_query={}', 'qtile': 'http://docs.qtile.org/en/stable/search.html?q={}'}
