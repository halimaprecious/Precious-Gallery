## PROJECT NAME 
**PRECIOUS~GALLERY**


## AUTHOR 
*PRECIOUS HALIMA*


## DESCRIPTION 

This is a photo gallery web Application where you can view different photos and see the details of each photo.You can also search a photo by category.


## Features


As a user of the application you will be able to:


1. View different photos that interest you.
2. Click on a single photo to expand it and also view the details of the photo. The photo details will appear on a modal within the same route as the main page.
3. Search for different categories of photos. (ie. Travel, Food)
4. Click on share icon to share the image with any of your social account or alternatively Copy a link to the photo and share with your friends.
5. View photos based on the location they were taken or category.


### Installation and setup instructions

1. Clone this repo: git clone https://github.com/halimaprecious/Precious-Gallery.git
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database gallery using the command below.


       CREATE DATABASE gallery;
5. Migrate the database using the command below


       python3 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## Running the tests

Use the command given below to run automated tests.

        python manage.py test gallery




## TECHNOLOGIES USED 

* [Django](https://www.djangoproject.com/) - web framework used
* Javascript - For DOM(Document Object Manipulation) scripts
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## CONTACTS
halimaprecious3@gmail.com

## LIVE LINK
Find the deployed app:
[here](https://preciousgallery.herokuapp.com/)
 

## LICENSE 


[MIT](https://choosealicense.com/licenses/mit/)


Copyright (c) 2022 Precious Halima

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
