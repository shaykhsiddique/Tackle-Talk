
   Tackle Talk
==========
	
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://shaykhsiddique.github.io)

Tackle Talk is an extension of NFL+ that grants subscribers access to highlighted recaps of the most talked about players, through the prediction of AI, Stemming from social media comments.
![flowchart](https://github.com/shaykhsiddique/PVAMU_BoB/assets/18369069/6c66844d-2971-43ea-9e0f-10993c00b358)


Description
--------------
*Requirements and Dependencies*
- Python3

*Python Dependencies*
- Flask - Web Framework
- Pandas - Used for data manipulation and analysis 
- Re - Regular Expressions
- Spacy - Machine Learning pre-trained models
- Levenshtein - Used for mathematical formulation

*Project Deployment*
Run the bash commands.
``` bash
pip install flask
pip install pandas
pip install spacy
pip install Levenshtein
```
Install all dependencies.

Run the application by using the following command from the root of the project.
``` bash
python3 app.py
```

The Flask server will run on **localhost:5001**.

If you need to change the server IP or Port, it will be found on the Project Root, `app.py` **last line**.

``` python
	app.run(host='0.0.0.0', debug=True, port=5001)
```

Change the port number from here.



https://github.com/shaykhsiddique/Tackle-Talk/assets/18369069/0817814c-88fb-4d1d-b73d-5abe224bf2a0


Datasets
--------------
Datasets are collected from social media.
<img width="954" alt="Screen Shot 2024-03-08 at 4 24 15 AM" src="https://github.com/shaykhsiddique/PVAMU_BoB/assets/18369069/293d78c5-780f-4da3-8a21-df8c47ed25c5">
Processed dataset-
<img width="1014" alt="Screen Shot 2024-03-08 at 4 26 34 AM" src="https://github.com/shaykhsiddique/PVAMU_BoB/assets/18369069/76c99c7c-448a-40ac-a07d-11a86b2f5b3f">


Use this to access [Figma Model](https://www.figma.com/file/OMJfmUIqWiwuz0BWr4BRHa/BOTB_V1_03%2F07%2F24?type=design&node-id=21%3A691&mode=design&t=p0xhXGhmAfpL7lWX-1)

Screenshots
--------------

Login to Tackle Talk
![FireShot Capture 002 - Tackle Talk - 172 25 32 85](https://github.com/shaykhsiddique/PVAMU_BoB/assets/18369069/4b6cbc14-a6e3-4e2f-9222-fd4e1d0e01a1)

Home Page

![FireShot Capture 003 - Tackle Talk - 172 25 32 85](https://github.com/shaykhsiddique/PVAMU_BoB/assets/18369069/d4d1ea8a-1b24-46ed-af57-48ee51fe17c1)

Players spotlight contents

![FireShot Capture 005 - Tackle Talk - 172 25 32 85](https://github.com/shaykhsiddique/PVAMU_BoB/assets/18369069/a1c751f5-eac5-4d2e-988a-6bb4dd9ee2f4)


**Common Problems while deploying**
```
Address already in use
Port 5001 is in use by another program. Either identify and stop that program, or start the server with a different port.
```
**Fix:** Just use a different port while deploying. How to change the port is discussed on the **Project Deployment** section above.

For any questions related to the application, please feel free to contact.
Email: shaykhsiddiqee@gmail.com

