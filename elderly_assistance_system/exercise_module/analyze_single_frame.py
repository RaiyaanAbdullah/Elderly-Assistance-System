import json


  
video_x=1920
video_y=1088



# Iterating through the json
# list
def get_keypoints(json_file):
    f = open(json_file,)
    data = json.load(f)
    joint_names=['head','chest','l_shoulder','l_elbow','l_hand','r_shoulder','r_elbow','r_hand','abdomen','l_hip','l_knee','l_ankle','r_hip','r_knee','r_ankle','l_eye','r_eye','l_ear','r_ear','r_feet','r_toe','r_heel','l_feet','l_toe','l_heel']
    
    keypoints=data['people'][0]['pose_keypoints_2d']
    
    keypoints_dict={}
    
    for i in range(0,25):
        
        #print(joint_names[i],"- X:",keypoints[i*3],"- Y:",keypoints[i*3+1],"- P:",keypoints[i*3+2])
        keypoints_dict[joint_names[i]]={"X":keypoints[i*3]/video_x,"Y":keypoints[i*3+1]/video_y,"P":keypoints[i*3+2]}
    return keypoints_dict



yo = get_keypoints('D:/Elderly Assistant External files/Exercise Videos/Openpose variations/openpose-1.7.0-binaries-win64-gpu/openpose\python/output_json_folder/12-f-rf1_000000000000_keypoints.json')

