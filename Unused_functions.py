
#can name a csv file regardless if the csv is in the name or not designed to be in the initial line of a class
def __init__(self,filename,date,location):
        self.name = filename
        if '.csv' not in self.name:
            self.namecsv = self.name + '.csv'
        if '.csv' in self.name:
            self.namecsv = self.name
            self.name = self.name.replace('.csv', '')
        self.path = location + filename
#allows you to run cmd commands off of a class 
def cmd(self,command):
        p = subprocess.run([command], text=True, shell=True, stdout=subprocess.PIPE)
        print(p.returncode)
        print(p.stdout)
