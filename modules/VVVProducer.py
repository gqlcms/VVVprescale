import ROOT
from ROOT import TLorentzVector
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import math
import os
import numpy as np
from numpy import sign

def Process_0Lepton_2fatJets(event):
    muons = Collection(event, 'Muon')
    nLooseMu = 0
    for imu in range(0, event.nMuon):
      if (event.Muon_highPtId[imu]=='\x02' and event.Muon_tkRelIso[imu] <0.1 and abs(muons[imu].eta)<2.4 and muons[imu].pt>20):
        nLooseMu += 1

    electrons = Collection(event, 'Electron')
    nLooseEle = 0
    for iele in range(0, event.nElectron):
      if (event.Electron_cutBased_HEEP[iele] and abs(electrons[iele].eta)<2.5 and electrons[iele].pt>35):
        nLooseEle += 1
    
    if not ((nLooseEle+nLooseMu)==0) : return False
    if not (event.nFatJet >= 2)      : return False
    if not (event.FatJet_pt[0]> 350) : return False
    return True

class VVVProducer(Module):
  def __init__(self , year, MODE = "0Lepton_gKK" ):
    self.year = year
    self.MODE = MODE
    self.Process_Genparticles = False
    if self.MODE == "0Lepton_gKK":
        self.function = Process_0Lepton_2fatJets

  def beginJob(self):
    pass

  def endJob(self):
    pass

  def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
    self.out = wrappedOutputTree
    self.is_mc = bool(inputTree.GetBranch("GenJet_pt"))

  def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
    pass

  def analyze(self, event):
    return (self.function)(event)


VVV2016 = lambda MODE="0Lepton_gKK": VVVProducer("2016",MODE)
VVV2017 = lambda MODE="0Lepton_gKK": VVVProducer("2017",MODE)
VVV2018 = lambda MODE="0Lepton_gKK": VVVProducer("2018",MODE)