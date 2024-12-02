FROM debian:stable-slim

RUN apt update
RUN apt install curl jq git pip jupyter protobuf-compiler -y
RUN pip3 install requests psycopg2-binary python-dotenv python-dateutil --break-system-packages
RUN pip3 install pandas numpy plotly yfinance protobuf --break-system-packages