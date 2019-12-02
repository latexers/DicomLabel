import os
import shutil
import xlrd

# def copy_dir(original_path, des_path):
#     isExists = os.path.exists(des_path)
#     if not isExists:
#         os.makedirs(des_path)
#         return True
#     return True

if __name__ == "__main__":
    path = "D:\中山肿瘤\pre_liver\data_pre_UIH"
    excel_path = "D:\中山肿瘤\（中肿）原发小肝癌1-5-整理.xlsx"
    first_path = "D:/中山肿瘤/data_pre/UIH/first"
    second_path = "D:/中山肿瘤/data_pre/UIH/second"
    worksheet = xlrd.open_workbook(excel_path)
    sheet_names = worksheet.sheet_names()
    print(sheet_names)
    first_ablation = worksheet.sheet_by_name(sheet_names[0])
    second_ablation = worksheet.sheet_by_name(sheet_names[1])
    first_rows = first_ablation.nrows
    first_cols = first_ablation.ncols

    second_rows = second_ablation.nrows
    second_cols = second_ablation.ncols
    first_image_id_list = []
    second_image_id_list = []
    for i in range(1,first_rows):
        cell = first_ablation.cell_value(i, 2)
        first_image_id_list.append(str(int(cell)))

    for i in range(1,second_rows):
        cell = second_ablation.cell_value(i, 2)
        second_image_id_list.append(str(int(cell)))

    print(first_image_id_list)
    print(second_image_id_list)
    # name_list = os.listdir(path)
    # # excel_image_id = ""
    # for name in name_list:
    #     name_split = name.split('_')
    #     image_id = name_split[1]
    #     scan_id = name_split[2]
    #     print(image_id)
    #     # print(scan_id)
    #     org_path = path + "\\" + name
    #     print(image_id in second_image_id_list)
    #     if image_id in first_image_id_list:
    #         des_path = first_path + '\\' + image_id + '\\' + scan_id
    #         shutil.copytree(org_path,des_path)
    #     elif image_id in second_image_id_list:
    #         des_path = second_path + '\\' + image_id + '\\' + scan_id
    #         shutil.copytree(org_path,des_path)
    #     else:
    #         continue
    # org_path = path + '\\' + name
        # des_path = path + '\\' + image_id + '\\' + scan_id
        # print(org_path)
        # shutil.copytree(org_path,des_path)
        # print(des_path)
    print("这是一个Dicom标记程序")