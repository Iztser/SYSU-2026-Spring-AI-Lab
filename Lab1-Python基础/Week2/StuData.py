class StuData:
    def __init__(self,filename):
        self.data = []
        try:
            with open(filename,"r",encoding = "utf-8") as f:
                for lines in f:
                    line = lines.split(' ')
                    self.AddData(line[0],line[1],line[2],int(line[3]))
        except FileNotFoundError:
            print("错误：找不到文件")
    def AddData(self,name,id,sex,age):
        singleInfo = [name,id,sex,age]
        self.data.append(singleInfo)
    def printData(self):
        for info in self.data:
            print(info)
    
    def SortData(self,cond):
        map = {"name":0,"id":1,"sex":2,"age":3}
        index = map[cond]
        self.data.sort(key = lambda x:x[index])
    def ExportFile(self,new_filename):
        with open(new_filename,"w",encoding = 'utf-8') as f:
            for info in self.data:
                line = info[0] + ' ' + info[1] + ' ' + info[2] + ' ' + str(info[3])
                f.write(line + '\n')



filename = input("请输入文件名：")
myData = StuData(filename)
myData.AddData("Eric","249","M",19)
myData.AddData("小李","250","M",20)
cond = input("请输入排序条件：")
myData.SortData(cond)
myData.printData()
new_filename = input("请输入新文件名：")
myData.ExportFile(new_filename)