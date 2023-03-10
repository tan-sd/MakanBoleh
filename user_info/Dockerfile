FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY invokes.py ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./user_info.py .
CMD [ "python", "./invokes.py" , "./user_info.py" ]
