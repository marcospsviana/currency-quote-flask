## flask

*create virtual environment*
```
python -m venv .venv
```
*activate virtual environment*
```
source .venv/bin/activate
```
*install dependency management pip-tools*
```
pip install pip-tools
```
*create requirements for pip-compile*
```
touch requirements.in
touch requirements-dev.in
```
*add dependencys*
```
flask
python-decouple
requests
flask-cors 
```
 *editing requirements-dev.in*
 ```
 -r requirements.in
 pytest
 blak
 ```

 ## Heroku apps

 *create heroku app backend*
 ```
 heroku apps:create currency-backend-flask

 ```

 

