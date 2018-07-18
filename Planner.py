import tkinter as tk
import time
import Link

class App():
    
    def __init__(self, root):
        self.root = root
        months = ['Ιανουάριος','Φεβρουάριος','Μάρτιος','Απρίλιος','Μάιος','Ιουνίος',
              'Ιούλιος','Αύγουστος','Σεπτέμβριος','Οκτώβριος','Νοέμβριος','Δεκέμβριος']
        self.year = time.localtime()[0]

        #φτιάχνω λίστα με τους μήνες
        self.months = Link.Link(str)
        for i in range(12):
            self.months.add(months[i])
        self.months.setDefault(months[time.localtime()[1]-1])

        #φτιάχνω το frame για τους μήνες
        self.monthsFrame = tk.Frame(self.root)
        self.monthsFrame.pack(expand = False,side = 'top',anchor = 'n')
        self.month = tk.StringVar()
        self.month.set(self.months.getData() + ' ' + str(self.year))
        self.left = tk.Button(self.monthsFrame, text = '<', bg = 'lightgreen',
                              command = self.back)
        self.left.pack(fill = 'both',side = 'left')
        self.right = tk.Button(self.monthsFrame, text = '>', bg = 'lightgreen',
                              command = self.next)
        self.right.pack(fill = 'both',side = 'right')
        self.label = tk.Label(self.monthsFrame,textvariable = self.month,
                              font = 'Arial 10',width = 45, height = 2,
                              bg = 'lightblue')
        self.label.pack(fill = 'both',side = 'bottom')
        
        #φτιάχνω λίστα με τους αριθμούς των μηνών
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.numbers = Link.Link(int)
        for i in range(12):
            self.numbers.add(numbers[i])
        self.numbers.setDefault(time.localtime()[1])
        
        #φτιάχνω το frame για τον πίνακα
        self.tableFrame = tk.Frame(self.root)
        self.tableFrame.pack(expand = True,side = 'top',anchor = 'n')
        self.table = Table(self.tableFrame,self.numbers.getData(),self.year)

    def next(self):
        if self.months.getData() == 'Δεκέμβριος':
            self.year += 1
        self.months.setNext()
        self.month.set(self.months.getData() + ' ' + str(self.year))
        self.numbers.setNext()
        self.table.setNextMonth(self.numbers.getData(),self.year)

    def back(self):
        if self.months.getData() == 'Ιανουάριος':
            self.year -= 1
        self.months.setPrevious()
        self.month.set(self.months.getData() + ' ' + str(self.year))        
        self.numbers.setPrevious()
        self.table.setPreviousMonth(self.numbers.getData(),self.year)

class Table():
    def __init__(self, root, month, year):
        self.root = root
        self.month = month
        self.year = year
        self.daysList = ['Δε','Τρ','Τε','Πε','Πα','Σα','Κυ']
        
        #φτιάχνω λίστα με τους αριθμούς των ημερών
        self.numOfDays = self.getNumOfDays(self.month)
        self.numbers = Link.Link(int)
        for i in range(self.numOfDays):
            self.numbers.add(i+1)
        self.numbers.setDefault(time.localtime()[2])

        #φτιάχνω λίστα με τις μέρες
        self.days = Link.Link(str)
        for i in range(7):
            self.days.add(self.daysList[i])
        self.days.setDefault(self.daysList[time.localtime()[6]])

        #αρχικοποιώ ημέρα
        for i in range(time.localtime()[2]):
            self.days.setPrevious()
        self.firstDay = self.days.getData()

        #φτιάχνω τον πίνακα
        self.days.setDefault(self.firstDay)
        self.numbers.setDefault(1)
        self.table = self.makeTable()

    def setNextMonth(self, number, year):
        self.month = number
        self.year = year
        
        #βρίσκω τη γραμμή που έχει το 1
        row = 5
        for i in range(2):
            for j in range(7):
                if self.texts[5-i][j].get() == '1':
                    row = 5-i
        for i in range(7):
            self.texts[0][i].set(self.texts[row][i].get())

        #βάζω τον σωστό αριθμό ημερών ανά μήνα
        self.numOfDays = self.getNumOfDays(self.month)
        if self.numbers.getSize() == self.numOfDays - 1:
            self.numbers.add(31)
        if self.numbers.getSize() == self.numOfDays + 1:
            self.numbers.remove(31)
        if self.numbers.getSize() == self.numOfDays - 2:
            self.numbers.add(30)
            self.numbers.add(31)
        if self.numbers.getSize() == self.numOfDays + 2:
            self.numbers.remove(31)
            self.numbers.remove(30)
        if self.numbers.getSize() == self.numOfDays - 3:
            self.numbers.add(29)
            self.numbers.add(30)
            self.numbers.add(31)
        if self.numbers.getSize() == self.numOfDays + 3:
            self.numbers.remove(31)
            self.numbers.remove(30)
            self.numbers.remove(29)
        
        self.numbers.setDefault(int(self.texts[row][6].get()))
        self.numbers.setNext()

        for i in range(5):
            for j in range(7):
                self.texts[i+1][j].set(self.numbers.getData())
                self.numbers.setNext()

    def setPreviousMonth(self, number, year):
        self.month = number
        self.year = year

        #βρίσκω τη γραμμή που έχει το 1
        row = 1
        for i in range(2):
            for j in range(7):
                if self.texts[i][j].get() == '1':
                    if j == 0 and i == 1:
                        row = 0
                    else:
                        row = i

        for i in range(7):
            self.texts[5][i].set(self.texts[row][i].get())

        #βάζω τον σωστό αριθμό ημερών ανά μήνα
        self.numOfDays = self.getNumOfDays(self.month-1)
        if self.numbers.getSize() == self.numOfDays - 1:
            self.numbers.add(31)
        if self.numbers.getSize() == self.numOfDays + 1:
            self.numbers.remove(31)
        if self.numbers.getSize() == self.numOfDays - 2:
            self.numbers.add(30)
            self.numbers.add(31)
        if self.numbers.getSize() == self.numOfDays + 2:
            self.numbers.remove(31)
            self.numbers.remove(30)
        if self.numbers.getSize() == self.numOfDays - 3:
            self.numbers.add(29)
            self.numbers.add(30)
            self.numbers.add(31)
        if self.numbers.getSize() == self.numOfDays + 3:
            self.numbers.remove(31)
            self.numbers.remove(30)
            self.numbers.remove(29)

        pointer = int(self.texts[5][0].get())
        pointer -= 1
        self.numbers.setDefault(pointer)
        for i in range(5):
            for j in range(7):
                self.texts[4-i][6-j].set(self.numbers.getData())
                self.numbers.setPrevious()

    def makeDays(self):
        title = 4*' '
        for i in range(7):
            title += self.daysList[i] + 6*' '
        return tk.Label(self.frame,text = title,font = 'Arial 10',bg = 'lightgreen')

    def getNumOfDays(self, number):
        n = number
        if n == 0:
            n = 12
        m1 = [1,3,5,7,8,10,12]
        if n in m1:
                return 31
        elif n == 2:
            if self.isLeap(self.year):
                return 29
            else:
                return 28
        else:
            return 30

    def makeTable(self):
        self.frame = tk.Frame(self.root) #όλο το κάτω frame
        self.frame.pack(expand = True,fill = 'both')
        daysLabel = self.makeDays()
        daysLabel.pack(fill = 'both')
        self.texts = []
        self.buttons = []
        for i in range(6):
            row = []
            texts = []
            column = tk.Frame(self.frame) #το frame κάθε γραμμής
            column.pack(expand = False,fill = 'both')
            for j in range(7):
                text = tk.StringVar()
                text.set(2*' ')
                texts.append(text)
                button = tk.Button(column, textvariable = text,bg = 'lightblue')
                button.pack(expand = True,side = 'left',anchor = 'center')
                row.append(button)
            self.texts.append(texts)
            self.buttons.append(row)
        self.putNumbers()
        return self.frame

    def putNumbers(self):
        counter = 0
        write = False
        for i in range(6):
            for j in range(7):
                if i+j < 7 and not write:
                    if self.daysList[i+j] == self.firstDay:
                        write = True
                        counter = i+j
                else:
                    self.texts[i][j].set(self.numbers.getData())
                    self.numbers.setNext()

        #βάζω τα νούμερα πριν το 1 της πρώτης γραμμής
        counter = 30
        if self.numbers.getSize() == self.numOfDays + 1:
            counter = 31
        for i in range(7):
            if self.texts[0][6-i].get() == 2*' ':
                self.texts[0][6-i].set(counter)
                counter -= 1

    def isLeap(self, year):
        return year%400 == 0 or (year%4 == 0 and year%100 != 0)

root = tk.Tk()
root.title('Ημερολόγιο')
root.geometry('400x300+400+100')
root.resizable(width = False, height = False)
App(root)
root.mainloop()
