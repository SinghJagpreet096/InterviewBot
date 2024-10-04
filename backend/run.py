from services import data_process
from services import prediction
import click
import sys

if sys.argv[1] == "data_process":
    data_process.main()
elif sys.argv[1] == "prediction":   
    prediction.main()