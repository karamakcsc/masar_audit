# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "masar_audit"
app_title = "Masar Audit"
app_publisher = "KCSC"
app_description = "Manage auditing firms"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "yasseralghoul@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/masar_audit/css/masar_audit.css"
# app_include_js = "/assets/masar_audit/js/masar_audit.js"

# include js, css files in header of web template
# web_include_css = "/assets/masar_audit/css/masar_audit.css"
# web_include_js = "/assets/masar_audit/js/masar_audit.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "masar_audit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "masar_audit.install.before_install"
# after_install = "masar_audit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "masar_audit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doctype_js = {
    "Quotation" : "custom/Quotation/quotation.js",
    "Project" : "custom/project/project.js"
 }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"masar_audit.tasks.all"
# 	],
# 	"daily": [
# 		"masar_audit.tasks.daily"
# 	],
# 	"hourly": [
# 		"masar_audit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"masar_audit.tasks.weekly"
# 	]
# 	"monthly": [
# 		"masar_audit.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "masar_audit.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "masar_audit.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "masar_audit.task.get_dashboard_data"
# }

fixtures = [
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", [
                "Quotation-quotation_documents",
                "Quotation-quotation_document_template",
                "Quotation-section_break_34",
                "Project-column_break_21",
        		"Project-revenue",
        		"Project-wip_clients",
        		"Project-unbilled_revenue",
        		"Project-deferred_revenue",
                "Project-account",
                "Journal Entry-project",
                "Project-revenue_balance",
                "Project-wip_clients_balance",
                "Project-unbilled_revenue_balance",
                "Project-deferred_revenue_balance",
            ]
        ]
    ]}
]
