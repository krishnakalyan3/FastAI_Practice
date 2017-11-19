#!/usr/bin/env python3

def img_stats(PATH):
    img = plt.imread(f'{PATH}valid/cats/{files[0]}')
    print(img.shape)
    plt.imshow(img)



