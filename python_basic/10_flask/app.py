from flask import Flask,request,redirect,render_template
import sqlite3
import os

app = Flask(__name__)
path = os.path.dirname(__file__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputform', methods=['GET','POST'])
def inputform():
    if request.method == 'GET':
        return render_template('inputform.html')
    else:
        #db에 데이터 입력
        conn = sqlite3.connect(path + '/customer.db')
        cur = conn.cursor()
        cur.execute('''create table if not exists customer
                       (name text,
                        email text,
                        tel text,
                        address text,
                        gender text)''')
        conn.commit()
        data=[request.form['name'],request.form['email'],request.form['tel'],request.form['address'],request.form['gender']]
        cur.execute('insert into customer values(?,?,?,?,?)',data)
        conn.commit()
        conn.close()
        return redirect('/')

@app.route('/customerlist')
def customerlist():
    conn = sqlite3.connect(path + '/customer.db')
    cur = conn.cursor()
    cur.execute('select * from customer order by name')
    data = cur.fetchall()
    print(data)
    return render_template('customerlist.html',data=data)

if __name__ == '__main__':
    app.run(debug=True,port=80)