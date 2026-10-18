# Educational image only: NOT a FIS OPF image.
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PORT=8080 PYTHONDONTWRITEBYTECODE=1
WORKDIR /opt/lab
COPY mock_app.py /opt/lab/mock_app.py
RUN chgrp -R 0 /opt/lab && chmod -R g=u /opt/lab
EXPOSE 8080
USER 1001
ENTRYPOINT ["python3","-B","/opt/lab/mock_app.py"]
