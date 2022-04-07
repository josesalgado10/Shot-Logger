import tkinter
import stats

_DEFAULT_FONT = ('Helvetica', 20)
_HALFCOURT = 'Halfcourt.gif'
_JBALOGO = 'JBA.gif'


class ShotChartApp:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._root_window.title('Shot Logger 1.0')
        self._root_window.geometry('1200x600')
        self._root_window.config(background = 'grey')
        
#         the_canvas = tkinter.Canvas(self._root_window, background = 'white',
#                                      height = 650, width = 500)
#         the_canvas.grid(row = 1, column = 1, rowspan = 9)
        
        halfcourtimg = tkinter.PhotoImage(file=_HALFCOURT)
        self._label1 = tkinter.Label(self._root_window,image = halfcourtimg)
        self._label1.grid(row = 1, column = 1, rowspan = 9)
        self._label1.halfcourtimg = halfcourtimg
         
        jbaimg = tkinter.PhotoImage(file=_JBALOGO)
        self._label2 = tkinter.Label(image = jbaimg, background = 'grey')
        self._label2.grid(row = 3, column = 3, rowspan = 5)
        self._label2.jbaimg = jbaimg
        
        self.Entry = tkinter.Entry
        
        button_2p = self._create_button('2+', 1, 0)
        button_2m = self._create_button('2-', 2, 0)
        button_3p = self._create_button('3+', 3, 0)
        button_3m = self._create_button('3-', 4, 0)
        button_perc = self._create_button('Show %', 6, 0)
        button_store = self._create_button('Store', 8, 0)
        
        ###Implement to GUI
        _row_for_player = 1
        for player in stats.TEAM:
            self._make_player_buttons(player, _row_for_player, 2)
            _row_for_player += 1
        
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.rowconfigure(5, weight = 1)
        self._root_window.rowconfigure(6, weight = 1)
        self._root_window.rowconfigure(7, weight = 1)
        self._root_window.rowconfigure(8, weight = 1)
        self._root_window.rowconfigure(9, weight = 1)
        self._root_window.rowconfigure(10, weight = 1)
        self._root_window.rowconfigure(11, weight = 1)
        self._root_window.rowconfigure(12, weight = 1)
        

        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.columnconfigure(2, weight = 1)
        self._root_window.columnconfigure(3, weight = 1)
        self.player_selected = None
        self._status = tkinter.Label(master = self._root_window, text ='No player selected', font = _DEFAULT_FONT, background='grey', foreground='black')
        self._status.grid(row = 0, column = 1, columnspan = 1, sticky = tkinter.W + tkinter.E)
        
    def _create_button(self, text, row, col) -> tkinter.Button:
        if text == 'Store':
            button = tkinter.Button(
                master = self._root_window,
                text = text, font = _DEFAULT_FONT,
                command = self.store_all_player_stats(stats.TEAM),
                background = 'grey',
                foreground = 'black')
        
            button.grid(row = row, column = col, sticky = \
                        tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        else:
            button = tkinter.Button(
                master = self._root_window,
                text = text, font = _DEFAULT_FONT,
                command = self._make_command(text),
                background = 'grey',
                foreground = 'black')
        
            button.grid(row = row, column = col, sticky = \
                        tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        return button
    
    ### Add team param / add command
    def _make_player_buttons(self, Player, row, col):
        button = tkinter.Button(master = self._root_window, 
                                text = Player._first + ' ' + Player._last,
                                font = _DEFAULT_FONT,
                                command = self.select_player_from_stats(Player._first + ' ' + Player._last),
                                background = 'grey',
                                foreground = 'black')
        
        button.grid(row = row, column = col, sticky = \
                    tkinter.N + tkinter.S + tkinter.E + tkinter.W)
    
    ### Add team param / fix
    def select_player_from_stats(self, player):
        def command():
            self.player_selected = stats.select_player(player)
            print('Player Selected:', self.player_selected._first,
                  self.player_selected._last)
        return command
        
    def _make_command(self, key: str) -> 'function':
        def command_function() -> None:
            if self.player_selected == None:
                print('Please select a player')
            else:
                self.player_selected.handle(key)
                self._status.config(text=self.player_selected.player_status)
        return command_function

    def store_all_player_stats(self, team):
        def command():
            stats.store_all(team)
            self._root_window.destroy()
        return command
     
    def run(self):
        self._root_window.mainloop()
                    
if __name__ == '__main__':
    ShotChartApp().run()
