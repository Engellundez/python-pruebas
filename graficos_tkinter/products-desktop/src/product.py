from tkinter import ttk
from tkinter import *
import sqlite3


class Product():
    db_name = 'src/database.db'

    def __init__(self, window) -> None:
        self.wind = window
        self.wind.title('Products Application')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text="Register a new Product")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Name Input
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

        # Price Input
        Label(frame, text='Price: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        # Button Add Product
        ttk.Button(frame, text='Save Product', command=self.add_product).grid(
            row=3, columnspan=2, sticky='ew')
        
        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3,column=0, columnspan=2, sticky='we')

        # Table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor='center')
        self.tree.heading('#1', text='Price', anchor='center')

        # Buttons
        ttk.Button(text='DELETE', command=self.delete_product).grid(row=5,column=0, sticky='we')
        ttk.Button(text='EDIT', command=self.edit_product).grid(row=5,column=1, sticky='we')

        # Filling te Row
        self.get_products()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()

        return result

    def get_products(self):
        # get_children get all elements in the table.
        records = self.tree.get_children()
        # cleaning table
        for element in records:
            self.tree.delete(element)

        # querying data
        query = 'SELECT * FROM products ORDER BY name DESC'
        db_rows = self.run_query(query)

        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

    def valitadion(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if not self.valitadion():
            self.message['text'] = 'Name and price are REQUIRED'
            return None
        
        query = 'INSERT INTO products (name, price) VALUES(?,?)'
        parameters = (self.name.get(), self.price.get())
        self.run_query(query, parameters)
        self.message['text'] = f'Product {self.name.get()} added Successfully'
        
        self.name.delete(0,'end')
        self.price.delete(0,'end')
        
        
        self.get_products()

    def get_item_selected_in_table(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
            return self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return None
            
    def delete_product(self):
        name = self.get_item_selected_in_table()
        if not name:
            return
        
        query = 'DELETE FROM products WHERE name = ?'
        self.run_query(query, (name,))
        self.message['text'] = f'Record {name} deleted Successfully'
        self.get_products()
    
    def edit_product(self):
        old_name = self.get_item_selected_in_table()
        if not old_name:
            return
        
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = f'Edit product "{old_name}"'
        
        # Old Name
        Label(self.edit_wind, text='Old Name: ').grid(row=0,column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,value=old_name), state='readonly').grid(row=0,column=2)
        
        # New Name
        Label(self.edit_wind, text='New Name: ').grid(row=1,column=1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row=1,column=2)
        
        # Old Price
        Label(self.edit_wind, text='Old Price: ').grid(row=2,column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind,value=old_price), state='readonly').grid(row=2,column=2)
        
        # New Price
        Label(self.edit_wind, text='New Price: ').grid(row=3,column=1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row=3,column=2)
        
        # save button
        Button(self.edit_wind, text='Update', command=lambda: self.edit_records(new_name.get(), old_name, new_price.get(), old_price)).grid(row=4,column=2,sticky='we')
    
    def edit_records(self, new_name, old_name, new_price, old_price):
        query = 'UPDATE products SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_price, old_name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = f'Record {old_name} updated successfully'
        self.get_products()
        