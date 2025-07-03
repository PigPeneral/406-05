FROM jupyter/base-notebook:latest

RUN pip install pandas numpy matplotlib seaborn scikit-learn

WORKDIR /home/jovyan/work

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.allow_root=True", "--NotebookApp.ip='0.0.0.0'"]

EXPOSE 8888