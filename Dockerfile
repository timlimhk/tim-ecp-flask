FROM python:3
ADD tests/ /tests
ADD TimEcpFlask/ /TimEcpFlask
WORKDIR /TimEcpFlask
RUN apt-get update
RUN pip install -r requirements.txt
CMD python app.py
