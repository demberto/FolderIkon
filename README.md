# FolderIkon

> A Windows utility to set folder icons.

Normally, setting a folder icon (not to be confused with a folder picture) through Windows Explorer requires an icon of ICO format, this means converting it first. Also changing the folder name will make the icon ineffective.

**FolderIkon** will take a JPG, ICO or a PNG file, convert it, create/edit the configuration file `desktop.ini`, set the appropriate permissions and [notify the Shell](https://docs.microsoft.com/windows/win32/api/shlobj_core/nf-shlobj_core-shchangenotify) about the icon. The icon will be hidden as it has generally no other use, *also it is a 256x256 image, nothing beautiful*.

However tilted images e.g those of product boxes etc. will not be displayed properly. A square image is recommended for optimum results. I suggest not to use images of other aspect ratios although they will work.

## Installation

Requires Python 3.6+ and Windows

```
pip install --upgrade folderikon
```

## Usage

Set the first ICO, JPG or PNG found in the current folder as the folder icon (subfolders not included).
```
folderikon
```

Set `image` as the folder icon of the current folder. `image` can be a URL as well.
```
folderikon -i image
```

Set `image` as the folder icon of `folder` and name the icon as `icon`
```
folderikon -i image -d folder -o icon
```

Extended usage information:
```
folderikon [-h] [--image IMAGE] [--icon ICON] [--folder FOLDER] [--delete-original] [--raise-on-existing] [--dont-hide-icon] [--silent] [--no-color]

A Windows utility to set folder icons.

optional arguments:
  -h, --help            show this help message and exit
  --image IMAGE, --input IMAGE, -i IMAGE
                        The image to set as folder icon. JPG, ICO and PNG formats are supported. URLs can be specified as well. Defaults to the       
                        first JPG/PNG file found in the current folder.
  --icon ICON, --output ICON, -o ICON
                        Output icon file name. Defaults to the name of first JPG/PNG found in current folder saved with a '.ico' extension.
  --folder FOLDER, -d FOLDER
                        The path of the folder whose icon is to be set. Defaults to the current folder.
  --delete-original, -f
                        Deletes the original image.
  --raise-on-existing   Raise an exception if the folder already has an icon.
  --dont-hide-icon      The folder icon is marked as hidden by default. Use this option to not do it.
  --no-color            Disables colored output.
```

### [TODO](TODO.md)

### [Changelog](CHANGELOG.md)

### [License]
MIT License