
FROM python:3.7
ADD protos/gen-py /protos/gen-py
ADD orders/server /server

# Add the client code strictly for development
# purposes
COPY ./requirements.txt /server/requirements.txt
WORKDIR /server
RUN pip install -r requirements.txt
EXPOSE 50051
CMD PYTHONPATH=/:/protos/gen-py python3 server.py