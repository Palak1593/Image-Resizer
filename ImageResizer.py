# import cv2
# image=cv2.imread("images.jpeg",cv2.IMREAD_UNCHANGED)
# # cv2.imshow("title",image)
# # cv2.waitKey(0)

# #percent by which the image is resized 
# scale_percent=50

# #calculate the 50 percent of original dimanesions
# new_width=int(image.shape[1] *scale_percent /100)

# new_height =int(image.shape[0] *scale_percent /100) 

# dsize=(new_width, new_height) 

# #resize image
# output=cv2.resize(image, dsize)

# cv2.imwrite('new_image.png',output)  

# cv2.waitKey(0)     

import cv2

image = cv2.imread("Screenshot 2023-07-02 at 1.29.27 AM.png", cv2.IMREAD_UNCHANGED)

if image is not None:
    cv2.imshow("title", image)  #These lines display the loaded image in a window with the title "title" using cv2.imshow(). 
    
    cv2.waitKey(0)    #cv2.waitKey(0) waits for a keyboard event and returns the key code of the pressed key. 
                    #   Here, 0 indicates that it will wait indefinitely until a key is pressed.

    # percent by which the image is resized 
    scale_percent = 50   #the output image will be resized to 50% of the original dimensions.

    # calculate the 50 percent of original dimensions
    new_width = int(image.shape[1] * scale_percent / 100) # image.shape[1] represents the width,
    new_height = int(image.shape[0] * scale_percent / 100) #image.shape[0] represents the height,

    dsize = (new_width, new_height) 

    # resize image
    output = cv2.resize(image, dsize)   #dsize: The desired size for the output image. It can be specified as a tuple (width, height) 

    cv2.imwrite('new_image.png', output  )  #used in OpenCV to save an image to a file. 
                                        #    It takes the image data and writes it to the specified file location.