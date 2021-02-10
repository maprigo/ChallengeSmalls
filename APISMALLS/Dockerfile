FROM python:3.7

COPY gPRC_smalls/protos/gen-py/ protos/gen-py/ 
COPY gPRC_smalls/orders/client_wrapper.py /app/client_wrapper.py 
# We copy just the requirements.txt first to leverage Docker cache
COPY APISMALLS/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY APISMALLS/. /app



CMD PYTHONPATH=/:/protos/gen-py python3 app.py
