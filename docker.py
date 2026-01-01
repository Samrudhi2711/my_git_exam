Q. Create a website using container (httpd) accessible on

http://localhost:9300


Step 1: Install Docker (if not already installed)

Check Docker installation:

docker --version


If not installed, install Docker and start the service.


  
Step 2: Create a project directory
mkdir my_website
cd my_website



Step 3: Create an HTML file

Create a file named index.html:

nano index.html


Add the following content 👇
(Replace PRN with your actual PRN number)

<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Name: Samrudhi Gadge</h1>
    <h2>PRN: YOUR_PRN_NUMBER</h2>
</body>
</html>


Save and exit.


Step 4: Run httpd container

Run Apache (httpd) container and map port 9300 → port 80:

docker run -dit \
-p 9300:80 \
-v $(pwd)/index.html:/usr/local/apache2/htdocs/index.html \
--name my_httpd \
httpd

Explanation:

-p 9300:80 → maps container port 80 to localhost port 9300

-v → mounts your HTML file into container

httpd → Apache web server image



Step 5: Verify the container is running

docker ps



You should see my_httpd running.

Step 6: Access the website

Open browser and go to:

👉 http://localhost:9300



✅ Output will show:

Name: Samrudhi Gadge
PRN: YOUR_PRN_NUMBER

(Optional) Stop the container
docker stop my_httpd
