import os
import tensorflow as tf
import numpy as np
import cv2
import time


class CNN(object):
    detection_graph = tf.Graph()
    def __init__(self):
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile('frozen_inference_graph.pb', 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
    def get_image_feature_map(self, image):
        start = time.time()
        with self.detection_graph.as_default():
            with tf.Session(graph=self.detection_graph) as sess:
                image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
                feature_vector = self.detection_graph.get_tensor_by_name(
                    "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/Relu6:0")
                image_np = cv2.resize(image, (900, 400))
                image_np_expanded = np.expand_dims(image_np, axis=0)
                rep = sess.run([feature_vector], feed_dict={image_tensor: image_np_expanded})
                return np.array(rep).reshape(-1, 128)