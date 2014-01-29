Usage

* use the hotkey ctrl + g (if enabled)
 * otherwise, use the window command ctrl + shift + p
 * and type GotoRowCol
 * press ENTER
* an input box will appear at the bottom of the sublime text window with two initial values populated 1 1. The first value represents the row, the second value represents the column. they are 1 based
* enter your desired coordinates (e.g. 26 32 for row 26 col 32)
 * you can also enter a row by itself without the column. this will be interpreted as "go to row n col 1"
 * example 26 results in (row 26, col 1)
* press ENTER



Replacing "goto row" hotkey

by default, the "goto row" hotkey ctrl + g brings up a prompt at the top of the sublime text window with a colon in it indicating that you can input a row number to navigate the cursor and view to that row. The included file Default.sublime-keymap can replace this behavior with the "GotoRowCol" functionality. Pressing ctrl + g can result in the behavior described in the Usage section of this README. To enable this hotkey, change:

from: //{ "keys": ["ctrl+g"], "command": "prompt_goto_row_col", "args": {} }

to: { "keys": ["ctrl+g"], "command": "prompt_goto_row_col", "args": {} }

The "goto row" functionality will still be available through the ctrl + p window command if you enable this hotkey. To use it this method of invoking the "goto row" functionality, do the following:

use the window command ctrl + p
 * a prompt will appear at the top of the sublime text window
 * type a colon : plus the row you want to navigate to
 * press ENTER
 * example: :38 then ENTER will take you to line 38 in the text file



Settings

file Packages/GotoRowCol/GotoRowCol.sublime-settings contains the following settings

 * gtrc_prompt_default (default: "1 1") - Controls the default prompt text
