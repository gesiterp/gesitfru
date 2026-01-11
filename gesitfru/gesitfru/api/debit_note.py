import frappe
from frappe.utils.data import money_in_words

@frappe.whitelist()
def get_money_in_words(number):
    text = money_in_words(number)
    # hapus kata 'only' pada akhir kalimat
    return text.replace(" only", "").replace(" saja", "")
