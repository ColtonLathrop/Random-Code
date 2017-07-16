import load_image as li

tar_img = 'test2.png'
assci_output = ''

pixel_img = li.get_image(tar_img)
pixel_size = li.get_size(tar_img)
#print('----------------------------')
limit_x = pixel_size[0] - 1
limit_y = pixel_size[1] - 1
#print(pixel_size[0], pixel_size[1])

for x in range(limit_y):
    for i in range(limit_x):
        if pixel_img[i,x][3] > 0:
            assci_output = assci_output + '@'
        else:
            assci_output = assci_output + ','
    assci_output = assci_output + '\n'
print(assci_output)
