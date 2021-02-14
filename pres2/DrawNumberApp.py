from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.gridlayout import GridLayout, GridLayoutException

class Board( Widget ):

    def on_touch_down(self, touch):
        print( touch )

        #add the line dictionary to the canvas for display, create a line object
        with self.canvas:
            touch.ud["line"] = Line( points=( touch.x, touch.y ), width = 10 )

    def on_touch_move( self, touch):
        print( touch )
        #add points to the dictionary of points on the canvas that was created on the touch down
        touch.ud["line"].points += ( touch.x, touch.y )

    def on_touch_up( self, touch ):
        print( "up" )


class drawNumberApp( App ):

    def build(self):

        #create the class instance variables, the overall widget and the board where we will be drawing
        self.ind = 1
        self.window = Widget()
        self.board = Board()
        self.layout_outer = GridLayout( rows=2 )
        self.button_layout = GridLayout( cols=2 )


        #create the two buttons that we can use
        clear = Button( text="clear", on_press=self.clear_canvas, size_hint_y=None, height=200 )
        save = Button( text="save", on_press=self.save_canvas, size_hint_y=None, height=200 )

        self.board_layout = GridLayout()

        self.board_layout.add_widget( self.board )
        self.layout_outer.add_widget( self.board_layout )
        self.layout_outer.add_widget( self.button_layout )
        self.button_layout.add_widget( clear )
        self.button_layout.add_widget( save )

        return self.layout_outer

    def clear_canvas( self, etc=1 ):
        self.board.canvas.clear()
    
    def save_canvas( self, etc ):
        save_string = "nmnist" + str(self.ind) + ".png"
        self.ind += 1
        self.board_layout.export_to_png( filename=save_string)

        self.clear_canvas()
    


if __name__ == "__main__":
    drawNumberApp().run()