# replace_video_background_opencv
This application replaces your background in live video feed.

## Getting Started 

Clone this repo 
`git clone https://github.com/Hemanthhari2000/replace_video_background_opencv.git`

now `cd replace_video_background_opencv`

install all the requirements using 
`pip install -r requirements.txt`

now download the pretrained model from (here)[https://github-releases.githubusercontent.com/125507544/2ee360dc-5490-11e8-8173-41a5ea207792?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20210227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210227T163820Z&X-Amz-Expires=300&X-Amz-Signature=36097cd2d2127436b13263c39c8ba87af0d4a8b5bdc9a3e99a03663cbf28512d&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=125507544&response-content-disposition=attachment%3B%20filename%3Ddeeplabv3_xception_tf_dim_ordering_tf_kernels.h5&response-content-type=application%2Foctet-stream]

if you want to download the video then download from (here)[https://vod-progressive.akamaized.net/exp=1614454474~acl=%2A%2F1287384843.mp4%2A~hmac=ae540d1028fa5c13e16fed3407b60f2727bd77c8b070f34d85d5e0e89a1675cc/vimeo-prod-skyfire-std-us/01/685/13/328428416/1287384843.mp4?download=1&filename=Pexels+Videos+2098989.mp4]


and finally run `python cv.py`

## Preview

#### Result with background video

![](resources/result.PNG)

#### Result without background video

![](resources/onlyMask.PNG)

