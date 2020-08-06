#!/usr/bin/env python3

import scripts.emails
import os
from scripts import reports, emails

table_data=[
  ['Name', 'Amount', 'Value'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48],
  ['kiwi', 4, 0.49]
]
reports.generate("report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)

sender = "rahil.shaikh504@gmail.com"
receiver = "mohamedrshaikh@gmail.com"
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."

message = emails.generate(sender, receiver, subject, body, "report.pdf")
emails.send(message)

