// Copyright (c) 2022, Gift and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["PAYE Report"] = {
	"filters": [
		{
			fieldname: 'from_date',
			label: 'From Date',
			fieldtype: 'Date',
			reqd: 1,
			default: "2022-01-01"
		},
		{
			fieldname: 'to_date',
			label: 'To Date',
			fieldtype: 'Date',
			reqd: 1,
			default:frappe.datetime.get_today()
		},
		{
			fieldname: 'currency',
			label: 'Currency',
			fieldtype: 'Data',
			reqd: 1,
			default: 'NGN'
		},
		{
			fieldname: 'employee',
			label: 'Employee',
			fieldtype: 'Link',
			options: "Employee",
			reqd: 0	
		},
		{
			fieldname: 'company',
			label: 'Company',
			fieldtype: 'Link',
			options: "Company",
			reqd: 1
		},
		{
			fieldname: 'status',
			label: 'Status',
			fieldtype: 'Data',
			default: "Submitted"
		}

	]
};
