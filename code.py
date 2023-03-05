import pandas as pd
import matplotlib.pyplot as plt

#read the data from the csv file
df = pd.read_csv('Credit_card_transactions.csv')

#define function to create line plot to show average amount of transaction
def plot_line():
    #group data by card type and month and calculate average amount
    df_line = df.groupby(['Card Type', 'Month'], as_index=False)['Amount'].mean()
    #plot a line for each card type with amount
    card_types = df['Card Type'].unique()
    for card_type in card_types:
        plt.plot(df_line[df_line['Card Type'] == card_type]['Month'], df_line[df_line['Card Type'] == card_type]['Amount'], label=card_type)
    plt.xlabel('Month')
    plt.ylabel('Average Amount')
    plt.title('Average Amount by Card Type')
    plt.legend()
    plt.show()

#define function for pie chart to show data city wise
def plot_pie():
    #group data by city and calculate total amount
    df_pie = df.groupby('City', as_index=False)['Amount'].sum()
    #plot the pie chart with percentage and city names
    plt.pie(df_pie['Amount'], labels=df_pie['City'], autopct='%1.1f%%')
    plt.title('Total Amount by City')
   
    plt.show()

#define function for bar plot to show graph of expense type
def plot_bar():
    #group data by expense type and calculate total amount
    df_bar = df.groupby('Exp Type', as_index=False)['Amount'].sum()
    #plot the bar chart with short number format and exp type labels
    plt.bar(df_bar['Exp Type'], df_bar['Amount'], tick_label=df_bar['Exp Type'], width=0.6)
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 3))
    plt.xlabel('Exp Type')
    plt.ylabel('Total Amount')
    plt.title('Total Amount by Exp Type')
   
    plt.show()

plot_line()
plot_pie()
plot_bar()
