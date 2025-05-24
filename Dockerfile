FROM python:3.12

RUN mkdir /app
COPY pyproject.toml /app
COPY uv.lock /app
WORKDIR /app

RUN pip install uv

RUN uv sync

COPY . /app

# Expose the Jupyter port
EXPOSE 8888

# Set up Jupyter with a predefined password
RUN echo '#!/bin/bash\nuv run jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token="" --NotebookApp.password=""' > /app/start-jupyter.sh
RUN chmod +x /app/start-jupyter.sh

ENTRYPOINT [ "/app/start-jupyter.sh" ]