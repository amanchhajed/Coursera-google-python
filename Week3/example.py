#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails


def load_data(filename):
  with open(filename, encoding="utf-8") as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  max_sale_year = 0
  max_year = None
  yearly_sales = {}
  for item in data:
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales = item
    year = item["car"]["car_year"]
    yearly_sales[year] = yearly_sales.get(year, 0) + item["total_sales"]
    if yearly_sales[year] > max_sale_year:
      max_year = year
      max_sale_year = yearly_sales[year]

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(max_sales["car"]["car_model"], max_sales["total_sales"]),
    "The most popular year was {} with {} sales".format(max_year, max_sale_year)
  ]

  return summary


def cars_dict_to_table(car_data):
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  new_summary = '\n'.join(summary)
  reports.generate('/tmp/cars.pdf', "Cars report", new_summary, cars_dict_to_table(data))
  msg = emails.generate("automation@example.com", "student-03-f19e840934ed@example.com",
                                   "Sales summary for last month", new_summary, "/tmp/cars.pdf")
  email.send(msg)

if __name__ == "__main__":
  main(sys.argv)