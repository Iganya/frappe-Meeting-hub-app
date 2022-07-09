# Copyright (c) 2022, Gift and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	if filters.from_date and filters.to_date:
		if filters.from_date > filters.to_date:
			frappe.throw("From date cannot be Greater than To Date")
	#Getting Columns of the report
	columns = [
		{
			'fieldname': 'employee', 
			'label': 'Employee', 
			'fieldtype': 'Data',
			'width': 200
		},
		{
			'fieldname': 'employee_name', 
			'label': 'Employee Name', 
			'fieldtype': 'Data'
		},
		{
			'fieldname': 'date_of_joining', 
			'label': 'Date Of Joining', 
			'fieldtype': 'Date'
		},
		{
			'fieldname': 'company', 
			'label': 'Company', 
			'fieldtype': 'Data'
		},
		{
			'fieldname': 'start_date', 
			'label': 'Start Date', 
			'fieldtype': 'Date'
		},
		{
			'fieldname': 'end_date', 
			'label': 'End Date', 
			'fieldtype': 'Date'
		},
		{
			'fieldname': 'tax_pin', 
			'label': 'Tax Pin', 
			'fieldtype': 'Data'
		}
	]
	#Using mysql to get data from multiple tables.
	data = frappe.db.sql("""
			SELECT t1.employee, 
			t1.employee_name, 
			t1.date_of_joining, 
			t1.designation, 
			t1.company, 
			t2.start_date, 
			t2.end_date 
			FROM `tabEmployee`AS t1 
			JOIN `tabSalary Slip` AS t2""", as_dict=1)
	#Setting filters on Employee 
	if filters.get("employee"):
		data = [dic for dic in data if dic["employee"] == filters.get("employee")]

	return columns, data
