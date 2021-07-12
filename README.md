# find_and_move_dublicate_files

### Background.
For a long time, I put all the images from my phone in one folder. 
There are a lot of files accumulated there, and a lot of duplicates among the files in different subfolders. 
Duplicates should be deleted by first moving them to a separate folder for analysis.

### Gui
![Gui](https://github.com/DelionA/find_and_move_dublicate_files/Images/screenshot1.png)

# before
/Folder
    ./Folder_1
        file_name_1.jpeg
        file_name_2.jpeg
    ./Folder_2
        file_name_1.jpeg
        file_name_2.jpeg
        file_name_3.jpeg
    ./Folder_3
        file_name_2.jpeg
        file_name_3.jpeg

# after
/Folder
    ./Folder_1
        file_name_1.jpeg
        file_name_2.jpeg
    ./Folder_2
        file_name_3.jpeg
    ./Folder_3

/Dublicated
    0_file_name_1.jpeg
    1_file_name_2.jpeg
    2_file_name_2.jpeg
    3_file_name_3.jpeg
    
    
Autor DelionA
