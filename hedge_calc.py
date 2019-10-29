from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QLineEdit, QPushButton)
import sys
from .maths import calculate_hedge_to_place

class GuiWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)

        self.setWindowTitle('Cath\'s Hedge Calculator')
        layout = QVBoxLayout()
        self.setLayout(layout)

        welcome_label = QLabel('Welcome to Cath\'s <h1>Hedge Calculator</h1>')
        instruction_label = QLabel('Enter the parameters below...')

        layout.addWidget(welcome_label)
        layout.addWidget(instruction_label)

        # Allows the user to input the hedge required
        self.hedge_required = QLineEdit()
        self.hedge_required.setPlaceholderText('Hedge Required')
        layout.addWidget(self.hedge_required)

        # Allows the user to input the existing hedge
        self.existing_hedge = QLineEdit()
        self.existing_hedge.setPlaceholderText('Existing hedge')
        layout.addWidget(self.existing_hedge)

        # Allows the user to input the VIF
        self.VIF = QLineEdit()
        self.VIF.setPlaceholderText('VIF')
        layout.addWidget(self.VIF)

        # A button to get the hedge_to_place
        button = QPushButton('Calculate Hedge')
        button.clicked.connect(self.calculate_hedge)
        layout.addWidget(button)

        # A label which shows the hedge to place
        self.hedge_to_place = QLabel("")
        layout.addWidget(self.hedge_to_place)


    def calculate_hedge(self):
        hr = int(self.hedge_required.text())
        eh = int(self.existing_hedge.text())
        vif = int(self.VIF.text())
        tol = 250000
        htp = calculate_hedge_to_place(hr, eh, vif, tol)


        self.hedge_to_place.setText(str(htp))









if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GuiWidget()
    window.show()  # Show the window
    app.exec_()  # Start the event loop
