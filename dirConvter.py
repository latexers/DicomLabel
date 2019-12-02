import os
import shutil
import xlrd
import pydicom

if __name__ == "__main__":
    base_path = './Data/PA0/ST0/SE0'
    # pa_names = os.listdir(base_path)
    # # dicom_names = []
    # for pa in pa_names:
    #     st_names = os.listdir(base_path + '/' + pa)
    #     for st in st_names:
    #         se_names = os.listdir(base_path + '/' + pa + '/' + st)
    #         for se in se_names:
    #             dicom_names = os.listdir(base_path + '/'+ pa + '/' + st + '/' + se)
    #             for dicom in dicom_names:
    #                 dicom_name = base_path + '/'+ pa + '/' + st + '/' + se + '/' + dicom
    #                 ds = pydicom.dcmread(dicom_name)
    #                 print(type(ds))
    #                 print(ds.PatientName)
    #                 print(ds.PatientID)
    #                 print()
    #                 # print(ds)
    #             print(dicom_names)

    dicom_name = './IM0'
    ds = pydicom.dcmread(dicom_name)
    print(ds)
    scans = []
    # for file in filelocations:
    #     dicomds = dicom.read_file(file, stop_before_pixels=True)
    #     mod_ds = {data_elem.keyword: data_elem.value for data_elem in dicomds.values()}
    #     scans.append(mod_ds)
    # mod_ds = {ds.keyword: ds.value for data_elem in ds.values()}
    # print(mod_ds)
    for value in ds.values():
        print(value)
