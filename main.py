import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qrangeslider import QRangeSlider

def setFolderHandler(config,configvar, window, isfolder=True):
    if not isfolder:
        config[configvar] = QFileDialog.getOpenFileName(
            window,
            'Observations file', 
            '', 
            'Text files (*.txt)'
        )[0]
    else:
        config[configvar] = QFileDialog.getExistingDirectory(
            window,
            "Open Directory",
            "/Users/michael"
        )

def setValueChangeHandler(value, config, configvar, window):
    if not type(value) == int:
        if text.isnumeric(): config[configvar] = int(text)
        else: config[configvar] = 100
    else:
        config[configvar] = value

def computePopulationBias(simulationData, observationData):
    observationSum = sum(np.where(not np.isnan(observationData)))
    simulationSum = sum(np.where(not np.isnan(observationData)) - np.where(not np.isnan(simulationData)))
    return simulationSum / observationSum * 100
 

def simulate(config):
    oldpop = np.array([0]*config['params'])
    for var in range(config['params']):
        oldpop[var] = config['minparam'][var] + congfigp['populationSize'] * 
                      (config['maxparam'][var] - config['minparam'])

    oldpop = np.round(oldpop,5)

    pbiases = np.zeros((config['populationSize'],8))

    simulationOutput = np.zeros((8,3))

    simulationResults = np.zeros(())
    #print(config)
    for i in range(config['populationSize']):
        #print(i)
        


def main():
    config = {
        'inputFolder': None,
        'outputFolder': None,
        'observationsFile': None,
        'populationSize': 0,
        'paramCount': 0,
        'minparam': np.array([0,0]),
        'maxparam':np.array([0,0]),
    }
    # init ui
    app  = QApplication([])
    
    window = QWidget()
    
    hlayout = QHBoxLayout()
    vlayout = QVBoxLayout()

    # buttons
    # -- set work folder.
    setWorkFolderBtn = QPushButton('Select Work folder')
    setWorkFolderBtn.clicked.connect(lambda: setFolderHandler(config,'inputFolder', window))
    # -- sets output folder.
    setOutputFolderBtn = QPushButton("Select Output folder")
    setOutputFolderBtn.clicked.connect(lambda: setFolderHandler(config, 'outputFolder', window))
    # -- set observations file path
    setObservationsFileBtn = QPushButton("Select Observations")
    setObservationsFileBtn.clicked.connect(lambda: setFolderHandler(config, 'observationsFile', window, isFolder=False))
    # -- set simulate button
    simulateBtn = QPushButton('Simulate')
    simulateBtn.clicked.connect(lambda: simulate(config))
    
    # textboxes
    # -- set population count textbox
    populationCountTxt = QLineEdit()
    populationCountTxt.textChanged.connect(lambda text: setValueChangeHandler(text, config, 'populationSize', window))

    # arrange components in ui
    vlayout.addWidget(setWorkFolderBtn)
    vlayout.addWidget(setOutputFolderBtn)
    vlayout.addWidget(setObservationsFileBtn)
    vlayout.addWidget(QLabel('Calibration Parameters'))
   
    populationFormSet = QHBoxLayout()
    populationFormSet.addWidget(QLabel('Population Size'))
    populationFormSet.addWidget(populationCountTxt)
    
    paramFormSet = QHBoxLayout()
    paramFormSet.addWidget(QLabel('Number of Parameters'))
    paramValue = QSlider(Qt.Horizontal)
    paramValue.valueChanged.connect(lambda value: setValueChangeHandler(value, config, 'paramCount', window))
    paramFormSet.addWidget(paramValue)

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
    vlayout.addLayout(paramFormSet)
    vlayout.addLayout(maxCalibFormSet)
    vlayout.addLayout(minCalibFormSet) 
    vlayout.addWidget(simulateBtn)   
    
    hlayout.addLayout(vlayout)
    window.setLayout(hlayout);
    window.show()

    app.exec_()    # add event handlers
    
if __name__ == '__main__':
    main()

