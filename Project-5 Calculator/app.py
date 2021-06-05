from tkinter import *

root = Tk()
root.title('Calculator')
root.resizable(0 , 0)

def is_operator(ch) :
    if ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '%' :
        return True
    return False

class Calculator :

    display_str = StringVar()
    operator_str = StringVar()
    oper_eq = ''
    display_eq = ''
    actual_eq = ''

    def __init__(self) :
        
        self.title = Label(root , text = 'Calculator' , font=('consolas' , 24))
        self.display_screen = Entry(root , bg = '#f1f2f6' ,bd=0, font=('consolas' , 36) , textvariable=Calculator.display_str, justify='right', width=11)
        self.operator_screen = Entry(root , fg = 'grey',bg = '#f1f2f6' ,bd=0, textvariable=Calculator.operator_str,font=('consolas' , 24) ,justify='right', width=16)
        # buttons
        self.numbers = {
            num : Button(
                root ,
                text = num ,
                width = 5 , 
                height = 2 ,
                font = ('consolas' , 18),
                relief='ridge',
                bg = 'white',
                command = lambda i = num: self.btn_click(str(i))
            ) for num in range(0,10)
        }
        self.operators = {
            operator : Button(
                root ,
                text = operator ,
                width = 5 , 
                height = 2 ,
                font = ('consolas' , 18),
                bg = '#bdc3c7',
                relief='ridge' ,
                command = lambda i = operator: self.btn_click(i)
            ) for operator in ['+' , '-' , '*' , '/' , '%' , '.']
        }
        self.extras = {
            key : Button(
                root ,
                text = key ,
                width = 5 , 
                height = 2 ,
                font = ('consolas' , 18),
                bg = '#bdc3c7',
                relief='ridge' ,
                command = lambda i = key: self.clear_or_backspace(i)
            ) for key in ['C' , '<']
        }
        self.equal = {'=' : Button(
            root , 
            text = '=' ,
            width = 5,
            height = 5 ,
            font = ('consolas' , 18) ,
            relief='ridge',
            bg='orange',
            command = lambda : self.equal_to()
        )}
        self.initialize_screen()
        self.place_widgets()
        root.mainloop()

    def place_widgets(self) :
        
        self.title.grid(row=0 , column=0 , columnspan=4 , padx=10 , pady=10)
        self.operator_screen.grid(row=1 , column=0 , columnspan=4 , padx=10 , pady=10)
        self.display_screen.grid(row=2 , column=0 , columnspan=4 , padx=10 , pady=10)
        self.extras['C'].grid(row=3 ,column=0 , padx=2,pady=2)
        self.operators['/'].grid(row=3 ,column=1 , padx=2,pady=2)
        self.operators['*'].grid(row=3 ,column=2 , padx=2,pady=2)
        self.extras['<'].grid(row=3 , column=3 , padx=2 , pady=2)
        self.numbers[7].grid(row=4 , column=0 , padx=2 , pady=2)
        self.numbers[8].grid(row=4 , column=1 , padx=2 ,pady=2)
        self.numbers[9].grid(row=4 , column=2 , padx=2 , pady=2)
        self.operators['+'].grid(row=4 , column=3 , padx=2 , pady=2)
        self.numbers[4].grid(row=5 , column=0 , padx=2 , pady=2)
        self.numbers[5].grid(row=5 , column=1 , padx=2 ,pady=2)
        self.numbers[6].grid(row=5 , column=2 , padx=2 , pady=2)
        self.operators['-'].grid(row=5 , column=3 , padx=2 , pady=2)
        self.numbers[1].grid(row=6 , column=0 , padx=2 , pady=2)
        self.numbers[2].grid(row=6 , column=1 , padx=2 ,pady=2)
        self.numbers[3].grid(row=6 , column=2 , padx=2 , pady=2)
        self.equal['='].grid(row=6 , column=3 ,rowspan = 2,padx=2 , pady=2)
        self.operators['%'].grid(row=7 , column=0 , padx=2 , pady=2)
        self.numbers[0].grid(row=7 , column=1 , padx=2 , pady=2)
        self.operators['.'].grid(row=7 , column=2,padx=2 , pady=2)

    def initialize_screen(self) :
        Calculator.display_str.set('0')

    def btn_click(self , ch) : 
        if is_operator(ch) :
            Calculator.actual_eq += ch
            Calculator.oper_eq = ch
            Calculator.display_eq = ''

        else :
            Calculator.display_eq += ch
            Calculator.actual_eq += ch

        Calculator.operator_str.set(Calculator.oper_eq)
        Calculator.display_str.set(Calculator.display_eq)

    def clear_or_backspace(self , ch) :
        if ch == 'C' :
            Calculator.actual_eq += ''
            Calculator.oper_eq = ''
            Calculator.display_eq = ''
            Calculator.display_str.set('0')
            
        elif ch == '<' :
            Calculator.oper_eq = ''
            Calculator.display_eq = Calculator.display_eq[:-1]
            if Calculator.display_eq == '' :
                Calculator.display_eq = '0'
            else :
                Calculator.actual_eq = Calculator.actual_eq[:-1]
            Calculator.display_str.set(Calculator.display_eq)
            Calculator.operator_str.set(Calculator.oper_eq)
    
    def equal_to(self) :
        
        total = eval(Calculator.actual_eq)
        Calculator.display_eq = str(total)
        Calculator.actual_eq = str(total)
        Calculator.oper_eq = 'Ans.'
        Calculator.operator_str.set(Calculator.oper_eq)
        Calculator.display_str.set(Calculator.display_eq)

if __name__ == '__main__' :
    
    app = Calculator()
    