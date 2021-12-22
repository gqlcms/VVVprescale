from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True


class countHistogramsProducer_Data(Module):
    def __init__(self):
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.h_nevents = ROOT.TH1D('nEvents', 'nEvents', 1, 0, 1)
        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        prevdir = ROOT.gDirectory
        outputFile.cd()
        self.h_nevents.Write()
        prevdir.cd()

    def analyze(self, event):
        self.h_nevents.Fill(0.5)
        return True

countHistogramsModule_Data = lambda: countHistogramsProducer_Data()