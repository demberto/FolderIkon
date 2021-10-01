import argparse
from pathlib import Path

from .constants import *
from .exceptions import ParentIsNotAFolderError, exception_exit
from .metadata import __prog__, __description__

__all__ = ['argparser']

def __default_image_arg():
    cwd = Path.cwd()
    for ext in SUPPORTED_IMAGE_FORMATS:
        images = cwd.glob(f'*.{ext}')
        for image in images:
            return image
    return None

def __is_dir(path):
    if not Path(path).is_dir():
        exception_exit(ParentIsNotAFolderError)
    return Path(path)

argparser = argparse.ArgumentParser(prog=__prog__,
                                    description=__description__)
argparser.add_argument('--image',
                       '--input',
                       '-i',
                       default=__default_image_arg(),
                       help="The image to set as folder icon. "
                            "JPG, ICO and PNG formats are supported. "
                            "URLs can be specified as well. "
                            "Defaults to the first JPG/PNG file "
                            "found in the current folder.")
argparser.add_argument('--icon',
                       '--output',
                       '-o',
                       help="Output icon file name. "
                            "Defaults to the name of first "
                            "JPG/PNG found in current folder "
                            "saved with a '.ico' extension.")
argparser.add_argument('--parent',
                       '-p',
                       '-d',
                       type=__is_dir,
                       default=Path.cwd(),
                       help="The path of the folder whose "
                            "icon is to be set. Defaults to "
                            "the current folder.")
argparser.add_argument('--delete-original',
                       '-x',
                       action='store_true',
                       help="Deletes the original image.")
argparser.add_argument('--raise-on-existing',
                       action='store_true',
                       help="Raise an exception if the folder already has an icon.")
argparser.add_argument('--dont-hide-icon',
                       action='store_true',
                       help="The folder icon is marked as hidden "
                            "by default. Use this option to not do it.")
argparser.add_argument('--no-color',
                       action='store_true',
                       help="Disables colored output.")
