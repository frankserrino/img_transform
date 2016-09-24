import tensorflow as tf
#import matplotlib.image as mpimg
#import matplotlib.pyplot as plt

def transform_file(dimension,raw_image):        
    desired_width = dimension 
    desired_height = dimension

    raw_image_data = raw_image

    height, width, depth = raw_image_data.shape   

    image = tf.placeholder("float32", [height,width,depth]) 
     #Inserts a placeholder for a tensor that will be always fed. (?)

    exp_image = tf.expand_dims(image, 0)
    # add another dimension to image

    if height > width:
        resize_height = desired_height
        resize_width = int((desired_height / height) * width)
    else:
        resize_height = int((desired_width / width) * height) 
        resize_width = desired_width

    resized_image_batch = tf.image.resize_bilinear(exp_image, [resize_height,resize_width], align_corners=None, name=None)
    #resizes batched images, but we only have one but still use this command

    resized_image = tf.squeeze(resized_image_batch)
    #'squeezes' the image back into 3 dimensions from 4 caused by tf.expand'

    if height > width:
        padded_image = tf.image.pad_to_bounding_box(resized_image, 0, int((desired_width - resize_width)/2), desired_height, desired_width)
    else:
        padded_image = tf.image.pad_to_bounding_box(resized_image, int((desired_height - resize_height)/2), 0, desired_height, desired_width)
    grayscale = tf.reduce_mean(padded_image, 2)  # Compute mean along last axis

    with tf.Session() as session:
        result = session.run(grayscale, feed_dict={image: raw_image_data})
        return result

    
