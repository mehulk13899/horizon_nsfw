#  Installation:

1. Ensure the python3 version is 3.8.12. To check, run python3 -V. If you do not have it, you can install it here

2. Setup a virtual environment in the project folder using python3: $ python3 -m venv venv

3. Start the virtual environment. You should see (venv) in as part of the command prompt once it is started: $ source venv/bin/activate 
NOTE: To stop the virtual environment at any time, run (venv) $ deactivate

4. Install all the requirements, including flask. Be sure not to use sudo as this will install flask in the global environment instead of the virtual environment: (venv) $ pip3 install -r requirements.txt

5. Start server ==> uvicorn main:app --host 0.0.0.0 --port 8000

# free txt
pip3 freeze > requirements.txt

# install multiple env
https://levelup.gitconnected.com/install-multiple-python-versions-on-mac-a58b1966825f

# import error of opennsfw2
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y


# Test Dataset 

video==> https://nsfw.xxx/
image==> https://github.com/EBazarov/nsfw_data_source_urls

# Used Modules
==> https://github.com/bhky/opennsfw2


https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/


# build docker without cache
#!/bin/bash
docker build --no-cache . -t nsfw_backend3.8:latest