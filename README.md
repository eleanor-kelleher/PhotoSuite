# PhotoSuite

I tend to take a lot of photos of birds. 
This is a small collection of scripts that I use for managing my photos. 
Hopefully I'll get more ideas on how to automate this whole process more in the future!

## Import files from SD card

```import_sd_photos.py```

This one goes through all the directories on my SD card that are created by the camera,
and imports each file onto my D drive. It follows my file structure of `/photos_dir/year/yyyy-mm-dd/file.jpg` and
creates these folders if they do not exist. 

The only thing left for me to do is confirm all photos are moved, delete the files on the SD card
(I'm scared to automate the deletion for now), rename the dated photo folder to something that makes more sense
(e.g. `2024-02-04 Dublin Bay Excursion`), and start tagging bird species!
Maybe some of this automation process can be automated in the future.

## Rename Irish Bird Blog directories

```rename_directories.py```

This one is for organising photos destined for an [Irish Bird Blog](https://theirishbirdblog.com/) article.
When curating decent photos I usually search by species tag, copy the most presentable ones into a folder
for that bird. It ends up a mess of `DSCN1234.JPG` and `IMG_5678.JPG` names, so this script goes through
all bird folders in my IrishBirdBlog directory, and renames the files to something more appropriate based on
the folder name:

```
7 2022-06 Puffin\DSCN1234.JPG  ->  7 2022-06 Puffin\IBB_Puffin_1.JPG
```

## Delete dangling RAWs

```delete_raws.py```

As of August 2024, I'm now also saving JPG and RAW (CR3) files. I currently don't really edit RAW files, but
I am keeping them for retroactive editing at some point in the future when that is a part of my process.
JPGs are easier for me to handle in my current day-to-day - they are faster to load to preview
(for deletion or tagging) and also they can natively be tagged in Windows (I don't think this is possible
with RAWs but happy to be corrected).

This script goes through all additional RAW files that I am saving, and check to see if the corresponding
JPG exists. If it does not, it means I have deleted it and so the script moves the RAW file with the same name
to a DELETE folder (I'm still scared to automate the deletion).

From just August to October, this deletion script has removed almost 1000 RAW files and saved over 33 GB of space!