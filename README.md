# find_and_move_dublicate_files

### Background.
For a long time, I put all the images from my phone in one folder. 
There are a lot of files accumulated there, and a lot of duplicates among the files in different subfolders. 
Duplicates should be deleted by first moving them to a separate folder for analysis.

### Gui
![Gui](https://github.com/DelionA/find_and_move_dublicate_files/blob/master/Images/screenshot1.png)

# before
/Folder<br />
..../Folder_1<br />
........file_name_1.jpeg<br />
........file_name_2.jpeg<br />
..../Folder_2<br />
........file_name_1.jpeg<br />
........file_name_2.jpeg<br />
........file_name_3.jpeg<br />
..../Folder_3<br />
........file_name_2.jpeg<br />
........file_name_3.jpeg<br />

# after
/Folder<br />
..../Folder_1<br />
........file_name_1.jpeg<br />
........file_name_2.jpeg<br />
..../Folder_2<br />
........file_name_3.jpeg<br />
..../Folder_3<br />

/Dublicated<br />
....0_file_name_1.jpeg<br />
....1_file_name_2.jpeg<br />
....2_file_name_2.jpeg<br />
....3_file_name_3.jpeg<br />
    
    
Autor DelionA
