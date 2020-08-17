# File: lidar.py
# Author: Leilani H. Gilpin
# Date: 30 December 2019
# Section: 1
# Email: lhg@mit.edu
# Description: Lidar interpretation code.   

import argparse
#import requests
import sys
import logging as log
import pprint as pp
import matplotlib.pyplot as plt

#import nltk

# Load the SDK
#%matplotlib inline
#from lyft_dataset_sdk.lyftdataset import LyftDataset
from nuscenes.nuscenes import NuScenes
from nuscenes.utils.data_classes import *

# Load the dataset
# Adjust the dataroot parameter below to point to your local dataset path.
# The correct dataset path contains at least the following four folders
# (or similar): images, lidar, maps, v1.0.1-train
data_root = '/Users/leilani/Dropbox (MIT)/car-can-explain/data/'
lyft_root = data_root+'lyft-data/'
nuscenes_root = data_root+'nuscenes-data/'
LIMIT = 5
debug = False # set to verbose for now
#level5data = LyftDataset(data_path=lyft_root,
#                         json_path=lyft_root+'v1.02-train/', verbose=debug)
data_name = 'v1.0-mini'

nusc = NuScenes(version=data_name, dataroot=nuscenes_root+data_name+'/', verbose=debug)

# TODO - Need verbose
# def old_main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('sentence', nargs='+',
#                     help='Sentence')
#     parser.add_argument("-v", "--verbose", action='store_true',
#                         help='This is the same as debug right now')
#     parser.add_argument("-f", "--format", action='store_true',
#                         help='The format of the dataset.  Right now,
#                         the default is nuscenes')
#     parser.add_argument("-d", "This is the default data path", action='store_true',
#                         default='/Users/leilani/Dropbox (MIT)//v1.02-train/')
#     args = parser.parse_args()

#     if args.verbose:
#         log.basicConfig(stream=sys.stdout, format="%(levelname)s: %(message)s",
#                         level=log.DEBUG)
#         log.info("Verbose output.")

# Right now, this does nothing because it's for testing 
def lyft_test():
    #     parser = argparse.ArgumentParser()
#     parser.add_argument('sentence', nargs='+',
#                     help='Sentence')
#     parser.add_argument("-v", "--verbose", action='store_true',
#                         help='This is the same as debug right now')
#     parser.add_argument("-f", "--format", action='store_true',
#                         help='The format of the dataset.  Right now,
#                         the default is nuscenes')
#     parser.add_argument("-d", "This is the default data path", action='store_true',
#                         default='/Users/leilani/Dropbox (MIT)//v1.02-train/')
#     args = parser.parse_args()

#     if args.verbose:
#         log.basicConfig(stream=sys.stdout, format="%(levelname)s: %(message)s",
#                         level=log.DEBUG)
#         log.info("Verbose output.")
    
    #level5data.list_scenes()
    my_scene = level5data.scene[0]
    process_scene(my_scene)

    my_sample = level5data.sample[10]
    level5data.render_pointcloud_in_image(my_sample['token'], pointsensor_channel='LIDAR_TOP')
    
def run_tests(scenes, limit=LIMIT):
    for scene in scene:
        process_scene(scene)

# A scene is a scene 25-45 seconds snippet of a car's journey.
def process_scene(scene):
    print(scene)
    my_sample_token = scene["first_sample_token"]
    # my_sample_token = level5data.get("sample", my_sample_token)["next"]  # proceed to next sample
    #level5data.render_sample(my_sample_token) # does not work right now, see [[documentation.org]]
    my_sample = level5data.get('sample', my_sample_token)
    process_sample(my_sample)

# A sample is an annotated keyframe of a scene at a given timestamp. A
# keyframe is a frame where the time-stamps of data from all the
# sensors should be very close to the time-stamp of the sample it
# points to.
def process_sample(sample):
    #print(sample)
    level5data.list_sample(sample['token'])
    # level5data.render_pointcloud_in_image(sample_token = sample["token"],
    #                                   dot_size = 1,
    #                                   camera_channel = 'CAM_FRONT')
    # ^ Again, doesn't work due to the bug 

    # Notice that the keys are referring to the different sensors that
    # form the sensor suite. Let's take a look at the metadata of a
    # sample_data taken from CAM_FRONT.
    #print(sample['data'])
    sensor_channel = 'CAM_FRONT'
    my_sample_data = level5data.get('sample_data', sample['data'][sensor_channel])
    print(my_sample_data)
    #level5data.render_sample_data(my_sample_data['token'])
    get_annotation(sample, my_sample_data, 16)

    
# sample_annotation refers to any bounding box defining the position of
#an object seen in a sample. All location data is given with respect
#to the global coordinate system. 
def get_annotation(sample, sample_data, index):
    my_annotation_token = sample['anns'][16]
    my_annotation =  sample_data.get('sample_annotation', my_annotation_token)
    print(my_annotation)

# Object instance are instances that need to be detected or tracked by
# an AV (e.g a particular vehicle, pedestrian).

#We generally track an instance across different frames in a
#particular scene. However, we do not track them across different
#scenes. In this example, we have 16 annotated samples for this
#instance across a particular scene
def get_instance(index):
    my_instance = level5data.instance[index]
    print(my_instance)

def nuscenes_test():
    nusc.list_scenes()
    my_scene = nusc.scene[0]
    print(my_scene)
    first_sample_token = my_scene['first_sample_token']
    
    my_sample = nusc.get('sample', first_sample_token)
    print(my_sample)

    sensor = 'CAM_FRONT'
    cam_front_data = nusc.get('sample_data', my_sample['data'][sensor])
    print(cam_front_data)

    lidar_data = nusc.get('sample_data', my_sample['data']['LIDAR_TOP'])
    pp.pprint(lidar_data)
    pp.pprint(lidar_data['token'])
    pp.pprint(lidar_data['calibrated_sensor_token'])
    file_path = nuscenes_root+data_name+'/'+lidar_data['filename']
    points = LidarPointCloud.from_file(file_path)
    pp.pprint(points.points)
#    pc.render_intensity()
    nusc.render_sample_data(my_sample['data']['LIDAR_TOP'], nsweeps=5,
                            underlay_map=True)
    # plt.figure(figsize=(9, 16))
    # plt.imshow(im)
    # plt.scatter(points[0, :], points[1, :], c=coloring, s=dot_size)
    # plt.axis('off')

    # print(pc.points.shape)
    # print(pc.nbr_dims)

    
def lidar_test():
    scene_name = 'scene-0061'
    scene_tokens = [s['token'] for s in nusc.scene if s['name'] == scene_name]
    assert len(scene_tokens) == 1, 'Error: Invalid scene %s' % scene_name

    export_scene_pointclouds_as_obj(nusc, out_path, scene_tokens[0],
                            channel='LIDAR_TOP', verbose=verbose)
    
#    nusc.render_sample_data(lidar_data['token'])
#    print(nusc.sensor)


def main():
    nuscenes_test()
    #lyft_test()
#    lidar_test()
    
if __name__ == "__main__":
    main()

