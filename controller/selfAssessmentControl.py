from form.selfAssessment_ui import Ui_Dialog
from PyQt5.QtWidgets import QDialog


class SelfAssessment(QDialog, Ui_Dialog):
    def __init__(self):
        super(SelfAssessment, self).__init__()
        self.setupUi(self)
