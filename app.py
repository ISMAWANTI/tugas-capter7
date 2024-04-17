# ini untuk membuat ip adress
from flask  import Flask, render_template,jsonify, request
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://ismawanti481:1234@ac-kqxaqgk-shard-00-00.o7l5fgd.mongodb.net:27017,ac-kqxaqgk-shard-00-01.o7l5fgd.mongodb.net:27017,ac-kqxaqgk-shard-00-02.o7l5fgd.mongodb.net:27017/?ssl=true&replicaSet=atlas-cx2us1-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# untuk ,enerima rrequest
@app.route('/diary', methods=['GET'])
def show_diary():
   # sample_receive = request.args.get('sample_give')
    # print(sample_receive)
    articles = list(db.diary.find({}, {'_id' : False}))
    return jsonify({'articles' : articles})
# berakhoir
# untuk menabah psot
@app.route('/diary', methods=['POST'])
def save_diary():
    # sample_receive = request.form.get('sample_give')
    # print(sample_receive)
    title_receive = request.form.get('title_give')
    content_receive = request.form.get('content_give')
    
    # buat file baru
    today = datetime.now()
    
    
    file = request.files['file_give']
    extension = file.filename.split('.')[-1]
    mytime = today.strftime('%Y-$m-%d-%H-%M-%S')
    filename = f'static/post-{mytime}.{extension}'
    file.save(filename)
    
    profile = request.files['profile_give']
    extension = profile.filename.split['.'][-1]
    profilename = f'static/profile-{mytime}.{extension}'
    profile.save(profilename)
    doc = {
        'file': filename,
        'profile' : profilename,
        'title' : title_receive,
        'content' : content_receive
    }
    db.diary.insert_one(doc)
    return jsonify({'msg' : 'data was saved'})
# berakhir
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
# berakhir ip adres
