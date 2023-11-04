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
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
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

Here are some examples of how you can use Econimate:
1. To learn about a new economic concept, such as inflation or supply and demand.
2. To get help with a specific economics assignment or problem.
3. To stay up-to-date on the latest economic news and research.

Econimate is a great resource for anyone who wants to learn more about economics, regardless of the level of expertise. However, please keep in mind that it is still in beta and may not be able to answer all queries perfectly. So, please be patient and understanding as we continue to develop and improve Econimate.

An example of potential usage can be seen in this video. Example Usage Video

For more examples, please refer to the Example Usage Video.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Limitations

Here are some known problems and limitations of the project that we strive to resolve in future implementations:

Model (4th Generation) not sufficiently trained to provide figures for all types of graphs, especially for general Economic Concepts. Furthermore, there is a tendency for the LLM to not recognise more advanced Economics conepts. We will continue developing the model through tuning with different LLMs and machine learning methods. Currently, the Beta Version only supports creating a single graph for the video created. In future developments, we will enhance this feature to provide multiple graphs with smooth transitions between them. To make the lessons more engaging, additional features such as animations and virtual human interactions will be implemented.

Known limitations are documented in this video. Usage Ex1

See the Known Limitations Video for a full list of proposed features (and known issues).

<!-- ROADMAP -->
## Roadmap
<img width="1470" alt="Screenshot 2023-11-03 at 8 25 09 PM" src="https://github.com/yanhd2019/GoogleHackathon/assets/149416928/685882ca-dfa0-47a3-9c02-c448ecc8e2be">


- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Haodong Yan - hyan3@andrew.cmu.edu
Sewon Hong - sewonh@andrew.cmu.edu
Yuchen Zhu - yzhu7@andrew.cmu.edu
Jiayuan Ye - jye3@andrew.cmu.edu
Yukta Butala - ybutala@andrew.cmu.edu

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>
