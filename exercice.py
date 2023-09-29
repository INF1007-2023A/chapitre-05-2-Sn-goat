#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	taxes = 0
	sous_total = 0
	for list_achat in data:
		quantity = list_achat[1]
		price = list_achat[2]
		mini_total = quantity * price
		sous_total += mini_total
		taxes += (0.15 * mini_total)
	total = sous_total + taxes 
	facture = f"{name}\nSOUS TOTALL    {format(sous_total, '.2f')}$\nTAXES           {format(taxes,'.2f')}$\nTOTAL          {format(total,'.2f')}$"
	
	return facture


def format_number(number, num_decimal_digits):
	str_number = str(number)
	for str_number in  range(3):
		print(str_number)
	
	return ""

def get_triangle(num_rows):
	triangle = ""
	for i in range(num_rows):
		w = "+" + " "*((num_rows - 1) - i) + "A"*(1 + 2*i) + " "*((num_rows - 1) - i) + "+" + "\n"
		triangle += str(w)
			
	middle = "+" + "+" * ((2*num_rows)-1) + "+"
	a = f"{middle}\n{triangle}{middle}"
	return a


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
