import os 
import csv 
from datetime import datetime


class Username:

    def __init__(self,folder,filname):
        self.path=os.path.join(folder,filname)
        if not os.path.exists(folder):
            os.mkdir(folder)


    def get_status(self,name,weight):
        aysor =datetime.now().strftime("%d %h %m")
        with open(self.path,mode="a",newline="")as wf:
            writer =csv.writer(wf)
            writer.writerow([aysor,name,weight])


    def get_info(self):
        if not os.path.exists(self.path):
            return 0
        count =0
        with open(self.path,mode="r",newline="")as rf:
            reader =csv.reader(rf)
        for row in reader:
            if len(row[2])<2:
                weight =float(row[2])
                count+=weight

        return count



        