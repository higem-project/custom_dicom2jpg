
"""
dicom2jpg
=========

A simple tool to convert DICOM files into jpg, png, tiff, or bmp files and Numpy array.
It piplines the lookup transformations by applying Modality LUT, VOI LUT, and Presentation LUT to the images,
which makes output files looks like what we see on standard DICOM viewers.

Basic usage:
    
    dicom2jpg.dicom2jpg(folder_of_dicom_files)

"""

# import info

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __author__, __author_email__, __license__

from .utils import _dicom_convertor
from .utils import _dicom_to_img


def io2img(dcmio):
    """
    DICOM BytesIO -> ndarray, in 8 bit integer; RGB format if it's color image
    """
    return _dicom_to_img(dcmio, input_type='io')

def dicom2img(origin):
    """
    DICOM -> ndarray, in 8 bit integer; RGB format if it's color image
    origin: a .dcm file
    """
    return _dicom_to_img(origin, input_type='ds')

def dicom2tiff(origin, target_root=None, anonymous=False, multiprocessing=True):
    # under construction
    """
    DICOM -> tiff
    origin: can be a .dcm file, a folder, or a list/tuple containing file/folders
    target_root: root of output files and folders
    default target root folder is the root of origin file
    """
    return _dicom_convertor(origin, target_root, filetype='tiff',
                            multiprocessing=multiprocessing, 
                            anonymous=anonymous)

def dicom2jpg(origin, target_root=None, anonymous=False, multiprocessing=True):
    """
    DICOM -> jpg
    origin: can be a .dcm file, a folder, or a list/tuple containing file/folders
    target_root: root of output files and folders
    default target root folder is the root of origin file
    """
    return _dicom_convertor(origin, target_root, filetype='jpg',
                            multiprocessing=multiprocessing, 
                            anonymous=anonymous)

def dicom2png(origin, target_root=None, anonymous=False, multiprocessing=True):
    """
    DICOM -> png
    origin: can be a .dcm file, a folder, or a list/tuple containing file/folders
    target_root: root of output files and folders
    default target root folder is the root of origin file

    """
    return _dicom_convertor(origin, target_root, filetype='png',
                            multiprocessing=multiprocessing, 
                            anonymous=anonymous)


def dicom2bmp(origin, target_root=None, anonymous=False, multiprocessing=True):
    """
    DICOM -> bmp
    origin: can be a .dcm file, a folder, or a list/tuple containing file/folders
    target_root: root of output files and folders
    default target root folder is the root of origin file

    """
    return _dicom_convertor(origin, target_root, filetype='bmp',
                            multiprocessing=multiprocessing, 
                            anonymous=anonymous)

def dicom2png_cq500(origin, target_root=None, anonymous=False, multiprocessing=True, counter:int = None, dataset:str = None):

    assert target_root, "You must pass a target_root for saving you converted files"  
          
    return _dicom_convertor(origin, target_root, filetype='png',
                            multiprocessing=multiprocessing, 
                            anonymous=anonymous, 
                            counter=counter, dataset=dataset)
# import os
# x = 0
# for file in os.listdir('/Users/luizfelipe/Desktop/Python/Libraries/example_image'):
#     if file.lower() != '.ds_store':
#         x+=1   
#         dicom2png_cq500('/Users/luizfelipe/Desktop/Python/Libraries/example_image', '/Users/luizfelipe/Desktop/Python/Libraries/converted',  multiprocessing=False, counter=x, dataset='cq500')
#     else:
#         continue
