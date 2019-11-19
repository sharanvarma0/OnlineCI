from flask import *
import os
app = Flask(__name__)

@app.route('/')
def editPython():
        return render_template('template.html',prog='',input='',remarks='',output='')

@app.route('/result', methods=['POST','GET'])
def compute():
    if request.method == 'POST':
        result = request.form
        result_dict = dict(result.items())
        open("code.py",'w').write(result_dict['prog'])
        open("input.file",'w').write(result_dict['input'])
        os.system('python code.py < input.file 1> output.file 2> remarks.file')
        remark = open('remarks.file','r').read()
        outputs = open('output.file','r').read()
        os.system('rm code.py *.file')
        return render_template('template.html',prog=result_dict['prog'],input=result_dict['input'],remarks=remark,output=outputs)

if __name__ == '__main__':
    app.run(debug = False)
