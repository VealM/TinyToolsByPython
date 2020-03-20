# Try Tiny Tools by Running them in python!

## Scan

Run [scan](./scan.py) and get your phone photos into scanning document

It support iteration over multi-image-folders and generate scanning pics in corresponding scan-folders.

Example Usage:

``` shell
D:\NoteBook\scan> ls
D:\NoteBook\scan> scan.py test # test is a folder with pics NO sub-folders in it!
D:\NoteBook\scan> ls test # NO sub-folders in image folder!
D:\NoteBook\scan> score.jpg test.jpeg
D:\NoteBook\scan> python scan.py # By default, it will iterate img folders in current folder.
# You can point specific folder by use --data_dir
#Output like is:
# Processing for folder test in .
# Completed for folder test!
D:\NoteBook\scan> ls Scantest # get the result in ScanYourfolder(here Scantest)
D:\NoteBook\scan> score.jpg test.jpeg
```

### To do lists

- 1 Receive args from command line to specify the pic format(jpeg, jpg, png and so on). In this version, the scan format is consistent with the original format
- 2 Reinforce the scanning results for small font size and shallow color text in pics.

Number in the image is much clearer rather than text in left side.

![score-1.jpg](https://i.loli.net/2020/03/20/Be97xdkFpMl56Xv.jpg)
 
## Bland-Altman

Plot  Bland-Altman figure for features in 95% limits of agreement and calculate data points over limits in percentage

Run it by

``` shell
python Bland-Altman.py
```

For more details, look into BAplot in [BlandAltman](./BlandAltman.py)

