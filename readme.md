<h2> Read the Below details to set up required things to run the code. </h2>

<p>uvicorn app.main:app --reload

where: uvicorn is ASGI server for python application
app.main:  the path where you have called the end point
app.main:app : the object returned by evoking FASTAPI()
--reload: auto-reload the server upon every file change</p>


<p>To create python virtual env. 
"python3 -m venv venv"</p>

<p>To activate python vitrual enviornment 
"source venv/bin/activate"</p>

<p>To install fastapi and uvicorn
"pip3 install fastapi uvicorn"</p>

<p>to install sqlalchemy so that we can manage/ access sql database postgresql
"pip3 install sqlalchemy"</p>

<p>To install postgres 
"pip3 install psycopg2-binary"</p>