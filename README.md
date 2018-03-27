Getting Started
---------------

1. Create docker image 
    ```
    docker build -t credit:latest .
    ```
    
2. Run docker container 
    ```
    docker run -d -v /mnt/python/credit-fair-e:/home/projects/credit-fair-e -p 8080:8080 -i -t f550bf267128
    ```
    
3. Run project
    ```
    python3.6 /home/projects/credit-fair-e/app.py
    ```    