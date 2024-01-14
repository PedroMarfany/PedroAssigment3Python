"""
Script to filter info of the dataset
"""

import pandas as pd 
import click 
class Film:
    def _init_(self, title, year, tickets_sold):
        self.title = title
        self.year = year
        self.tickets_sold = tickets_sold
        
    def calculate_profit(self, ticket_price):   #funcion para calcular el profit a partir de los datos proporcionados
        try:
            gross_profit = self.tickets_sold * ticket_price
            return gross_profit
        except Exception as e:
            print(f"Error calculating profit for {self.title}: {e}")    #con este except aseguramos que si hay errores no se den precios erroneos y simplemente no de datos
            return None

@click.command()
@click.option('--title', prompt='Enter film title', help='The title of the film')
@click.option('--year', prompt='Enter release year', type=int, help='The release year of the film')
@click.option('--tickets_sold', prompt='Enter tickets sold', type=int, help='Number of tickets sold for the film')
@click.option('--ticket_price', prompt='Enter ticket price', type=float, help='Price of each movie ticket')

def main(title, year, tickets_sold, ticket_price)


if _name_ == '_main_':               
    main()