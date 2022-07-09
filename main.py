from flask import Flask, render_template

# 웹 서버 역할 Flask APP 생성
app = Flask(__name__)

# 라우팅 설정 - url을 통한 접속 > 응답을 담당
@app.route('/')
def index():
    return '<h1>안녕하세요</h1>'

@app.route('/page')
def page():
    return '<h1>상세페이지</h1>'

# Flask 앱 가동(run)
if __name__ == "__main__":
    app.run()