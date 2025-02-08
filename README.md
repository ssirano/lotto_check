로또 당첨자 안내문 생성기

소개

이 프로젝트는 PySimpleGUI를 활용하여 로또 당첨자 안내문을 자동으로 생성하는 프로그램입니다. 
사용자가 회차 및 각 등수별 당첨자 수를 입력하면, HTML 문서를 생성하여 브라우저에서 확인하고 출력할 수 있습니다.

기능

PySimpleGUI 기반의 간단한 GUI 제공
회차 및 각 등수별 당첨자 수 입력 가능
HTML 기반의 안내문 자동 생성
브라우저에서 HTML 파일 자동 열기
인쇄 최적화된 HTML 디자인 적용

사용 방법
1. 설치
이 프로젝트는 Python 3이 필요하며, 실행 전에 아래 패키지를 설치해야 합니다.
pip install PySimpleGUI
2. 실행 방법
아래 명령어를 실행하여 프로그램을 실행할 수 있습니다.
python lotto_winner_generator.py
3. 사용 방법
프로그램을 실행하면 GUI 창이 나타납니다.
회차 번호 및 각 등수별 당첨자 수를 입력합니다.
생성 버튼을 클릭하면 안내문이 생성됩니다.
생성된 HTML 파일이 브라우저에서 자동으로 열립니다.
필요하면 브라우저에서 인쇄할 수 있습니다.

파일 설명
lotto_winner_generator.py: 메인 실행 파일
lotto_winners.html: 생성된 HTML 안내문 파일 (프로그램 실행 후 생성됨)

기술 스택
Python 3
PySimpleGUI
HTML & CSS
Webbrowser 모듈
