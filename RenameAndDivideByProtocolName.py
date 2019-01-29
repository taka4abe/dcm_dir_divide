# coding: utf-8

import shutil, os
import pydicom as dicom

# 01, 02 などの施設の dir で使用する。
for CaseID in os.listdir('.'):
    # CaseID in 01-001, 01-002, 01-003, ...
    SequenceNamelist = []
    print(CaseID)
    try:
        os.makedirs('../renamed/' + CaseID) #Bayer直下にrenamed dir を作成
    except:
        pass
    if os.path.isdir(CaseID) == True:
        print("Renaming",  CaseID) # CaseID in 01-001, 01-002, 01-003, ...
        for ImageID in os.listdir(CaseID):
            #print(CaseID + "/" +  ImageID)
            try:
                target_dicom_file = CaseID + "/" + ImageID
                ds = dicom.read_file(target_dicom_file)
                try:
                    ProtocolName = ds.ProtocolName
                except:
                    pass

                try:
                    os.makedirs('../renamed/' + CaseID + '/' + ProtocolName)
                except:
                    pass

                try:
                    savename = '../renamed/' + CaseID + '/' + ProtocolName +\
                               '/' + ProtocolName +'_' + ImageID
                    shutil.copyfile(target_dicom_file, savename)
                    print('Saving:', CaseID, ImageID)
                except:
                    print('Failed to save:', CaseID, ImageID)
                    pass

            except:
                pass


print("finished")
