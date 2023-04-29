import os

class Student():
    def __init__(self):
        self.id = None  #id号
        self.name = None #名字
        self.scores = {'英语':None,'语文':None,'数学':None}  #使用一个字典来存储成绩


class StudentList():
    def __init__(self,filename):
        self.filename = filename
        self.data = []  #用列表形式存储所有的数据
        if not os.path.exists(self.filename):  #如果路径不存在，那么创建文件
            open(self.filename,'w')
        with open(self.filename,'r') as file:
            for item in file.readlines():  #将所有的信息存储到列表中
                self.data.append(dict(eval(item)))


    #保存功能
    def save(self):   #将self.data中的信息更新到txt文件中
        with open(self.filename,'w') as file:
            for item in self.data:
                file.writelines(str(item) + '\n')


    #用户提供ID，返回ID对应的信息
    def find_id(self,id):
        if not self.is_id_exist(id):
            print("该ID不存在！")
            return none
        for item in self.data:
            if not item['id'] == id:
                continue
            else:
                return item

    #检查id是否存在
    def is_id_exist(self,id):
        for item in self.data:
            if id == item['id']:
                return True


    #1.插入新的学生信息
    def insert(self):
        student = Student()
        while True:
            student.id = input("请输入学生的ID：")
            if self.is_id_exist(student.id):
                print("ID号已存在，请重新输入！")
                continue
            if student.id.strip() == ' ':  #strip删除字符串前后的空格
                print("学生ID不可为空")
                continue
            while True:
                student.name = input("请输入学生姓名:")
                if student.name.strip() == ' ':
                    print("学生姓名不可为空")
                else:
                    break
            for subject in student.scores.keys():  #keys能够获得字典的键列表
                while True:
                    try:
                        score = float(input(f'请输入学生的{subject}成绩：'))
                        if not 0 <= score <= 100:
                            raise ValueError
                        student.scores[subject] = score
                        break
                    except ValueError:
                        print('学生成绩必须是0-100之间的数字，请重新选择输入！')
            self.data.append({'id':student.id,'name':student.name,'scores':student.scores})
            self.save()
            print("成功录入学生信息！")
            break


    #2.查询学生信息功能
    def search(self):
        query = input("请输入想要搜索的ID或姓名:")
        if len(self.data) != 0:
            print(f"{'ID':<10}{'姓名':<8}{'英语':<8}{'语文':<8}{'数学':<8}")  #<代表靠左堆积，后面的数字代表字符串宽度
            for item in self.data:
                if query == item['id'] or query == item['name']:
                    print(f"{item['id']:<10}{item['name']:<10}{item['scores']['英语']:<10}{item['scores']['语文']:<10}{item['scores']['数学']:<10}")

    #3.删除学生信息
    def delete(self):
        while True:
            id = input("请输入想要删除的学生ID：")
            item = self.find_id(id)
            if item != None:
                self.data.remove(item)  #remove删除
                print(f"已成功删除ID为{id}学生")
                self.save()
                return


    #4.修改学生信息
    def modify(self):
        while True:
            id = input("请输入想要修改的学生ID：")
            item = self.find_id(id)
            self.data.remove(item)
            for subject in item['scores'].keys():
                while True:
                    try:
                        score = float(input(f'请修改学生的{subject}成绩：'))
                        if not 0 <= score <= 100:
                            raise ValueError
                        item['scores'][subject] = score
                        break
                    except ValueError:
                        print('学生成绩必须是0-100之间的数字，请重新输入！')
            self.data.append(item)
            self.save()
            print(f'已成功修改ID为{id}的学生成绩')
            break
        

    #5.排序功能
    def sort(self):  #对学生成绩排序，可选英语，数学，语文这三种学科进行降序排序
        while True:
            choice = input("请选择想要排序的科目：")
            if choice in ['英语','数学','语文']:
                self.data.sort(key = lambda x:float(x['scores'][choice]),reverse = True)
                self.show_lst()
            break

    #6.统计功能，统计总人数
    def total(self):
        print(f"总共有{len(self.data)}名同学的信息")

        
    #7.显示所有的学生信息
    def show_lst(self):
        if len(self.data) != 0:
            print(f"{'ID':<10}{'姓名':<8}{'英语':<8}{'语文':<8}{'数学':<8}")
            for item in self.data:
                print(f"{item['id']:<10}{item['name']:<10}{item['scores']['英语']:<10}{item['scores']['语文']:<10}{item['scores']['数学']:<10}")
        else:
            print("无数据显示")
        
                        

#窗口的显示界面制作
def menu():
    print("*******************************信息管理系统******************")
    print('\t1.录入信息\t\t2.查找信息')
    print('\t3.删除信息\t\t4.修改信息')
    print('\t5.排序\t\t\t6.统计总人数')
    print('\t7.显示所有信息\t8.退出系统')
    print('*****************************************************************')

#主函数
def main():
    student_list = StudentList("student.txt")
    menu()
    while True:
        functions = {'1':student_list.insert,'2':student_list.search,'3':student_list.delete,'4':student_list.modify,'5':student_list.sort,'6':student_list.total,'7':student_list.show_lst}
        choice = input("请输入功能（输入数字1-8）：")
        if choice in functions:
            functions[choice]()  #通过字典调用相应的函数
            menu()
        elif choice == '8':
            answer = input("确认退出系统吗（输入Y或N）：")
            if answer == 'y' or answer == 'Y':
                print('～～～～～～～～～感谢使用～～～～～～～') 
                break
            else:
                continue
        else:
            print("输入错误，请重新输入。")
    
        
if __name__ == "__main__":
    main()
