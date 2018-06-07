#  |||||||||||     ||||||||     |\\       ||  ||||||||||||
# ||||           ||||||||||||   ||\\      ||  ||
#|||            ||||      ||||  || \\     ||  ||
#||             |||        |||  ||  \\    ||  ||
#||             |||        |||  ||   \\   ||  ||||||||
#||             |||        |||  ||    \\  ||  ||
#||             |||        |||  ||     \\ ||  ||
#|||            ||||      ||||  ||      \\||  ||
# ||||           ||||||||||||   ||       \||  ||
#  |||||||||||     ||||||||     ||        \|  ||


material = {
    'blue_ink': '#1c1f26',
    'blue_grey': '#273338',
    'grey_blue': '#36454d',
    'base01': '#e5e9f0',
    'base00': '#d8dee9',
    'base0': '#4c566a',
    'base1': '#5e81ac',
    'base2': '#eee8d5',
    'white': '#F9FAF9', #eceff4',
    'yellow_bold': '#eead0e',
    'yellow_light': '#bdbd5a',
    'tomato': '#e6685d',
    'red': '#df342a',
    'magenta': '#df342a',
    'teal': '#16a085',
    'blue': '#57bbd1',
    'cyan': '#88c0d0',
    'green': '#27ad27', #a3be8c
    'grey': '#c9bbae',
}
## Qutebrowser uses 10pt Monospace fonts as the default.
## This overrides the default fonts with they value assigned
c.fonts.monospace = 'Source Code Pro Regular'

## Background color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.bg = material['blue_ink']

## Bottom border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.bottom = material['blue_ink']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.top = material['blue_ink']

## Foreground color of completion widget category headers. The font type is also available for edit
## Type: QtColor
c.colors.completion.category.fg = material['white']
#c.fonts.completion.category = '10pt Source Code Pro Bold'

## Background color of the completion widget for even rows.
## Type: QssColor
c.colors.completion.even.bg = material['blue_grey']

## Text color of the completion widget. The font type is also available for edit. 
## A list of 3 values corresponds to the 3 sections of the completion widget text.
## Type: QtColor
c.colors.completion.fg = [material['white'], material['grey'], material['teal']]
#c.fonts.completion.entry = '10pt Source Code Pro Regular' # ['bold 10pt monospace', '10pt monospace', 'bold 10pt monospace']

## Background color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.bg = material['grey_blue']

## Bottom border color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.border.bottom = material['grey_blue']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.item.selected.border.top = material['grey_blue']

## Foreground color of the selected completion item.
## Type: QtColor
c.colors.completion.item.selected.fg = material['white']

## Foreground color of the matched text in the completion.
## Type: QssColor
c.colors.completion.match.fg = material['yellow_bold']

## Background color of the completion widget for odd rows.
## Type: QssColor
c.colors.completion.odd.bg = material['blue_grey']

## Color of the scrollbar in completion view
## Type: QssColor
c.colors.completion.scrollbar.bg = '#2a2f35' #material['blue_grey']

## Color of the scrollbar handle in completion view.
## Type: QssColor
c.colors.completion.scrollbar.fg =  material['grey_blue'] #material['base2']

## Background color for the download bar.
## Type: QssColor
c.colors.downloads.bar.bg = material['blue_ink']

## Background color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.bg = material['red']

## Foreground color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.fg = material['white']

## Color gradient start for download backgrounds.
## Type: QtColor
# c.colors.downloads.start.bg = '#0000aa'

## Color gradient start for download text.
## Type: QtColor
c.colors.downloads.start.fg = material['white']

## Color gradient stop for download backgrounds.
## Type: QtColor
# c.colors.downloads.stop.bg = '#00aa00'

## Color gradient end for download text.
## Type: QtColor
# c.colors.downloads.stop.fg = material['white']

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.downloads.system.bg = 'rgb'

## Color gradient interpolation system for download text.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.downloads.system.fg = 'rgb'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
c.colors.hints.bg = material['yellow_bold']

## Font color for hints.
## Type: QssColor
c.colors.hints.fg = material['blue_ink'] #'white' #mod

## Font color for the matched part of hints.
## Type: QssColor
c.colors.hints.match.fg = material['yellow_bold']

## Background color of the keyhint widget.
## Type: QssColor
# c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'

## Text color for the keyhint widget.
## Type: QssColor
c.colors.keyhint.fg = material['white']

## Highlight color for keys to complete the current keychain.
## Type: QssColor
c.colors.keyhint.suffix.fg = material['yellow_bold']

## Background color of an error message.
## Type: QssColor
c.colors.messages.error.bg = material['red']

## Border color of an error message.
## Type: QssColor
c.colors.messages.error.border = material['red']

## Foreground color of an error message.
## Type: QssColor
c.colors.messages.error.fg = material['white']

## Background color of an info message.
## Type: QssColor
c.colors.messages.info.bg = material['yellow_light']

## Border color of an info message.
## Type: QssColor
c.colors.messages.info.border = material['yellow_light']

## Foreground color an info message.
## Type: QssColor
c.colors.messages.info.fg = material['blue_ink']

## Background color of a warning message.
## Type: QssColor
c.colors.messages.warning.bg = material['tomato']

## Border color of a warning message.
## Type: QssColor
c.colors.messages.warning.border = material['tomato']

## Foreground color a warning message.
## Type: QssColor
c.colors.messages.warning.fg = material['white']

## Background color for prompts.
## Type: QssColor
c.colors.prompts.bg = material['blue_grey']

## Border used around UI elements in prompts.
## Type: String
c.colors.prompts.border = '1px solid ' + material['white']

## Foreground color for prompts.
## Type: QssColor
c.colors.prompts.fg = material['white']

## Background color for the selected item in filename prompts.
## Type: QssColor
c.colors.prompts.selected.bg = material['base01']

## Background color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.bg = material['blue']

## Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = material['white']

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.bg = material['teal']

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = material['white']

## Background color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.bg = material['blue_ink']

## Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = material['teal']

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.bg = material['blue_ink']

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = material['tomato']

## Background color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.bg = material['green']

## Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = material['white']

## Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = material['blue_ink']

## Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = material['white']

## Background color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.bg = material['magenta']

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = material['white']

## Background color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.bg = material['tomato']

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = material['tomato']

## Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = material['white']

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
c.colors.statusbar.url.error.fg = material['red']

## Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = material['white']

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
c.colors.statusbar.url.hover.fg = material['blue']

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = material['yellow_bold']

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
c.colors.statusbar.url.success.https.fg = material['blue_ink']

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
c.colors.statusbar.url.warn.fg = material['yellow_bold']

## Background color of the tab bar.
## Type: QtColor
# c.colors.tabs.bar.bg = '#555555'

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = material['grey_blue']

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = material['white']

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = material['red']

## Color gradient start for the tab indicator.
## Type: QtColor
c.colors.tabs.indicator.start = material['yellow_bold']

## Color gradient end for the tab indicator.
## Type: QtColor
c.colors.tabs.indicator.stop = material['yellow_bold']

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.tabs.indicator.system = 'rgb'

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = material['blue_ink']

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = material['white']

## Background color of selected even tabs.
## Type: QtColor
c.colors.tabs.selected.even.bg = material['teal']

## Foreground color of selected even tabs.
## Type: QtColor
c.colors.tabs.selected.even.fg =  material['blue_ink']

## Background color of selected odd tabs.
## Type: QtColor
c.colors.tabs.selected.odd.bg = material['teal']

## Foreground color of selected odd tabs.
## Type: QtColor
c.colors.tabs.selected.odd.fg = material['blue_ink']

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'
