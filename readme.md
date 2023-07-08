<h1> Read the Below details to set up required things to run the code. </h1>

<h2>uvicorn app.main:app --reload</h2>

<p>where: uvicorn is ASGI server for python application</p>
<p>app.main:  the path where you have called the end point</p>
<p>app.main:app : the object returned by evoking FASTAPI()</p>
<p>--reload: auto-reload the server upon every file change</p>


<h2>To create python virtual env.</h2>
<p>"python3 -m venv venv"</p>

<h2>To activate python vitrual enviornment </h2>
<p>"source venv/bin/activate"</p>

<h2>To install fastapi and uvicorn<h2>
<p>"pip3 install fastapi uvicorn"</p>

<h2>to install sqlalchemy so that we can manage/ access sql database postgresql <h2>
<p>"pip3 install sqlalchemy"</p>

<h2>To install postgres library </h2>
<p>"pip3 install psycopg2-binary"</p>

<h2>To Create database</h2>
<p>Run command: "python3 create_db.py", This will create the table mentioned in models</p>