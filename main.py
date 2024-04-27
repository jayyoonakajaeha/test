from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# 설문조사 데이터를 저장할 파일 경로
SURVEY_DATA_FILE = 'survey_data.csv'

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # 폼에서 제출된 데이터 가져오기
        name = request.form['name']
        email = request.form['email']
        when = request.form['when']

        # 데이터를 CSV 파일에 저장
        with open(SURVEY_DATA_FILE, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, email, when])

        # 감사 메시지 표시 페이지로 리디렉션
        return redirect(url_for('thanks'))

    # 설문조사 폼 렌더링
    return render_template('survey.html')

@app.route('/thanks')
def thanks():
    # 감사 메시지 페이지 렌더링
    return render_template('thanks.html')

if __name__ == '__main__':
    #app.run('127.0.0.1', 5000, debug=True)
    app.run(host='0.0.0.0',port=5000,debug=True)
