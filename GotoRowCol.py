import sublime, sublime_plugin


class PromptGotoRowColCommand(sublime_plugin.WindowCommand):
    def run(self, automatic = True):
        settings = sublime.load_settings("GotoRowCol.sublime-settings") 
        gtrc_prompt_default = settings.get("gtrc_prompt_default", "1 1") 
        self.window.show_input_panel(
            'Enter a row and a column',
            gtrc_prompt_default,
            self.gotoRowCol,
            None,
            None
        )
        pass

    def gotoRowCol(self, text):
        try:
            splitText = text.split(" ")
            print("splits: " + str( len(splitText) ) )
            if len(splitText) == 1:
                # only the row was supplied
                (row, col) = (int(splitText[0]), 1)
            if len(splitText) == 2:
                (row, col) = splitText[0] , splitText[1]

            if self.window.active_view():
                self.window.active_view().run_command(
                    "goto_row_col",
                    {"row": row, "col": col}
                )
        except ValueError:
            pass


class GotoRowColCommand(sublime_plugin.TextCommand):
        def run(self, edit, row, col):
                print("INFO: Input: " + str({"row": row, "col": col}))
                # rows and columns are zero based, so subtract 1
                # convert text to int
                (row, col) = ( int( row ) - 1 , int( col ) - 1 )
                if row > -1 and col > -1:
                        # col may be greater than the row length
                        currentRowLength = len( self.view.substr( self.view.full_line( self.view.text_point( row , 0 ) ) ) ) -1
                        col = min( col , currentRowLength )
                        print("INFO: Calculated: " + str({"row": row, "col": col}))
                        self.view.sel().clear()
                        self.view.sel().add(sublime.Region(self.view.text_point(row, col)))
                        self.view.show(self.view.text_point(row, col))
                else:
                        print("ERROR: The Row or the Column arguments are less than one. Both must be >=1")
