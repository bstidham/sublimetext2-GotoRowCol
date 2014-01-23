sublimetext2-GotoRowCol
=======================

Places the cursor at the specified row and column 

Usage
=====

* use the window command `ctrl` + `shift` + `p` 
* type `GotoRowCol`
* press `ENTER`
* an input box will appear at the bottom of the sublime text window with two initial values populated `1 1`. The first value represents the `row`, the second value represents the `column`. they are `1 based` 
* enter your desired coordinates (e.g. `26 32` for `row 26` `col 32`)
* press `ENTER`

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
  * notes     initial creation. created in response to [this StackOverflow qestion](http://stackoverflow.com/questions/21283763/sublime-text-goto-line-and-column/21288455#21288455)
