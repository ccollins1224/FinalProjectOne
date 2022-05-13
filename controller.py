from PyQt5.QtWidgets import *
from view import Ui_MainWindow
import random
from sys import exit



class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.hands = ['rock', 'paper', 'scissors']  # creating the different options for the game
        self.comboBox_selection.addItems(self.hands)
        self.pushButton_submit.clicked.connect(lambda: self.submit())
        Controller.userscore = 0
        Controller.compscore = 0

    def submit(self):

        Controller.user = self.comboBox_selection.currentText()
        Controller.comp = random.choice(self.hands)


        if Controller.user == Controller.comp:
            self.label_result.setText(f'Computer is {Controller.comp}. You are {Controller.user}. You tie.')

        elif Controller.user == 'rock':
            if Controller.comp == 'paper':
                self.label_result.setText(f'Computer is {Controller.comp}. You are {Controller.user}. You lose.')
                Controller.compscore += 1
                self.label_compscore.setText(f'{Controller.compscore}')

            elif Controller.comp == 'scissors':
                self.label_result.setText(f'Computer is {Controller.comp}. You are {Controller.user}. You win.')
                Controller.userscore += 1
                self.label_userscore.setText(f'{Controller.userscore}')

        elif Controller.user == 'paper':
            if Controller.comp == 'scissors':
                self.label_result.setText(f'Computer is {Controller.comp}. You are {Controller.user}. You lose.')
                Controller.compscore += 1
                self.label_compscore.setText(f'{Controller.compscore}')
            elif Controller.comp == 'rock':
                self.label_result.setText(f'Computer is {Controller.comp}. You are {Controller.user}. You win.')
                Controller.userscore += 1
                self.label_userscore.setText(f'{Controller.userscore}')

        elif Controller.user == 'scissors':
            if Controller.comp == 'rock':
                self.label_result.setText(f'Computer is {Controller.comp}. You are {Controller.user}. You lose.')
                Controller.compscore += 1
                self.label_compscore.setText(f'{Controller.compscore}')
            elif Controller.comp == 'paper':
                self.label_result.setText(f'Computer is {Controller.comp}. You are {Controller.user}. You win.')
                Controller.userscore += 1
                self.label_userscore.setText(f'{Controller.userscore}')

        if Controller.userscore == 3:
            self.label_result.setText('GAME OVER - YOU WON!!!')
            Controller.userscore = 0
            Controller.compscore = 0
            self.label_userscore.setText('0')
            self.label_compscore.setText('0')

        if Controller.compscore == 3:
            self.label_result.setText('GAME OVER - COMPUTER WON!!!')
            Controller.userscore = 0
            Controller.compscore = 0
            self.label_userscore.setText('0')
            self.label_compscore.setText('0')
