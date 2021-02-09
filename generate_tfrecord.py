from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
import tensorflow.compat.v1 as tf
import shutil

from PIL import Image
import dataset_util
from collections import namedtuple, OrderedDict

flags = tf.app.flags
flags.DEFINE_string('csv_input', 'ground_truth.csv', 'Path to the CSV input')
flags.DEFINE_string('output_path', 'dataset.tfrecord', 'Path to output TFRecord')
flags.DEFINE_string('dataset_dir', 'dataset/', 'Path to the dataset dir')
FLAGS = flags.FLAGS


def split(df, group):
    # Spliting the object from the files
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    # Opening and readinf the files
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    # Encode the image in jpeg format to array values
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    # Setting up the image size
    width, height = image.size
    
    #Creating the boundary box coordinate instances such as xmin,ymin,xmax,ymax
    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] )
        xmaxs.append(row['xmax'] )
        ymins.append(row['ymin'] )
        ymaxs.append(row['ymax'] )
        classes.append(row['class'].encode('utf8'))
        
    # This is already exisiting code to convert csv to tfrecord
    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/label': dataset_util.bytes_list_feature(classes),
    }))
    return tf_example


def main(_):

    # Creating a TFRecordWriter instance
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    #selecting the path to the image folder
    path = os.path.join(os.getcwd(),FLAGS.dataset_dir)
    # Reading the csv from the data folder
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    # After the successful conversion the message prompts
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()