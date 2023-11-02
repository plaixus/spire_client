SPIRE client provides multiple helper functions to allow communication with the SPIRE server and manipulation of ROS bagfiles and topics

Function list:
- record: Given a list of ROS topics to record, the duration of the recording and the name of the resulting filename, it creates a bagfile of messages from the selected topics in the server
- play: Given a ROS bagfile name, it plays back the bagfile
- info: Returns bagfile info for the bagfile name you enter
- download: Extract a bagfile converted to CSV
- get_dataset: Given a bagfile containing images, returns a zip file including all images from that bagfile
- rosbag_list: Lists all bagfiles currently residing in the server
- compress: Compresses the required bagfile
- decompress: Decompresses the required bagfile
- reindex: Repairs the index of the required bagfile
- check: Checks whether the required bagfile is playable
- rosbag_filter: Filters selected topics from required bagfile into a new output bagfile
- fix: Fixes the required bagfile and produces the new repaired output bagfile