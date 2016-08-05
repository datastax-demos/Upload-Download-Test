# Requirements:

1. Python 3.5
2. Pip
3. Flask
4. Cassandra_driver

```
apt-get install python-dev
apt-get install python-pip
pip install flask
pip install cassandra_driver
```

# Schema

```
cqlsh -f cql/upload-download-test.cql
```

# Configuration

Modify app.config to match your cluster ip
```
DSE_CLUSTER = '127.0.0.1'
```

# Start the application

Foreground:
```
python Upload-Download-Test.py
```
Background:
```
nohup python Upload-Download-Test.py &
```