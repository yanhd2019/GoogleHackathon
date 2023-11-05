import google.generativeai as palm
import base64
import json
import pprint
import cv2
from moviepy.editor import ImageClip, VideoFileClip, AudioFileClip, concatenate_audioclips
import subprocess
import gtts
from playsound import playsound
from IPython.display import Audio
from gtts import gTTS
import tempfile
import spacy
import subprocess
import os
import shutil

def user_input(prompt = "Hi! Ask me an Economics Concept!\n"):
  user_input = input(prompt)
  return user_input
  
def generate_response(text, defaults, input = "Hi"):
  response = palm.generate_text(
    **defaults,
    prompt=text + "input:"+input+"\n"
  )
  return response.candidates[0]['output']
  
def segment_response(response):
    rt_val = 0
    if response == "Hi! Ask me an Economics Concept!\n":
        rt_val = -1 #User says hi
        text = response
        code = ""
    elif response == "This is not an Economic concept. Ask me anything about Economics instead!\n":
        rt_val = -2 #user ask non econ stuff
        text = response
        code = ""
    elif response == "":
        rt_val = -3 #API gives up
        text = response
        code = ""
    else:
        code, text = segment_strings(response)
        if code == "":
            if text == "":
                rt_val = 3 #Case WHAT THERE IS NOTHING YET SOMETHING
            else:
                rt_val = 1 #Case no figure

        elif text == "":
            rt_val = 2 #Case no text
        else:
            rt_val = 0
    return code, text, rt_val

def segment_strings(output):
    tempfile = "segment.py"
    
    beginning = """
import google.generativeai as palm
import base64
import json
import pprint
import subprocess
import os

# Configure the client library by providing your API key.
palm.configure(api_key="AIzaSyDQjYLfE6SMtZaJff4qbBAXudNBAXUulV4")
model_id="models/text-bison-001"
"""
    prompt1 = "prompt1= '''extract the python code from the following text if there exist and code section in text and remove all none python codes. Make the response to only have the code that is ready to run:\n"

    extract_code = """
'''
completion1=palm.generate_text(
    model=model_id,
    prompt=prompt1,
    temperature=0.99,
    max_output_tokens=1024,
)
result1 = completion1.candidates[0]['output']
"""
    prompt1_5 = "prompt1_5 = 'extract the python code from the following text if there exist. Make the response to only have the code that is ready to run:' + result1"

    extract_code1_5 = """
completion1_5=palm.generate_text(
    model=model_id,
    prompt=prompt1_5,
    temperature=0.99,
    max_output_tokens=1024,
)
result1_5 = completion1_5.candidates[0]['output']
"""
    
    prompt2 = "prompt2= '''extract the explanation from the following text. Make the response to only have the explanation:\n"

    extract_text = """
'''
completion2=palm.generate_text(
    model=model_id,
    prompt=prompt2,
    temperature=0.99,
    max_output_tokens=1024,
)
result2 = completion2.candidates[0]['output']

with open('codefile.txt', 'w') as file1:
    file1.write(result1_5)

with open('textfile.txt', 'w') as file2:
    file2.write(result2)

"""
    
#     code = beginning + prompt1 + extract_code + prompt2 + extract_text
    
    #create the tempfile
    with open(tempfile, 'w') as file:
        file.write(beginning)
        file.write(prompt1)
        file.write(output)
        file.write(extract_code)
        file.write(prompt1_5)
        file.write(extract_code1_5)
        file.write(prompt2)
        file.write(output)
        file.write(extract_text)
    
    #run the temp file
    subprocess.run(['python', tempfile], check=True)
    
    #remove the temp file
    os.remove(tempfile)
    
    with open('codefile.txt', 'r') as file1:
        code = file1.read()
    with open('textfile.txt', 'r') as file2:
        text = file2.read()
        
    os.remove('codefile.txt')
    os.remove('textfile.txt')
    
    if "```python" in code:
        code = code.replace("```", "")
        code = code.replace("python", "")
        
    return code, text
    
def save_audio(j, text, audio_folder = "audios"):
    tts = gtts.gTTS(text)

    #check for the figures folder, create one if DNE
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    tts.save(os.path.join(audio_folder, f"temp_audio{j+1}.aac"))
    return j+1
    
def code_to_figure(i, code, figures_folder="figures"):
    tempfile = "tempcode.py"
    
    #check for the figures folder, create one if DNE
    if not os.path.exists(figures_folder):
        os.makedirs(figures_folder)
        
    #check for matplotlib import in the code
    if "import matplotlib.pyplot as plt" not in code:
        code = "import matplotlib.pyplot as plt\n" + code
    
    npy = "import numpy as np\nimport pandas as pd\n"
    #remove .show to let .savefig function
    code = code.replace("plt.show()", "")
    
    #apply .savefig and add it to the tempfile
    save_code = f"""
plt.savefig('figures/figure{i+1}.jpg')

"""
    code = npy + code 
    code += save_code
    
    #create the tempfile
    with open(tempfile, 'w') as file:
        file.write(code)
    
    #run the temp file
    subprocess.run(['python', tempfile], check=True)
    
    #remove the temp file
    os.remove(tempfile)
    
    return i + 1
    
def reset_figures(figures_path = "figures"):
    if not os.path.exists(figures_path):
        print("figures folder DNE")
        os.makedirs(figures_path)
        return 0
    
    #remove the folder(easiest way)
    shutil.rmtree(figures_path)
    
    #remake the folder
    os.makedirs(figures_path)
    return 0
    
def reset_audios(audios_path = "audios"):
    if not os.path.exists(audios_path):
        print("audios folder DNE")
        os.makedirs(audios_path)
        return 0
    
    #remove the folder(easiest way)
    shutil.rmtree(audios_path)
    
    #remake the folder
    os.makedirs(audios_path)
    return 0
    
def reset_results(results_path = "results"):
    if not os.path.exists(results_path):
        print("figures folder DNE")
        os.makedirs(results_path)
        return 0
    
    #remove the folder(easiest way)
    shutil.rmtree(results_path)
    
    #remake the folder
    os.makedirs(results_path)
    return 0

def video_gen(k, text = "", result_folder="results", audio_folder="audios", figures_folder="figures"):
    # Load the image and audio
    image = VideoFileClip(os.path.join(figures_folder, f"figure{k+1}.jpg"))
    audio = AudioFileClip(os.path.join(audio_folder, f"temp_audio{k+1}.aac"))

    # Set the audio for the video clip
    video = image.set_audio(audio)

    # Specify the duration in seconds
    #start_time=0
    #end_time=50
    video=video.subclip()#start_time,end_time)
    print("1\n")
    # Export the final video
    output_path = os.path.join(result_folder, f"result{k+1}.mp4")
    video.write_videofile(output_path, codec='libx264')
    print("2\n")
    with open(os.path.join(result_folder, f"transcript{k+1}.txt"),'w') as transcript:
        transcript.write(text)
    return k + 1

# import os
# import cv2
# from moviepy.editor import ImageClip, AudioFileClip, concatenate_audioclips
# import subprocess

# def generate_video(k, text = "",result_folder="results", audio_folder="audios", figures_folder="figures", fps=30):
#     # Create results folder if it doesn't exist
#     if not os.path.exists(result_folder):
#         os.makedirs(result_folder)

#     # Define valid audio and figure extensions
#     valid_audio_exts = ('.mp3', '.wav', '.aac', '.m4a')
#     valid_figure_exts = ('.jpeg','.jpg')

#     # # Get the sorted list of audio files
#     # audio_files = sorted([files for files in os.listdir(audio_folder)
#     #                       if files.lower().startswith("response") and files.lower().endswith(valid_audio_exts)])
#     audio_files = os.path.join(audio_folder, f"temp_audio{k+1}.aac")
#     figure_files = os.path.join(figures_folder, f"figure{k+1}.jpg")

#     # # Get the sorted list of figure files
#     # figure_files = sorted([files for files in os.listdir(figures_folder)
#     #                        if files.lower().startswith("figure") and files.lower().endswith(valid_figure_exts)])

#     # Create clips for each audio and image pair
#     # clips = []
#     # for i, audio_file in enumerate(audio_files):
#     #     audio = AudioFileClip(os.path.join(audio_folder, audio_file))
#     #     if i < len(figure_files):  # If there's a corresponding image for the audio
#     #         img_clip = ImageClip(os.path.join(figures_folder, figure_files[i]))
#     #         clip = img_clip.set_duration(audio.duration).set_audio(audio)
#     #         clips.append(clip)
#     #     else:  # When there's one more audio than images
#     #         last_img = ImageClip(os.path.join(figures_folder, figure_files[-1]))
#     #         clip = last_img.set_duration(audio.duration).set_audio(audio)
#     #         clips.append(clip)
#     audio = AudioFileClip(audio_files)
#     img_clip = VideoFileClip(figure_files)
#     clips = img_clip.set_duration(audio.duration).set_audio(audio)


#     target_size = (1920, 1080)
#     resized_clips = clips.resize(newsize=target_size)

#     # Prepare for video writing using OpenCV
#     temp_video_avi = os.path.join(result_folder, f"temp_result{k+1}.avi")
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter(temp_video_avi, fourcc, fps, target_size)

#     # Extract audio tracks and combine them
#     audio_clips = audio
#     # combined_audio = concatenate_audioclips(audio_clips)
#     audio_filename = os.path.join(audio_folder, "temp_audio.aac")
#     audio_clips.write_audiofile(audio_filename, codec='aac')

#     # Write frames to OpenCV Video Writer
    
#     for frame in clips.iter_frames(fps=fps, dtype="uint8"):
#         out.write(frame)

#     out.release()

#     # Combine video-only AVI and audio track into final AVI
#     # final_avi = os.path.join(result_folder, f"result{k+1}.avi")
#     # cmd = [
#     #     'ffmpeg',
#     #     '-i', temp_video_avi,
#     #     '-i', audio_filename,
#     #     '-c:v', 'copy',
#     #     '-c:a', 'aac',
#     #     '-strict', 'experimental',
#     #     final_avi
#     # ]
#     # subprocess.call(cmd)
    
#     final_mp4 = os.path.join(result_folder, f"result{k+1}.mp4")
#     cmd = [
#         'ffmpeg',
#         '-i', temp_video_avi,
#         '-i', audio_filename,
#         '-c:v', 'libx264',
#         '-c:a', 'aac',
#         '-strict', 'experimental',
#         '-preset', 'fast',
#         '-b:v', '5000k',
#         final_mp4
#     ]
#     subprocess.call(cmd)

#     # Remove temporary files
#     # os.remove(temp_video_avi)
#     # os.remove(audio_filename)
#     # Remove temporary files
#     os.remove(temp_video_avi)
#     os.remove(audio_filename)

#     with open(os.path.join(result_folder, f"transcript{k+1}.txt"),'w') as transcript:
#         transcript.write(text)
#     return k + 1
    


#     import os
# import cv2
# from moviepy.editor import ImageClip, AudioFileClip, concatenate_audioclips
# import subprocess

def generate_video(k, text = "", result_folder="results", audio_folder="audios", figures_folder="figures", fps=30):
    # Create results folder if it doesn't exist
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # Define valid audio and figure extensions
    valid_audio_exts = ('.mp3', '.wav', '.aac', '.m4a')
    valid_figure_exts = ('.jpeg','.jpg')

    # Get the sorted list of audio files
    # audio_files = sorted([files for files in os.listdir(audio_folder)
    #                       if files.lower().startswith("response") and files.lower().endswith(valid_audio_exts)])

    audio_file = os.path.join(audio_folder, f"temp_audio{k+1}.aac")
    image_file = os.path.join(figures_folder, f"figure{k+1}.jpg")

    # Get the sorted list of figure files
    # figure_files = sorted([files for files in os.listdir(figures_folder)
    #                        if files.lower().startswith("figure") and files.lower().endswith(valid_figure_exts)])

    # Create clips for each audio and image pair
    audio = AudioFileClip(audio_file)
    clips = ImageClip(image_file).set_duration(audio.duration).set_audio(audio)

    target_size = (1920, 1080)
    resized_clips = clips.resize(newsize=target_size)
    
    # Prepare for video writing using OpenCV
    temp_video_avi = os.path.join(result_folder, f"temp_result{k+1}.avi")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(temp_video_avi, fourcc, fps, target_size)

    # Extract audio tracks and combine them
    audio_clips = clips.audio
    combined_audio = audio_clips
    audio_filename = os.path.join(result_folder, "temp_audio.aac")
    combined_audio.write_audiofile(audio_filename, codec='aac')

    for frame in resized_clips.iter_frames(fps=fps, dtype="uint8"):
        out.write(frame)
    
    # Write frames to OpenCV Video Writer
    # for clip in resized_clips:
    #     for frame in clip.iter_frames(fps=fps, dtype="uint8"):
    #         out.write(frame)

    out.release()

    # Combine video-only AVI and audio track into final MP4
    final_mp4 = os.path.join(result_folder, f"result{k+1}.mp4")
    cmd = [
        'ffmpeg',
        '-i', temp_video_avi,
        '-i', audio_filename,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-preset', 'fast',
        '-b:v', '5000k',
        final_mp4
    ]
    subprocess.call(cmd)

    # Remove temporary files
    os.remove(temp_video_avi)
    os.remove(audio_filename)

    with open(os.path.join(result_folder, f"transcript{k+1}.txt"),'w') as transcript:
        transcript.write(text)

    return k + 1
