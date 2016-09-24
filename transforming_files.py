def transform_file(dimension,raw_image):	
	import tensorflow as tf
	import matplotlib.image as mpimg
	import matplotlib.pyplot as plt


	desired_width = dimension 
	desired_height = dimension

	# First, load the image again
	#filename = "L03/small_bathroom_design_pictures.jpg"
#	filename = "/Users/fs/Downloads/LearningTensorFlowExercises/L03/Woonkamer2.jpg"
    raw_image_data = raw_image
#	raw_image_data = mpimg.imread(filename)
	#img=mpimg.imread(filename)

	#plt.show()

	print(raw_image_data.shape, raw_image_data.dtype)
	height, width, depth = raw_image_data.shape   


	image = tf.placeholder("float32", [height,width,depth]) 
	 #Inserts a placeholder for a tensor that will be always fed. (?)

	exp_image = tf.expand_dims(image, 0)
	# add another dimension to image

	#adj_width = int((desired_height / height) * width) # proportional smaller width given desired_height
	#adj_height = int((desired_width / width) * height) # proportional smaller height given DESORED_WIDTH

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
	    print(result.shape)
	    imgplot = plt.imshow(raw_image_data)
	    plt.show()
	    plt.imshow(result, cmap="gray")
	    plt.show()
	#tf.image.resize_bilinear(images, size, align_corners=None, name=None)  
	#tf.expand_dims(input, dim, name=None)
	#tf.squeeze(input, squeeze_dims=None, name=None)
    
    return
