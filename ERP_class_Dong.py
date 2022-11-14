from functools import partial       # For function buttons
from tkcalendar import Calendar     # For calendar usage
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
import datetime
# import MyFun
# MyFun.font_import()

# Still working on...
# https://pythonguides.com/python-tkinter-treeview/
# https://www.tutorialspoint.com/delete-and-edit-items-in-tkinter-treeview
# https://www.youtube.com/watch?v=n5gItcGgIkk
# http://tkdocs.com/shipman/ttk-Treeview.html
item = (' ', ' iPhone 13 Pro', ' iPhone 13 Pro Max', ' iPhone 13 mini'
                        , ' iPhone SE(3)', ' iPhone 12 Pro', ' iPhone 12 Pro Max'
                        , ' iPhone 12 mini', ' iPhone 12', ' iPhone 11 Pro'
                        , ' iPhone 11 Pro Max', ' iPhone 11', ' iPhone SE(2)')

customer = (' ', ' Andy', 'Sam', 'Tom', ' Sue', ' Sandy')


class ERP(object):
    def __init__(self, items, customers):
        # Window initialize

        self.win = tk.Tk()
        self.w_min = 1024
        self.w_max = 1024
        self.h_min = 768
        self.h_max = 768
        self.win_ini()

        # Menu bar initialize
        self.filemenu = None
        self.helpmenu = None
        self.othermenu = None
        self.menubar = tk.Menu(self.win)
        self.menubar_ini()
        self.win.config(menu=self.menubar)  # Add menubar in window

        # Create a notebook as a frame's group
        self.notebook = ttk.Notebook(self.win)
        self.notebook_ini()

        # Create Tab: frame_1
        self.frame_1 = ttk.Frame(self.notebook)
        self.tab_ini()

        #### Frame 1 ####
        ## Comboboxes: Item, Customer ####
        self.itembox_list = items
        self.customerbox_list = customers
        self.boxes_list = None
        self.boxes_contents = None
        self.box_y_list = None
        self.boxVar_list = None
        self.boxVar = None
        self.box = None
        self.combox_ini()

        ## Entries: ID, Order-Date, Quantity, Unit-Price ##
        self.entry_list = None
        self.entry_y_list = None
        self.entryVar_list = None
        self.entryStr = None
        self.entry = None
        self.entry_ini()

        ## Calendar: Order-Date ##
        self.calendar_button = None
        self.top = None
        self.cal = None
        self.calendar_ini()

        ## Labels: All ##
        self.label_list = None
        self.labels = None
        self.label = None
        # Label: Total-Price #
        self.totalPriceStr = None
        self.totalPrice = None
        self.label_ini()

        ## Tree ##
        # Tree's column name #
        self.treeColumn = None

        # Scrollbar #
        self.scrollbar_x = None
        self.scrollbar_y = None
        self.tree_ini()

        ## All StingVar ##
        self.var_list = None
        self.var_all()

        ## Buttton: Create, Update, Delete ##
        self.fun_button_list = None
        self.fun_buttons = None
        self.fun_button = None
        self.button_ini()

        #### Function: ####
        ## Select ##
        # Bind event and function
        # Recommend to use lambda here. Using partial causes error.
        self.tree.bind('<<TreeviewSelect>>', lambda event: self.tree_funs('Select'))
        self.tree.bind("<Double-1>", self.double_click)
        self.win.mainloop()

    def win_ini(self):
        ######## Window settings ########
        self.win.wm_title("ERP by Jhong,Dong You")
        self.win.resizable(width=True, height=True)

        self.win.minsize(width=self.w_min, height=self.h_min)  # 最小尺寸
        self.win.maxsize(width=self.w_max, height=self.h_max)  # 最大尺寸
        self.win.configure(bg='#ececec')

    def menubar_fun(self):
        # Can add action after selecting menubar
        print("menubar_fun")

    def menubar_ini(self):
        ######## Menubar ########
        # Window menu which is nearby the window title
        # For masOS user, it's at the top of the screen

        self.filemenu = tk.Menu(self.menubar, tearoff=False)
        self.helpmenu = self.filemenu
        self.othermenu = self.filemenu

        # First section in menubar
        self.filemenu.add_command(label="Open", command=partial(self.menubar_fun,'open'))
        self.filemenu.add_command(label="Save", command=partial(self.menubar_fun,'save'))
        self.menubar.add_cascade(label="File", menu=self.filemenu, underline=0)

        # Second section in menubar
        self.helpmenu.add_command(label="Find", command=partial(self.menubar_fun,'find'))
        self.helpmenu.add_command(label="About", command=partial(self.menubar_fun,'about'))
        self.menubar.add_cascade(label="Help", menu=self.helpmenu, underline=0)

        # Third section in menubar
        self.othermenu.add_command(label="Exit", command=self.win.destroy)  # Close window
        self.menubar.add_cascade(label='Other', menu=self.othermenu, underline=0)

    def notebook_ini(self):
        ######## Notebook ########
        self.notebook.pack(expand=1, fill="both")

    def tab_ini(self):
        ######## Tabs ########
        self.notebook.add(self.frame_1, text='Frame 1')

    def combox_ini(self):
        self.boxes_list = [' Item', ' Customer']
        self.boxes_contents = [self.itembox_list, self.customerbox_list]
        self.box_y_list = [2, 3]
        self.boxVar_list = []
        for boxtext, content, box_y in zip(self.boxes_list, self.boxes_contents, self.box_y_list):
            # Establish comboboxes of items
            self.boxVar = tk.StringVar()
            self.box = ttk.Combobox(self.frame_1, width=15, textvariable=self.boxVar)
            # boxvar.set(boxtext)  # Initialize text in box
            # Content of box
            self.box['value'] = content  # Set box contents
            self.box.grid(row=box_y, column=1, sticky='w', pady=5)
            self.boxVar_list.append(self.boxVar)

    def entry_ini(self):
        self.entry_list = ['ID', 'Order-Date', 'Quantity', 'Unit-Price']
        self.entry_y_list = [0, 1, 4, 5]
        self.entryVar_list = []
        for entrytext, entry_y in zip(self.entry_list, self.entry_y_list):
            self.entryStr = tk.StringVar()
            self.entry = ttk.Entry(self.frame_1, width=15, textvariable=self.entryStr)
            # entryStr.set(entrytext)  # Initialize text in entry
            self.entry.grid(row=entry_y, column=1, sticky='w', pady=5)
            self.entryVar_list.append(self.entryStr)

    def calendar_ini(self):
        #### Calendar: Order-Date ####
        self.calendar_button = ttk.Button(self.frame_1, text='Calendar', command=self.calendar_button_create)
        self.calendar_button.grid(row=1, column=2, sticky='we', pady=5)

    def calendar_button_create(self):
        self.top = tk.Toplevel(self.frame_1)
        today = datetime.date.today()
        mindate = datetime.date(year=2018, month=1, day=21)
        maxdate = today + datetime.timedelta(weeks=100)
        # Range from mindate to maxdate
        # print(mindate, maxdate)
        self.cal = Calendar(self.top, font="Arial 14", selectmode='day', locale='en_US',
                       mindate=mindate, maxdate=maxdate, disabledforeground='red',
                       cursor="hand1", year=2022, month=8, day=14)
        self.cal.pack(fill="both", expand=True)
        ttk.Button(self.top, text="ok", command=self.calendar_set).pack()

    def calendar_set(self):
        self.entryVar_list[1].set(self.cal.selection_get())
        # cal.see(datetime.date(year=2016, month=2, day=5))

    def label_ini(self):
        self.label_list = ['ID', 'Order-Date', 'Item', 'Customer', 'Quantity'
            , 'Unit-Price', 'Total-Price']
        self.labels = []
        for key, txt in enumerate(self.label_list):
            self.label = ttk.Label(self.frame_1, text=txt)
            if txt == 'Total-Price':
                self.label.grid(row=0 + 1 * key, column=0, sticky='w', pady=10)
            else:
                self.label.grid(row=0 + 1 * key, column=0, sticky='w', pady=5)
            self.labels.append(self.label)
        self.label_total_price()

    def label_total_price(self):
        ## Label: Total-Price ##
        self.totalPriceStr = tk.StringVar()
        self.totalPrice = ttk.Label(self.frame_1, textvariable=self.totalPriceStr)
        self.totalPriceStr.set('0')  # Initialize text in label
        self.totalPrice.grid(row=6, column=1, sticky='w', pady=10)  # padx == 0

    def tree_ini(self):
        #### Tree ####
        self.treeColumn = self.label_list  # Same as label
        self.tree = ttk.Treeview(self.frame_1, columns=self.treeColumn, show='headings')  # Set column text
        self.tree.grid(row=9, column=0, columnspan=10, sticky='nsew')

        ## Tree's column name ##
        for i in self.treeColumn:
            self.tree.heading(i, text=i)  # Text of tree's column
            self.tree.column(i, minwidth=0, width=80, anchor='w')  # Width of tree's column

        ## Scrollbar ##
        self.scrollbar_x = ttk.Scrollbar(self.frame_1, orient='horizontal', command=self.tree.xview)
        self.scrollbar_y = ttk.Scrollbar(self.frame_1, orient='vertical', command=self.tree.yview)
        self.scrollbar_x.grid(row=10, columnspan=10, sticky='ew')
        self.scrollbar_y.grid(row=9, column=10, sticky='ns')
        self.tree.configure(xscrollcommand=self.scrollbar_x.set)
        self.tree.configure(yscrollcommand=self.scrollbar_y.set)

    def var_all(self):
        #### All StingVar ####
        self.var_list = [self.entryVar_list[0], self.entryVar_list[1], self.boxVar_list[0]
            , self.boxVar_list[1], self.entryVar_list[2], self.entryVar_list[3], self.totalPriceStr]

    def button_ini(self):
        ## Buttton: Create, Update, Delete ##
        self.fun_button_list = ['Create', 'Update', 'Delete']
        self.fun_buttons = []
        for key, txt in enumerate(self.fun_button_list):
            self.fun_button = ttk.Button(self.frame_1, text=txt, command=partial(self.tree_funs, txt))
            self.fun_button.grid(row=12, column=7 + key, sticky='ew')
            self.fun_buttons.append(self.fun_button)

    def tree_funs(self, command):
        self.command = command
        if self.command == 'Create':
            self.create_tree()
        elif self.command == 'Update':
            self.update_tree()
        elif self.command == 'Delete':
            self.delete_tree()
        elif self.command == 'Select':
            self.select_tree()
        else:
            print('error command!')
            return

    def create_tree(self):
        print('create')
        # Run if createButton pressed
        self.tree_row = []
        for col_get in self.var_list:  # Get variables from entry and box
            self.tree_row.append(col_get.get())  # Become a row for tree
        self.tree.insert('', 'end', values=self.tree_row)  # Insert the row to tree

    def delete_tree(self):
        print('delete')

    def update_tree(self):
        print('update')

    def select_tree(self):
        for selected_item in self.tree.selection():
            self.row = self.tree.item(selected_item)      # Get the selected row
            self.cols = self.row['values']
            for var, col in zip(self.var_list, self.cols):        # Get variables from the row of tree
                var.set(col)

    def double_click(self, event):
        print('Double click!')
        self.region_click = self.tree.identify_region(event.x, event.y)
        print(self.region_click)


if __name__ == "__main__":
    app = ERP(item, customer)
