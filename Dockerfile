FROM python:3.7-alpine

RUN pip install requests colorama

# copy resources
COPY assets/ /opt/resource/

# make files executable
RUN chmod +x /opt/resource/in
RUN chmod +x /opt/resource/out
RUN chmod +x /opt/resource/lib/out.py
RUN chmod +x /opt/resource/check