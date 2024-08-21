FROM python

ADD getUser.py /

CMD [ "python", "getUser.py" ]