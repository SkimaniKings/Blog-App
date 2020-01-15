:satisfied:

# Flask-Pitch

## Description

- This is a python-Flask application that has been created to enable users to create and post pitches.A User can be able to create an account and their information will be saved into the databse of the website. The User is able to create a post whereby they will be able to update and delete posts at free will.

## Project Screenshot

- This is the Project Screenshot of the Home page

## BDD 
 1. On loading the website the user can see the homepage that has quotes that have been posted by others.
 2. The User needs to Create an account to be able to post anything.
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
    