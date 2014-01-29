sublimetext2-GotoRowCol
=======================

Places the cursor at the specified row and column 

Usage
=====

* use the hotkey `ctrl` + `g`
 * alternatively, use the window command `ctrl` + `shift` + `p` 
 * and type `GotoRowCol`
 * press `ENTER`
* an input box will appear at the bottom of the sublime text window with two initial values populated `1 1`. The first value represents the `row`, the second value represents the `column`. they are `1 based` 
* enter your desired coordinates (e.g. `26 32` for `row 26` `col 32`)
* press `ENTER`

Replacing "goto row" hotkey
===========================

Without this plugin installed, the "goto row" hotkey `ctrl` + `g` brings up a prompt at the top of the sublime text window with a colon in it indicating that you can input a row number to navigate the cursor and view to that row. The included file `Default.sublime-keymap` replaces this behavior with the "GotoRowCol" functionality. Pressing `ctrl` + `g` will now result in the behavior described in the `Usage` section of this README. 

The "goto row" functionality is still available through the `ctrl` + `shift` + `p` window command. To use it with this plugin installed, do the following:

* use the window command `ctrl` + `p`
* a prompt will appear at the top of the sublime text window
* type a colon `:` plus the row you want to navigate to
* press `ENTER`
* example: `:38` then `ENTER` will take you to line 38 in the text file


Behavior
========

once you've entered coordinates, the cursor will be placed at the requestd position and the viewport will scrow the area into viewable range

Gotchas
=======

* a `row` value entered that is greater than the number of rows in the view will scroll the cursor to the last line
* a `col` value entered that is greater than the length of text in the `row` will place the cursor at the last position of that line


Revision History
================

r1.0
  * developer bstidham (Bill Stidham)
  * date      01/22/2014
  * notes     
   * initial creation. created in response to [this StackOverflow qestion](http://stackoverflow.com/questions/21283763/sublime-text-goto-line-and-column/21288455#21288455)

r1.01
  * developer bstidham (Bill Stidham)
  * date      01/24/2014
  * notes     https://github.com/bstidham/sublimetext2-GotoRowCol/issues/1
   * Parenthesized print for compatibility: 
     * print without parens is only supported in sublime text 2 (python 2). sublime text 3 (python 3) requires that print be parenthesized.
   * Added file Default.sublime-keymap
     * replaces `ctrl` + `g` "goto row" functionality with GotoRowCol functionality

r1.02
  * developer bstidham (Bill Stidham)
  * date      01/28/2014
  * notes     
   * added file GotoRowCol.sublime.settings
     * added setting to GotoRowCol.sublime.settings: "gtrc_prompt_default": "1 1"
     * if this setting is not found, a default value of "1 1" is hard coded
   * modified GotoRowCol.py PromptGotoRowColCommand.gotoRowCol() to check the number of integers supplied
     * if 1 then it uses the value as the row number and navigates to the first column
     * if 2 then it goes to row col accordingly
   * commented out the `ctrl` + `g` hotkey in Default.sublime-keymap
     * will add instructions to the README for enabling this (by simply uncommenting it)
