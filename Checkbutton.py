from breezypythongui import EasyFrame
from tkinter.font import Font

class CheckbuttonDemo(EasyFrame):

    def __init__(self):
        # Initialize the main application window
        EasyFrame.__init__(self, title='Checkbutton Demo', width=500, height=300, resizable=False, background='lavender')

        # Title label for Today's Specials with a fancier font
        self.addLabel(text="Chef's Recommendations", row=0, column=0, sticky='NSEW', columnspan=2, background='lavender', foreground='darkblue', font=Font(family='Times New Roman', size=32, weight='bold', slant='italic'))

        # Checkbuttons for upscale menu items
        self.salmonCB = self.addCheckbutton(text='Pan-Seared Salmon', row=1, column=0)
        self.filetCB = self.addCheckbutton(text='Grilled Filet Mignon', row=1, column=1)
        self.asparagusCB = self.addCheckbutton(text='Truffle-infused Asparagus', row=2, column=0)
        self.caviarCB = self.addCheckbutton(text='Beluga Caviar', row=2, column=1)

        # Set background color for checkbuttons
        for cb in [self.salmonCB, self.filetCB, self.asparagusCB, self.caviarCB]:
            cb['background'] = 'lavender'

        # Command button for placing the order
        self.order = self.addButton(text='Place Order', row=3, column=0, columnspan=2, command=self.placeOrder)
        self.order['background'] = 'lightgreen'
        self.order['foreground'] = 'darkblue'
        self.order['width'] = 30

    def placeOrder(self):
        # Generate order summary message based on checked items
        message = ''

        if self.salmonCB.isChecked():
            message += 'Pan-Seared Salmon\n'
        if self.filetCB.isChecked():
            message += 'Grilled Filet Mignon\n'
        if self.asparagusCB.isChecked():
            message += 'Truffle-infused Asparagus\n'
        if self.caviarCB.isChecked():
            message += 'Beluga Caviar\n'
        if message == '':
            message += 'Sorry, no items ordered!'

        # Display order summary in a message box
        self.messageBox(title='Chef\'s Specials Order', message=message)


def main():
    # Instantiate the FancyMenuCheckbuttonDemo object and start the main loop
    CheckbuttonDemo().mainloop()


if __name__ == '__main__':
    main()
