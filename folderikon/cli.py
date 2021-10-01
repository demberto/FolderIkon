import configparser
from os import system
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse

import colorama
from PIL import Image
import requests

from .argparser import *
from .constants import *
from .exceptions import *
from .notify_shell import *
from .exceptions import *

class FolderIkon:
    def __init__(self, args):
        self.__image = args.image
        self.__icon = args.icon
        self.__parent = args.parent
        self.__delete_original = args.delete_original
        self.__raise_on_existing = args.raise_on_existing
        self.__dont_hide_icon = args.dont_hide_icon
        self.__no_color = args.no_color

        self.parent = self.__parent

    def iconize(self):
        if not self.__no_color:
            Error.color = True
            colorama.init(autoreset=True)

        if not self.__image:
            exception_exit(ImageNotSpecifiedError)

        if self.__image.startswith('http') or self.__image.startswith('www'):
            url = self.__image
            try:
                urlparse(url)
            except URLError:
                exception_exit(InvalidURLError)
            # /a/b/c.png -> WindowsPath('c.png')
            name = url.split('/')[-1]
            self.image = self.parent / name
            with open(self.image, 'wb') as fp:
                headers = requests.head(url).headers
                mime = headers.get('content-type')
                if mime not in SUPPORTED_IMAGE_MIME_TYPES:
                    exception_exit(ImageFormatNotSupportedError)
                content = requests.get(url).content
                fp.write(content)
        else:
            # Image is a local path
            self.image = Path(self.__image)

        if self.__icon:
            if self.parent == Path.cwd():
                self.parent = Path(self.__icon).parent
            self.icon = Path(self.__icon)
            if not self.icon.is_absolute():
                self.icon = self.parent / self.icon
        else:
            self.icon = self.image.with_suffix('.ico')
            if self.icon.exists() and self.__raise_on_existing:
                exception_exit(FolderIconAlreadyExistsError)

        if not self.image.suffix == '.ico':
            if self.icon.exists():
                if self.__raise_on_existing:
                    exception_exit(FolderIconAlreadyExistsError)
                self.icon.unlink()
            with Image.open(self.image) as img:
                img.save(self.icon, bitmap_format='bmp')

        self.conf = self.parent / Path('desktop.ini')
        conf_existed = False
        if self.conf.exists():
            conf_existed = True
            system('attrib -r -h -s "%s"' % str(self.conf))
        else:
            open(self.conf, 'x').close()
        config = configparser.ConfigParser()
        try:
            config.read(self.conf)
        except configparser.Error as exc:
            fp.close()
            if not conf_existed:
                self.conf.unlink()
            self.icon.unlink()
            system('attrib +h +s "%s"' % str(self.conf))
            exception_exit(DesktopIniError(exc))
        with open(self.conf, 'w') as fp:
            if '.ShellClassInfo' not in config:
                config.add_section('.ShellClassInfo')
            name = str(self.icon.name)
            section = config['.ShellClassInfo']
            section['IconResource'] = '%s,0' % name
            config.write(fp, space_around_delimiters=False)

        if not self.__dont_hide_icon:
            system('attrib +h "%s"' % str(self.icon))
        system('attrib +h +s "%s"' % str(self.conf))
        system('attrib +r "%s"' % str(self.parent))

        notify_shell()
        if self.__delete_original and self.image != self.icon:
            self.image.unlink()

def main():
    args = argparser.parse_args()
    FolderIkon(args).iconize()
