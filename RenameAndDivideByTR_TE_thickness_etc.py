#coding: utf-8

import shutil, os
import pydicom as dicom

for CaseID in os.listdir('.'):
    SequenceNamelist = []
    print(CaseID)
    try:
        os.makedirs('../renamed/' + CaseID)
    except:
        pass
    if os.path.isdir(CaseID) == True:
        print("Renaming",  CaseID) 
        for ImageID in os.listdir(CaseID):
            #print(CaseID + "/" +  ImageID)
            try:
                target_dicom_file = CaseID + "/" + ImageID
                ds = dicom.read_file(target_dicom_file)
                #print(ds.SeriesDescription)
                #ProtocolName = ds.SeriesDescription#ProtocolName
                try:
                    ScanningSequence = str(ds.ScanningSequence)
                    ProtocolName = ScanningSequence
                except:
                    pass

                try:
                    MRAcquisitionType = str(ds.MRAcquisitionType)
                    ProtocolName = ProtocolName + '_' + MRAcquisitionType
                except:
                    pass

                try:
                    SliceThickness = str(ds.SliceThickness)
                    ProtocolName = ProtocolName + '_' + SliceThickness
                except:
                    pass

                try:
                    RepetitionTime = str(ds.RepetitionTime)
                    ProtocolName = ProtocolName + '_' + RepetitionTime
                except:
                    pass

                try:
                    EchoTime = str(ds.EchoTime)
                    ProtocolName = ProtocolName + '_' + EchoTime
                except:
                    pass

                try:
                    NumberOfAverages = str(ds.NumberOfAverages)
                    ProtocolName = ProtocolName + '_' + NumberOfAverages
                except:
                    pass

                try:
                    os.mkdir('../renamed/' + CaseID + '/' + ProtocolName)
                except:
                    pass
                savename = '../renamed/' + CaseID + '/' + ProtocolName + '/' +\
                           ProtocolName +'_' + ImageID

                try:
                    shutil.copyfile(target_dicom_file, savename)
                    print('Saving:' CaseID, ImageID)
                except:
                    print('Failed to save:', CaseID, ImageID)
                    pass

            except:
                pass

print("finished")
