Blog for creating Posts by user and add comments to each post
Authentication using django simple-jwt

Create python env using python -m venv
Clone Git Reopsitory https://github.com/manojv200/webcastle_blog.git 
Activate env and install requirements.txt using pip install -r requirments.txt

After that,execute command python3 manage.py migrate

Then run the server using python3 manage.py runserver

Api endpoints:

Get Access and Refresh Token(simplejwt): http://127.0.0.1:8000/api/token/,  body :username and password
Create Post : http://127.0.0.1:8000/api/posts/ using POST body : title and description 
Get all Posts : http://127.0.0.1:8000/api/posts/ using GET
Get each Post : http://127.0.0.1:8000/api/posts/id_of_post/ using GET
Delete Post : http://127.0.0.1:8000/api/posts/id_of_post/  using DELETE
Add a comment : http://127.0.0.1:8000/api/posts/id_of_post/comments/ using POST body :content
Get all comments in a post : http://127.0.0.1:8000/api/posts/id_of_post/comments/ using GET

add Authorization and Content-Type in Headers for all Api end points

 
