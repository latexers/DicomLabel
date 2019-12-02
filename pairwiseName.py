import pydicom
import os
if __name__ == "__main__":
    path = "D:\中山肿瘤\首发"
    ids = []
    patientIDs =[]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".dcm"):
                dcmfile_name = os.path.join(root, file)
                dcmfile = pydicom.dcmread(dcmfile_name)
                # patientID['id'] = root.split('\\')[3]
                id = root.split('\\')[3]
                patientID = dcmfile.PatientID
                if id not in ids:
                    ids.append(id)
                    patientIDs.append(patientID)
                # patientID['patient'] = dcmfile.PatientID
                print(dcmfile.PatientID)
                # patientList.add(patientID)
    # print(id)
    print(ids)
    print(patientIDs)
    print("Processing Finished!")