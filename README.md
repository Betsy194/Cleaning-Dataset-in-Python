# Cleaning-Dataset-in-Python
df = pd.read_excel('sales_2017.xlsx')
df

#Change the name of columns
df.rename({'Order': 'Order ID', 'Customer': 'Customer ID', 'Sales': 'Sales Person', 
           'Order.1':'Order date','Ship':'Ship date', 'Order.2':'Order Priority',
          'Order.3': 'Order Quantity', 'Unit Sell':'Unit SellPrice', 'Discount': 'Discount Percent',
          'Shipping': 'Shipping Amount', 'Ship Mode':'Ship Mode Container'},
          axis='columns', inplace=True)
df.head()

#delete the first row
df = df.drop(df.index[[0]])

df.loc [1, 'Order date']

# To convert Date to Datetime
df['Order date'] = pd.to_datetime(df['Order date'])

# To convert Date to Datetime
df['Ship date'] = pd.to_datetime(df['Ship date'])

df.info()

#Convert str to float
df['Order Quantity'] = df['Order Quantity'].astype(float)
df['Unit SellPrice'] = df['Unit SellPrice'].astype(float)
df['Discount Percent'] = df['Discount Percent'].astype(float)
df['Shipping Amount'] = df['Shipping Amount'].astype(float)

df.info()

# convert Order date column to day
df['Order date'].dt.day_name()
