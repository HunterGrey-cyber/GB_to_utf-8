# GB_to_utf-8
## 批量将gb2312或者gbk编码文件转换为utf-8
## Convert any coding format to the format you want

### demo运行说明
将第5五行dir变量改成你想的路径
将第7行改编成你想要储存到的路径（千万不能在dir或其子路径下）

运行demo.py后python会自动检测路径下的所有文件，当发现 gb 2312 编码的文件时，会在save_dir路径下创建一个新的文件夹，并将转换后的文件写入改文件夹中。

你可以根据自己的需要将将oringinal_format改成你自己想要的格式

你也可以在40行改变改变后的编码格式

### demo explain
change the fifth line to whatever direcotry you want in which you have held the files that need to be converted
Change the seventh line to the directory that you want to save conveted file
(Never put the sav_dir under dir!)

while runing demo.py python while automatically check all the files under that directory and when a file that is encoded by the type of format that you specified, python will create a new directory that is identical to the relative path of the oringinal file under the save_dir.After create the new directory python will put the converted file in there.

you can specify the oringinal format you want in the sixth line

the default output will be encoded in utf-8
you can also change that in line 40
