from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QLineEdit, QPushButton)
import sys

class GuiWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)

        self.setWindowTitle('Cath\'s Hedge Calculator')
        layout = QVBoxLayout()
        self.setLayout(layout)

        welcome_label = QLabel('Welcome to Cath\'s <h1>Hedge Calculator</h1>')
        layout.addWidget(welcome_label)

        # Allows the user to input the hedge required
        hedge_required = QLineEdit()
        hedge_required.setPlaceholderText('Hedge Required')
        layout.addWidget(hedge_required)

        # Allows the user to input the existing hedge
        existing_hedge = QLineEdit()
        existing_hedge.setPlaceholderText('Existing hedge')
        layout.addWidget(existing_hedge)

        # Allows the user to input the VIF
        VIF = QLineEdit()
        VIF.setPlaceholderText('VIF')
        layout.addWidget(VIF)

        # A button to get the hedge_to_place
        button = QPushButton('Calculate Hedge')
        layout.addWidget(button)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GuiWidget()
    window.show()  # Show the window
    app.exec_()  # Start the event loop
