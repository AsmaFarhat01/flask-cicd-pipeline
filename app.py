from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Automated Deployement Pipeline</h1>
    <p> Hello Devops!</p>
    <p>This Flask app is deployed using docker and Github Actions CI/CD!</p>
    <p>Built By Asma Farhat Shaik</p>
    '''
@app.route('/health')
def health():
    return {'status': 'healthy'}, 200
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True)
