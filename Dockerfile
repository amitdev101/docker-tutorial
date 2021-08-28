FROM python:3.8

ADD main.py .

RUN pip install pyautogui shellit

CMD ["python", "./main.py"]

