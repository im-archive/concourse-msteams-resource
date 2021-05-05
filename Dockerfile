FROM python:3.8

ADD requirements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# install assets
ADD assets/ /opt/resource/
ADD test/ /opt/resource-tests/

RUN /opt/resource-tests/test.sh
