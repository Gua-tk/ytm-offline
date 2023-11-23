<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Code quality][codacy-shield]][codacy-url]
[![Top language][language-shield]][language-url]
[![Language count][language-count-shield]][language-count-url]
[![GNU GPL v3 License][license-shield]][license-url]
[![Lines of code][loc-shield]][loc-url]
[![Number of commits since v0.1][last-commit-shield]][last-commit-url]
[![Commit activity][commit-activity-shield]][commit-activity-url]
[![Docker size image][docker-size-shield]][docker-size-url]
[![Repository size][repo-size-shield]][repo-size-url]
[![Documentation web site][website-documentation-shield]][website-documentation-url]
[![web site][website-shield]][website-url]
[![CD pipeline][CD-CI-pipeline-shield]][CD-CI-pipeline-url]
[![Code Coverage][coverage-shield]][coverage-url]
[![Forks][forks-shield]][forks-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://iciq.cat">
    <img src="https://raw.githubusercontent.com/ytm-manager/ytm-manager.github.io/master/assets/images/logo.png" alt="Logo">
  </a>

<h6 align="center">presents</h3>

<img src="https://raw.githubusercontent.com/ytm-manager/ytm-manager.github.io/master/assets/images/product-screenshot.png" alt="Logo">
<!-- 
<h3 align="center">YouTube Music Manager</h3> -->

  <p align="center">
    The YouTube Music Manager (ytm-manager) application is a set of services to manage your YouTube Music Library.
    The application can be used via API REST, web platform or Telegram / WhatsApp bot.
    This application provides new ways to interact with the YouTube Music Service other than using the graphical 
    interface. 
    <br />
    <a href="https://ytm-manager.github.io/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://ytm-manager.com">View Demo</a>
    ·
    <a href="https://github.com/ytm-manager/ytm-manager-backend/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/ytm-manager/ytm-manager-backend/issues/new">Request Feature</a>
  </p>
</div>



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
        <li><a href="#try-the-platform">Try the platform</a></li>
        <li><a href="#deploy-and-run-the-software-locally">Deploy and run the software locally</a></li>
        <li><a href="#with-docker">Deploy and run the software locally with Docker</a></li>
        <li><a href="#manually">Deploy and run the software locally manually</a></li>
        <li><a href="#Learning-how-it-works">Learning how it works</a></li>
        <li><a href="#set-up-a-development-environment">Set up a development environment</a></li>
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

[![Product Name Screen Shot][product-screenshot]](https://ytm-manager.com)

The YouTube Music Manager (`ytm-manager`) is a suite of services that can be used to manage your YouTube Music personal 
library. These services provide another way to use the YouTube Music application and also expand its native 
functionality.

For example, *** YouTube Music Manager*** provides a functionality to download music from YouTube videos or playlists 
and upload them to YouTube Music, so you can lock your phone while listening to YouTube Music for free.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section lists any major frameworks/libraries used to bootstrap the **YouTube Music Manager** platform:

* [![Python][python-shield]][python-url]
* [![git][git-shield]][git-url]
* [![Flask][flask-shield]][flask-url]
* [![flask restx][flask-restx-shield]][flask-restx-url]
* [![Flasgger][flasgger-shield]][flasgger-url]
* [![yt-dlp][yt-dlp-shield]][yt-dlp-url]
* [![ytmusicapi][ytmusicapi-shield]][ytmusicapi-url]
* [![pipreqs][pipreqs-shield]][pipreqs-url]
* [![Docker][docker-shield]][docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

#### Try the platform
To get started, you will probably want to try the software from the official web page 
**[ytm-manager.com](http://ytm-manager.com)**.

YouTube Music Manager executes in the browser, so you do not need to install anything. 

Check the [user guide](https://ytm-manager.github.io/User-Guide/) from the 
[official documentation](https://ytm-manager.github.io/) to know more. 

#### Deploy and run the software locally
###### With Docker
The fastest way to get a copy up and running in your local machine is using *Docker* with `docker-compose`.

Assuming that you have `docker-compose` and `docker` installed on your machine, issue the 
following commands tu pull the [Docker image](https://hub.docker.com/r/ytm-manager/ytm-manager-backend) of the backend 
component and run it inside a container:
```shell
wget https://raw.githubusercontent.com/ytm-manager/ytm-manager-backend/master/docker-compose.yaml
sudo docker-compose up -d
```

Then, you can start sending requests to the API in the URL `http://localhost:5000`. You can check that the service is 
running by simply running a browser and opening the URL `http://localhost:5000/api/global/hello`, and the "Hello World"
message should be displayed. 

Check the [Docker installation guide](https://ytm-manager.github.io/Developer-Guide/Docker-installation/) from the
[official documentation](https://ytm-manager.github.io/) to know more.

###### Manually
If you want to run the software locally without using *Docker*, you may want to check [how to install ytm-manager into 
your machine](https://ytm-manager.github.io/Developer-Guide/Local-installation/). 

#### Learning how it works
If you want to understand how `ytm-manager` works we recommend that you read the 
[developer guide](https://ytm-manager.github.io/Developer-Guide/) from the
[official documentation](https://ytm-manager.github.io/).

#### Set up a development environment
If you want to make a contribution to the project or want to debug an error, you 
will need a functional development environment. This environment involves many tools and utilities [in addition 
to the ones needed to run the software manually](https://ytm-manager.github.io/Developer-Guide/Local-installation/).

You can follow [this guide](https://ytm-manager.github.io/Developer-Guide/Setting-up-development-environment/) 
from the [official documentation](https://ytm-manager.github.io/) to learn how to set up the development environment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<!-- Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos 
work well in this space. You may also link to more resources. -->

## Usage
Open a browser and navigate to the URL of **YouTube Music Manager** `http://localhost:5000/api/global/hello`. Check that 
the web page displays *Hello World!*. 

You can send requests to the different endpoints of the API using `curl`, Postman or any other applications or methods
to send requests. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
### TODO:
- [ ] Implement an end point that receives mp3 and upload to ytmusic.
- [ ] Implement an end point that receives a zip of .mp3 files to upload them to yt music.
- [ ] Change implementation of getting the current directory in APIController do it as in the upload service.
- [x] Add flexibility with the usage of the two different type of secrets.
- [ ] Read authentication for youtube music in each request instead of retrieving it from secrets.
- [x] Fix the docker network reachment. Port 5000 working without Docker.
- [ ] UploadPlaylist create a playlist in youtube music, download it an and add to the playlists in yt music playlists.

### TODO ?
- [ ] FRONTEND: Make API requests in Flutter
- [x] Show Text in App
- [x] TextBox Input (URL, FILE_PATH)
- [ ] Open File Button
- [ ] SendFile Button
- [ ] Refresh Session text box input widget

See the [open issues](https://github.com/ytm-manager/ytm-manager-backend/issues) for a full list of proposed features 
(and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing
This is an open-source project, so any contributions are **greatly appreciated** ❤. You can start by taking a look to 
the [`Developer guide`](https://ytm-manager.github.io/Developer-Guide/) to understand how **YouTube Music Manager** works.

If you have an issue or suggestion that would make **YouTube Music Manager** better, please 
[open a new issue](https://github.com/ytm-manager/ytm-manager-backend/issues/new) explaining your inquiry. We will try 
to satisfy your needs as soon as possible. 

If you want to make a contribution to **YouTube Music Manager** by yourself, please 
[open a new issue](https://github.com/ytm-manager/ytm-manager-backend/issues/new), so we can discuss the reach of your 
contribution. 
After that, [fork the repo](https://github.com/ytm-manager/ytm-manager-backend/fork), implement your change and create a 
[pull request](https://github.com/ytm-manager/ytm-manager-backend/compare) from your fork to the `develop` branch. 
We will merge your 
changes as soon as possible, so they are available in the next releases of **YouTube Music Manager**.

So, for each change that you want to do to **YouTube Music Manager** by yourself, you will need to:
1. [Fork the repo](https://github.com/ytm-manager/ytm-manager-backend/fork).
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Add and commit your Changes (`git add src; git commit -am 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Repeat steps 3 and 4 as many times as you need.
6. [Open a pull request from your fork to the develop branch](https://github.com/ytm-manager/ytm-manager-backend/compare).
7. Repeat steps 3 and 4 if further changes are required.

Do not forget to give the project a star ⭐ on GitHub!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License
![APGLv3 logo](https://www.gnu.org/graphics/gplv3-127x51.png "GNU AFFERO GENERAL PUBLIC LICENSE, Version 3")

Distributed under the [GNU GENERAL PUBLIC LICENSE, Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). 
See [`LICENSE`](https://github.com/ytm-manager/ytm-manager-backend/blob/master/LICENSE) to obtain a copy of the therms 
of this license.
See also [`LICENSE.md`](https://github.com/ytm-manager/ytm-manager-backend/blob/master/LICENSE.md) for more information 
about the licensing state of this project.

This software was developed by [Aleix Mariné-Tena](https://github.com/AleixMT).

**YouTube Music Manager (`ytm-manager`) ultimately belongs to [Aleix Mariné-Tena](https://github.com/AleixMT) and has 
total control over the licensing 
and distribution therms.**



>Copyright 2020-2023 [Aleix Mariné-Tena](https://github.com/AleixMT)

>This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later 
version.
> 
>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied 
> warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License v3 for more details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

>Main developer of ***YouTube Music Manager***: Aleix Mariné-Tena - [batangret@gmail.com](mailto:batangret@gmail.com) 📫

You can get more information of my work and research on my [GitHub profile](https://github.com/AleixMT).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
Thank Google for the development of YouTube and YouTube Music. Also, thank Google for allowing so much usage of 
its services and APIs for free.

The development of the ***YouTube Music Manager*** backend was possible thanks to the Python packages `ytmusicapi` and 
`yt-dlp`, packages that provide an easy way to use YouTube Music and YouTube programmatically through its API.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Credits

### People involved in the **YouTube Music Manager** development
* **Aleix Mariné-Tena**: Owner and main developer of ***YouTube Music Manager*** and its backend.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- Top page badges -->
[codacy-shield]: https://app.codacy.com/project/badge/Grade/8fb86f373fde43ebb38042da3f3b49a8
[codacy-url]: https://app.codacy.com/gh/ytm-manager/ytm-manager-backend/dashboard

[language-shield]: https://img.shields.io/github/languages/top/ytm-manager/ytm-manager-backend?color=yellow&logo=python
[language-url]: https://www.python.org/

[language-count-shield]: https://img.shields.io/github/languages/count/ytm-manager/ytm-manager-backend?color=red&logo=github
[language-count-url]: https://github.com/ytm-manager/ytm-manager-backend

[license-shield]: https://img.shields.io/github/license/ytm-manager/ytm-manager-backend?color=darkgreen&logo=gnu
[license-url]: https://github.com/ytm-manager/ytm-manager-backend/blob/master/LICENSE

[loc-shield]: https://img.shields.io/tokei/lines/github/ytm-manager/ytm-manager-backend
[loc-url]: https://github.com/ytm-manager/ytm-manager-backend

[last-commit-shield]: https://img.shields.io/github/last-commit/ytm-manager/ytm-manager-backend/master?logo=github
[last-commit-url]: https://github.com/ytm-manager/ytm-manager-backend/issues

[commit-activity-shield]: https://img.shields.io/github/commit-activity/y/ytm-manager/ytm-manager-backend?color=black&logo=github
[commit-activity-url]: https://github.com/ytm-manager/ytm-manager-backend/graphs/commit-activity

[docker-size-shield]: https://img.shields.io/docker/image-size/aleixmt/ytm-manager-backend/latest?color=purple&logo=docker
[docker-size-url]: https://hub.docker.com/r/aleixmt/ytm-manager-backend

[repo-size-shield]: https://img.shields.io/github/repo-size/ytm-manager/ytm-manager-backend?logo=github
[repo-size-url]: https://github.com/ytm-manager/ytm-manager-backend

[website-documentation-shield]: https://img.shields.io/website?url=https%3A%2F%2Fytm-manager.github.io%2F&logo=jekyll&label=Documentation%20website
[website-documentation-url]: https://ytm-manager.github.io/

[website-shield]: https://img.shields.io/website?url=https%3A%2F%2Fytm-manager.com&logo=icinga&label=ytm-manager%20website
[website-url]: https://ytm-manager.com

[CD-CI-pipeline-shield]: https://img.shields.io/github/actions/workflow/status/ytm-manager/ytm-manager-backend/build.yml?logo=docker&label=CD%20CI%20pipeline
[CD-CI-pipeline-url]: https://github.com/ytm-manager/ytm-manager-backend/actions/workflows/build.yml

[coverage-shield]: https://img.shields.io/codecov/c/github/ytm-manager/ytm-manager-backend/master?logo=codecov
[coverage-url]: https://app.codecov.io/gh/ytm-manager/ytm-manager-backend

[forks-shield]: https://img.shields.io/github/forks/ytm-manager/ytm-manager-backend.svg?label=Forks&maxAge=2592000&color=red
[forks-url]: https://github.com/ytm-manager/ytm-manager-backend/network/members



<!-- Static files and images -->
[product-screenshot]: https://github.com/ytm-manager/ytm-manager.github.io/blob/master/assets/images/product-screenshot.png



<!-- Shield technologies -->
[python-shield]: https://img.shields.io/badge/python-3.8.10-blue?style=for-the-badge&logo=python
[python-url]: https://www.python.org
[git-shield]: https://img.shields.io/badge/git-2.25.1-black?style=for-the-badge&logo=git
[git-url]: https://git.com
[flask-shield]: https://img.shields.io/badge/flask-2.3.3-purple?style=for-the-badge&logo=flask
[flask-url]: https://flask.palletsprojects.com/en/2.3.x/
[flask-restx-shield]: https://img.shields.io/badge/flask_restx-1.1.0-pink?style=for-the-badge&logo=flask
[flask-restx-url]: https://flask-restx.readthedocs.io/en/latest/
[flasgger-shield]: https://img.shields.io/badge/flasgger-0.9.7.1-green?style=for-the-badge&logo=swagger
[flasgger-url]: https://pypi.org/project/flasgger/
[yt-dlp-shield]: https://img.shields.io/badge/yt_dlp-2023.7.6-red?style=for-the-badge&logo=youtube
[yt-dlp-url]: https://github.com/yt-dlp/yt-dlp
[ytmusicapi-shield]: https://img.shields.io/badge/ytmusicapi-1.2.1-red?style=for-the-badge&logo=youtubemusic
[ytmusicapi-url]: https://ytmusicapi.readthedocs.io/en/stable/
[pipreqs-shield]: https://img.shields.io/badge/pipreqs-latest-brown?style=for-the-badge&logo=python
[pipreqs-url]: https://pypi.org/project/pipreqs/
[docker-shield]: https://img.shields.io/badge/docker-24.0.2_build_cb74dfc-grey?style=for-the-badge&logo=docker
[docker-url]: https://www.docker.com/


