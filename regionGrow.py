import SimpleITK as sitk
from myshow import myshow, myshow3d
from downloaddata import fetch_data as fdata

img_T1 = sitk.ReadImage(
    fdata("nac-hncma-atlas2013-Slicer4Version/Data/A1_grayT1.nrrd"))

# To visualize the labels image in RGB needs a image with 0-255 range
img_T1_255 = sitk.Cast(sitk.RescaleIntensity(img_T1), sitk.sitkUInt8)

size = img_T1.GetSize()
myshow3d(img_T1_255, zslices=range(50, size[2] - 50, 20), title='T1')

seed = (132, 142, 96)

seg = sitk.Image(img_T1.GetSize(), sitk.sitkUInt8)
seg.CopyInformation(img_T1)
seg[seed] = 1

seg = sitk.BinaryDilate(seg, 3)

myshow3d(sitk.LabelOverlay(img_T1_255, seg),
         xslices=range(132, 133), yslices=range(142, 143),
         zslices=range(96, 97), title="Initial Seed")

seg_con = sitk.ConnectedThreshold(img_T1, seedList=[seed],
                                  lower=100, upper=190)

myshow3d(sitk.LabelOverlay(img_T1_255, seg_con),
         xslices=range(132, 133), yslices=range(142, 143),
         zslices=range(96, 97), title="Connected Threshold")