import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout

ERROR_MSG = 'ERROR'

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Taschenrechner')
        # self.setFixedSize(300, 300)
        self.setGeometry(0,0,300,300)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()
        self.setLayout(self.generalLayout)


    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')


class PyCalcCtrl(PyCalcUi):
    """PyCalc Controller class."""
    def __init__(self):
        super().__init__()
        """Controller initializer."""
        self._evaluate = self.evaluateExpression
        # Connect signals and slots
        self._connectSignals()
    
    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self.displayText())
        self.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self.displayText() == ERROR_MSG:
            self.clearDisplay()

        expression = self.displayText() + sub_exp
        self.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self.buttons['='].clicked.connect(self._calculateResult)
        self.display.returnPressed.connect(self._calculateResult)
        self.buttons['C'].clicked.connect(self.clearDisplay)


    def evaluateExpression(self, expression):
        """Evaluate an expression."""
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG

        return result


# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    # Show the calculator's GUI
    # Create instances of the model and the controller
    PyCalcCtrl()
    # Execute the calculator's main loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()