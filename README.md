:satisfied:

# Flask-Pitch

## Description

- This is a python-Flask application that has been created to enable users to create and post pitches.A User can be able to create an account and their information will be saved into the databse of the website. The User is able to create a post whereby they will be able to update and delete posts at free will.A users is also able to Upvote and Downvote blog posts according to his preferences.

## Project Screenshot

- This is the Project Screenshot of the Home page
![Flask-Blog-App](flaskblog/static/pics/Screenshot.png)

## Live-Link
 - You can view the project on your browser using this livelink. `https://simkim.herokuapp.com/`
 
## BDD


1.  On loading the website the user can see the homepage that has quotes that have been posted by others.
2.  The User needs to Create an account to be able to post anything.

- input: The user credentials are required for account Creation.
- output: Once correct user credentials are added and they are successful user is redirected to the login page.
  A user needs unique username and password for account creation to be successful.If not account will not be created.

3. The user logs into the website.
   - input: The account details used to create the account.
   - Output: User is redirected to the home page with new navigation bar that allows him to add posts.
4. The User can now create a post
   - input:The User clicks on the new post link and adds his new post.
   - output: The new post is displayed on the home page.
5. User can update post.
   - Input: User clicks on the quote and he has created.
   - Output: A redirection to a page that allows them to update the post and submit.
6. User can delete Post
   - Input:User clicks on the quote that he has created.
   - Output: The delete button appears that allows one to delete posts created.
7. Random quotes are displayed on the home page on each reload or refreshing of the website.
8. A user has the ability to upvote and downvote a blog.
    - Press on the green Thumps up updates the vote count.
    - Pressing on the downvote adds count to the dislikes.

## Set Up Instructions

- Open your terminal and move to a directory where you would like to store the project eg. cd Documents
- Use the command `git clone` to clone the aplication at `https://github.com/SkimaniKings/flask-blog`.
- After cloning navigate to the project.
- Run `pip install` to install all the dependencies
- Now run the project using your terminal with the command `python3.6 app.py`

## Technologies Used

- PYTHON
- PIP
- FLASK FRAMEWORK
- BOOTSTRAP
- CSS
- POSTGRESS

## Licence

The MIT License (MIT)
Copyright (c) 2020 Simon Kimani.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

@SkimaniKings

## Contact Details

- You can reach me through:
  0713813919
  kimanisimon856@gmail.com

## Author

**Simon Kimani**
