FROM python:3.10-alpine
WORKDIR /script
COPY main.py main.py
ENTRYPOINT [ "python3", "-u", "main.py" ]
CMD ["--cycles", "4"]