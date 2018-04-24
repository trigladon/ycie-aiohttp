Getting Started
---------------

1. Create docker image 
    ```
    docker build -t "ycie-aiohttp:latest" .
    ```
    
2. Run docker container 
    ```
    docker run --name ycie_aiohttp -d -v /mnt/python/ycie-aiohttp:/home/projects/ycie-aiohttp -p 8000:8000 -i ycie-aiohttp:latest
    ```

3. Connect to container
    ```
    docker exec -it ycie_aiohttp /bin/bash
    ``` 
     
4. Run project    
    ```    
    cd /home/projects/ycie-aiohttp && export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && adev runserver
    ```    