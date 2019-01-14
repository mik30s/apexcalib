import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from qrangeslider import QRangeSlider


def setFolderHandler(configvar, window, isfolder=True):
    if not isfolder:
        configvar = QFileDialog.getOpenFileName(
            window,
            'Observations file', 
            '', 
            'Text files (*.txt)'
        )[0]
    else:
        configvar =  QFileDialog.getExistingDirectory(
            window,
            "Open Directory",
            "/Users/michael"
        )


def setTextHandler(text, configvar, window):
    print(text)
    if text.isnumeric():
        configvar = int(text)
    else:
        configvar = 100


def computePopulationBias(simulationData, observationData):
    observationSum = sum(np.where(not np.isnan(observationData)))
    simulationSum = sum(np.where(not np.isnan(observationData)) - np.where(not np.isnan(simulationData)))
    return simulationSum / observationSum * 100


def simulate(config):
    print(config)
    for i in range(config['populationSize']):
        print(i)


class AppConfig:
    def __init__(self):
        self.inputFolder = None
        self.outputFolder = None
        self.observationsFile = None
        self.populationSize = 0


def main():
    config = {
        'inputFolder': None,
        'outputFolder': None,
        'observationsFile': None,
        'populationSize': 0
    }
    # init ui
    app  = QApplication([])
    
    window = QWidget()
    
    hlayout = QHBoxLayout()
    vlayout = QVBoxLayout()

    # buttons
    # -- set work folder.
    setWorkFolderBtn = QPushButton('Select Work folder')
    setWorkFolderBtn.clicked.connect(lambda: setFolderHandler(config['inputFolder'], window))
    # -- sets output folder.
    setOutputFolderBtn = QPushButton("Select Output folder")
    setOutputFolderBtn.clicked.connect(lambda: setFolderHandler(config['outputFolder'], window))
    # -- set observations file path
    setObservationsFileBtn = QPushButton("Select Observations")
    setObservationsFileBtn.clicked.connect(lambda: setFolderHandler(config['observationsFile'], window, isFolder=False))
    # -- set simulate button
    simulateBtn = QPushButton('Simulate')
    simulateBtn.clicked.connect(lambda: simulate(config))
    
    # textboxes
    # -- set population count textbox
    populationCountTxt = QLineEdit()
    populationCountTxt.textChanged.connect(lambda text: setTextHandler(text, config['populationSize'], window))

    # arrange components in ui
    vlayout.addWidget(setWorkFolderBtn)
    vlayout.addWidget(setOutputFolderBtn)
    vlayout.addWidget(setObservationsFileBtn)
    vlayout.addWidget(QLabel('Calibration Parameters'))
   
    populationFormSet = QHBoxLayout()
    populationFormSet.addWidget(QLabel('Population Size'))
    populationFormSet.addWidget(populationCountTxt)
    
    maxCalibFormSet = QHBoxLayout()
    maxCalibFormSet.addWidget(QLabel('Max Calibration'))
    maxRange = QRangeSlider()
    maxRange.setMin(0)
    maxRange.setMax(1)
    maxCalibFormSet.addWidget(maxRange)
    
    minCalibFormSet = QHBoxLayout()
    minCalibFormSet.addWidget(QLabel('Min Calibration'))
    minRange = QRangeSlider()
    minRange.setMin(0)
    minRange.setMax(1)
    minCalibFormSet.addWidget(minRange)

    vlayout.addLayout(populationFormSet)
    vlayout.addLayout(maxCalibFormSet)
    vlayout.addLayout(minCalibFormSet) 
    vlayout.addWidget(simulateBtn)   

    hlayout.addLayout(vlayout)
    window.setLayout(hlayout);
    window.show()

    app.exec_()    # add event handlers
    
if __name__ == '__main__':
    main()

