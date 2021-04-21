'''写文件'''

# w : 覆盖写入
# a : 追加写入
# 在vscode中，当前目录指的是open folder命令打开的那个目录
# 在一般情况下，当前目录指的是当前文件所在的目录
# ./表示当前目录，可以省略
file = open('./book.txt','w',encoding='utf-8')
file.write('问君能有几多愁，恰似一江春水向东流。\n')
file.close()

with open('book.txt','a',encoding='utf-8') as file:
    file.write('八千里路云和月，三十功名尘与土。\n')


# 练习： 复制tulips.jpg -> flower.jpg

with open(r'.\day05\Tulips.jpg','rb') as img:
    with open(r'day05\flower.jpg','wb') as newimg:
        newimg.write(img.read())