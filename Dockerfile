FROM python:3.7

ADD requrements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# install asserts
ADD assets/ /opt/resource/
ADD test/ /opt/resource-tests/

RUN /opt/resource-tests/test.sh
