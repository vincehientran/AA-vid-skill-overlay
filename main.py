import cv2

skill = {
    '1':(0,0),
    '2':(1,0),
    '3':(2,0),
    '4':(3,0),
    '5':(4,0),
    'W(UP)':(5,0),
    'z':(0,1),
    'x':(1,1),
    'c':(2,1),
    'v':(3,1),
    'b':(4,1),
    'W(DN)':(5,1),
    'M4':(6,1),
    'M5':(7,1),
    'q':(0,2),
    'e':(1,2),
    'r':(2,2),
    't':(3,2),
    'f':(4,2),
    'g':(5,2),
    'h':(6,2),
    'n':(7,2)
}

def get_skills_frame(frame):
    crop_width = 400
    crop_height = 110

    start_x = int((1920 - crop_width) / 2) + 10
    start_y = int(1080 - crop_height)
    cropped_frame = frame[start_y:start_y + crop_height, start_x:start_x + crop_width]

    return cropped_frame

def get_skill(coords, frame):
    x, y = coords
    crop_width = 31
    crop_height = 31

    offset = 0 if x < 6 else 6

    start_x = 15+((x*crop_width)-1) + offset
    start_y = 4+((y*crop_height)+3)
    cropped_frame = frame[start_y:start_y + crop_height, start_x:start_x + crop_width]

    return cropped_frame

def play_video(video_path):
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open the video")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break
        
        frame = get_skills_frame(frame)
        skillFrame = get_skill(skill['q'], frame)

        cv2.imshow('Video', skillFrame)

        if cv2.waitKey(6) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_file_path = '../video.mkv'

play_video(video_file_path)
