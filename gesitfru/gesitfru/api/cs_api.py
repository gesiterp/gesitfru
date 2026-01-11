import frappe
import frappe.utils
@frappe.whitelist()
def create_cs_from_dn(dn_name):
    dn = frappe.get_doc("DEBIT NOTE", dn_name)
    cs = frappe.new_doc("CS")
    cs.closing_date = frappe.utils.nowdate()
    cs.cust_group = dn.customer
    cs.type_of_cover = dn.cob
    cs.no_dn = dn.nota_no
    cs.install = dn.installement
    cs.period_from = dn.periode
    cs.period_to = dn.period_to
    cs.status = "Draft"
    cs.gross_premium = dn.premium
    cs.policy_cost = dn.policy_cost
    cs.discount = dn.discount
    cs.nett_premium = dn.total_due_to_us
    cs.insert()
    return cs.name
