FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./food_info.py .
COPY ./food_db.sql .
CMD [ "python", "./food_info.py" ]
