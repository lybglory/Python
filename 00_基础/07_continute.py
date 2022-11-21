# encoding=utf-8
i = 1
while i <= 5:
    if i == 3:
        print(f'第{i}个苹果有虫子！不吃！')
        # 在continue之前一定要修改计数器，否则会陷入死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
