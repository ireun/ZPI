import sys
import pickle
import sklearn

from PySide6 import QtWidgets

import GUI

ui = GUI.Ui_Wizard()


def run():
    with open('scaler.pickle', 'rb') as scaler_handle:
        scaler = pickle.load(scaler_handle)

    params = [[ui.temp_spalin_1.value(),
               ui.temp_spalin_2.value(),
               ui.poziom_p_konc.value(),
               ui.temp_hydratora.value(),
               ui.delta_p.value(),
               ui.pressure_in.value(),
               ui.temp_spalin_in.value(),
               ui.air.value(),
               ui.temp_spalin_in_2.value(),
               ui.zasiarczenie_wegla.value()
               ]]

    data = scaler.transform(params)

    with open('regression_tree.pickle', 'rb') as model_handle:
        model = pickle.load(model_handle)

    output = model.predict(data)
    ui.output.setText("Przewidywana ilość siarki to " + str(*output))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    Wizard = QtWidgets.QWizard()
    ui.setupUi(Wizard)
    ui.pushButton_run.clicked.connect(run)
    Wizard.show()
    sys.exit(app.exec())
