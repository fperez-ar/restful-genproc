Instructions:
  * make virtual env: python3 -m venv dev
  * activate virtual env: source dev/bin/activate
  * install requirements: pip3 install requirements.txt
  * run: python3 home.py

In docker:
 Need to expose port 5000 when running,
 `docker build -t restful-genproc .`
 `docker run -p 5000:5000 --rm restful-genproc`
 for interactive:`docker run restful-genproc -it -p 5000:5000 /bin/bash`
