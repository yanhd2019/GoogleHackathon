# GoogleHackathon
<p align="center">
  <img src="https://github.com/yanhd2019/GoogleHackathon/assets/149416928/f9b8c193-8467-4989-b2bc-43a5e5ea1ec2" width="388">
</p>


<h3 align="center">ECONIMATE</h3>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Have you ever tried to dive into the world of economics, only to find yourself overwhelmed by the countless graphs and complex notes? Well, don't worry! Meet Econimate, your friendly AI tutor that makes learning economic concepts a breeze. Whether you're a student, a professional, or simply curious about the world of economics, Econimate is here to help you grasp these concepts in a fun and easy-to-understand manner through engaging and informative videos.


<!-- GETTING STARTED -->
## Getting Started


### Importing Libraries

1. Install the client library and import necessary modules.
   ```js
    from functions import *
    import google.generativeai as palm
    import base64
    import json
    import pprint
    import cv2
    from moviepy.editor import ImageClip, AudioFileClip, concatenate_audioclips
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
   ```
2. We utilized Google's Palm2 to assist in generating both the explanation and the code for creating a reference graph. To access the Palm2 API, you can obtain an API_KEY from [here](https://console.cloud.google.com/welcome?hl=ko&_ga=2.223201821.704841096.1699130066-1569134934.1698429316&_gac=1.183110100.1699130066.CjwKCAjw15eqBhBZEiwAbDomEnuAMRbTYfGsjtAzJWzYqBW2-cCfpdz_ijcF0VY5xhFDL75tMDxEWhoCvMEQAvD_BwE&project=storied-radius-362713).


  ```
  const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use Econimate, simply run the provided code in your local Python environment and enter your Economics doubts when prompted. Econimate will then generate a video that explains the concept in a clear and concise way, using graphs and audio to make your learning easy and fun.

Have a look at how amazing videos Econimate generates:


https://github.com/yanhd2019/GoogleHackathon/assets/149416928/81acbb2e-6b58-441a-bf58-4aca8f8e7bf3



Here are some examples of how you can use Econimate:
1. To learn about a new economic concept, such as inflation or supply and demand.
2. To get help with a specific economics assignment or problem.
3. To stay up-to-date on the latest economic news and research.

Econimate is a great resource for anyone who wants to learn more about economics, regardless of the level of expertise. However, please keep in mind that it is still in beta and may not be able to answer all queries perfectly. So, please be patient and understanding as we continue to develop and improve Econimate.

An example of potential usage can be seen in [this video](https://drive.google.com/file/d/11ge-2Gi4svGetE5dMaKMrKtyzyRVyzeH/view?usp=sharing).


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Limitations

Here are some known problems and limitations of the project that we strive to resolve in future implementations:

Model (4th Generation) not sufficiently trained to provide figures for all types of graphs, especially for general Economic Concepts. Furthermore, there is a tendency for the LLM to not recognise more advanced Economics conepts. We will continue developing the model through tuning with different LLMs and machine learning methods. Currently, the Beta Version only supports creating a single graph for the video created. In future developments, we will enhance this feature to provide multiple graphs with smooth transitions between them. To make the lessons more engaging, additional features such as animations and virtual human interactions will be implemented.


<!-- ROADMAP -->
## Roadmap
 Stage 1:
 
![WhatsApp Image 2023-11-03 at 20 26 05](https://github.com/yanhd2019/GoogleHackathon/assets/149416928/6d7cb024-936d-4511-bfd3-171d8e2e9fea)

At present, we've set up a process where you can ask your economics questions to our chatbot, and in return, you'll receive a video with the answers that will be downloaded to your local files. You can check out the steps we've followed in the diagram above, and you can access the code to see how it all works.

A pivotal milestone in reaching this stage involved training the Palm2 API using our prompts. If you're interested in seeing how this was accomplished, you can access the [video](https://drive.google.com/file/d/1GvOEAXIKn1mD6oyD3MrFSpLnq0bmV3ZA/view?usp=sharing) that demonstrates the process. It's a great way to gain insight into the behind-the-scenes work that contributes to the chatbot's performance.



Stage 2: 

Our next exciting endeavor is to develop a chatbot-like interface that allows you to ask your questions directly and receive video answers in real-time. We're working diligently to bring this feature to life, making the process of accessing economic insights even more seamless and convenient for you. Stay tuned for our upcoming enhancements!


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Created with ❤️ by:

Haodong Yan - hyan3@andrew.cmu.edu     
Sewon Hong - sewonh@andrew.cmu.edu     
Yuchen Zhu - yzhu7@andrew.cmu.edu   
Jiayuan Ye - jye3@andrew.cmu.edu      
Yukta Butala - ybutala@andrew.cmu.edu    


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

In our journey through this hackathon, we've received invaluable support and guidance from some remarkable individuals. Special gratitude goes out to Josh Gordon for his invaluable introduction to the Palm2 API, which played a pivotal role in our project. We also want to express our appreciation to the entire Google team for their dedicated guidance and mentorship over the past week. We would like to extend our heartfelt thanks to Prof. Ganesh Mani for his unwavering support and encouragement. Your collective efforts and insights have been instrumental in our success. Thank you all for your contributions to this incredible experience!


<p align="right">(<a href="#readme-top">back to top</a>)</p>
