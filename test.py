import PySimpleGUI as sg
import webbrowser
import os
from datetime import datetime

def create_html(draw_number, date_str, winners):
    html_content = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4 landscape;
            margin: 0;
        }
        body {
            margin: 0;
            padding: 0;
            background: #fff;
            font-family: 'Nanum Myeongjo', serif;
        }
        .page {
            width: 297mm;
            height: 210mm;
            padding: 20mm;
            margin: 10mm auto;
            background: #fff;
            box-sizing: border-box;
            page-break-after: always;
            border: 1px solid #ddd;
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .border-decoration {
            position: absolute;
            top: 10mm;
            left: 10mm;
            right: 10mm;
            bottom: 10mm;
            border: 2px solid #gold;
            pointer-events: none;
        }
        .content {
            text-align: center;
            position: relative;
            z-index: 1;
            width: 100%;
        }
        .draw-number {
            font-size: 36px;
            color: #333;
            margin-bottom: 30px;
        }
        .winner-type {
            font-size: 72px;
            color: #c4302b;
            margin: 20px 0;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .winner-count {
            font-size: 120px;
            color: #1a1a1a;
            margin: 30px 0;
            font-weight: bold;
        }
        .store-info {
            position: absolute;
            bottom: 20mm;
            width: 100%;
            text-align: center;
            font-size: 24px;
            color: #333;
        }
        .date {
            position: absolute;
            top: 20mm;
            right: 30mm;
            font-size: 20px;
            color: #666;
        }
        .background-text {
            position: absolute;
            font-size: 200px;
            color: rgba(0,0,0,0.03);
            z-index: 0;
            transform: rotate(-45deg);
        }
        @media print {
            body {
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
            .page {
                margin: 0;
                border: none;
            }
        }
    </style>
</head>
<body>
'''
    
    # 각 등수별 페이지 생성
    for rank, count in winners.items():
        if count > 0:  # 당첨자가 있는 경우만 페이지 생성
            html_content += f'''
    <div class="page">
        <div class="border-decoration"></div>
        <div class="date">{date_str}</div>
        <div class="background-text">LOTTO</div>
        <div class="content">
            <div class="draw-number">제 {draw_number} 회</div>
            <div class="winner-type">{rank}등 당첨</div>
            <div class="winner-count">{count} 명</div>
        </div>
        <div class="store-info">
            <p>주원복권방</p>
            <p>TEL: ______________</p>
        </div>
    </div>
'''
    
    html_content += '</body></html>'
    
    # HTML 파일 저장
    with open('lotto_winners.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 브라우저에서 열기
    abs_path = os.path.abspath('lotto_winners.html')
    webbrowser.open('file://' + abs_path)

def main():
    sg.theme('LightGrey1')

    layout = [
        [sg.Text('로또 당첨자 안내문 생성기', font=('Helvetica', 20), justification='center')],
        [sg.Text('회차:', size=(15,1)), sg.Input(key='-DRAW-', size=(20,1))],
        [sg.Text('1등 당첨자 수:', size=(15,1)), sg.Input(key='-FIRST-', size=(20,1), default_text='0')],
        [sg.Text('2등 당첨자 수:', size=(15,1)), sg.Input(key='-SECOND-', size=(20,1), default_text='0')],
        [sg.Text('3등 당첨자 수:', size=(15,1)), sg.Input(key='-THIRD-', size=(20,1), default_text='0')],
        [sg.Button('생성', size=(10,1)), sg.Button('닫기', size=(10,1))]
    ]

    window = sg.Window('로또 당첨자 안내문 생성기', layout, element_justification='center')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == '닫기':
            break

        if event == '생성':
            try:
                draw_number = values['-DRAW-']
                winners = {
                    '1': int(values['-FIRST-']),
                    '2': int(values['-SECOND-']),
                    '3': int(values['-THIRD-'])
                }
                
                # 현재 날짜
                date_str = datetime.now().strftime('%Y년 %m월 %d일 추첨')
                
                # HTML 생성 및 열기
                create_html(draw_number, date_str, winners)
                
                sg.popup('안내문이 생성되었습니다.\n브라우저에서 확인 후 인쇄해주세요.')
                
            except ValueError:
                sg.popup_error('입력값을 확인해주세요.\n회차와 당첨자 수는 숫자로 입력해야 합니다.')

    window.close()

if __name__ == '__main__':
    main()