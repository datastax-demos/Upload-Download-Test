from flask import Flask, render_template, request
import base64, io
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
app = Flask(__name__)
app.config.from_pyfile('app.config')

session = None

@app.route('/')
def index():
    return render_template("index.jinja2")

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['file']
    id = request.form.get("upload_id")
    encoded_string = base64.b64encode(file.stream.read())

    insert_image = session.prepare("""INSERT INTO cvs_poc.image (upload_id, image) VALUES (?,?)""")

    session.execute(insert_image.bind({"upload_id": int(id), "image": encoded_string}))

    return render_template("index.jinja2")

@app.route('/download')
def download():
    id = request.args.get("image_id")
    if id is '':
        return "Row Doesnt Exist"
    get_image = session.prepare("""SELECT * FROM cvs_poc.image WHERE upload_id=?""")
    image = session.execute(get_image.bind({"upload_id":int(id)}))
    if len(image.current_rows) > 0:
        return image.current_rows[0]["image"]
    else:
        return "Row Doesnt Exist"
def init_cassandra():
    global session
    print("Connecting to Cassandra")
    cluster = Cluster(app.config['DSE_CLUSTER'].split(','))
    session = cluster.connect("cvs_poc")
    session.row_factory = dict_factory
    print("Connected to Cassandra")

if __name__ == '__main__':
    init_cassandra()
    app.run(host='0.0.0.0')

