Getting Started
---------------

1. Create docker image 
    ```
    docker build -t ycie-aiohttp:latest .
    ```
    
2. Run docker container 
    ```
    docker run -d -v /mnt/python/ycie-aiohttp:/home/projects/ycie-aiohttp -p 8080:8080 -i -t f550bf267128
    ```
    
3. Run project
    ```
    python3.6 /home/projects/ycie-aiohttp/app.py
    ```    