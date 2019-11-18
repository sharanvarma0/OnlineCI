from flask import *
import os
app = Flask(__name__)


@app.route('/')
def editPython():
        return render_template('template.html',prog='',remarks='',output='')


@app.route('/result', methods=['POST','GET'])
def compute():
    if request.method == 'POST':
        result = request.form['prog'] 
        open("code.py",'w').write(result)
        os.system('python3 code.py 1> output.file 2> remarks.file')
        remark = open('remarks.file','r').read()
        outputs = open('output.file','r').read()
        os.system('rm code.py')
        return render_template('template.html',prog=result,remarks=remark,output=outputs)
    
if __name__ == '__main__':
    app.run(debug = False)
