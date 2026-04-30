from __future__ import unicode_literals
import os, re, json
import frappe
from frappe.utils import flt, cint, get_time, make_filter_tuple, get_filter, add_to_date, cstr, get_timespan_date_range, nowdate, add_days, getdate, add_months, get_datetime
from frappe import _
from frappe.desk.reportview import get_filters_cond
from frappe.cache_manager import clear_user_cache
from six import string_types


@frappe.whitelist()
def get_module_name_from_doctype(doc_name, current_module=""):
    if not doc_name:
        return []

    values = {"doc_name": doc_name}
    condition = ""

    if current_module:
        condition = "and w.`name` = %(current_module)s"
        values["current_module"] = current_module

    rows = frappe.db.sql(
        f"""
        select
            w.`name` as module,
            (
                select restrict_to_domain
                from `tabModule Def`
                where `name` = w.module
            ) as restrict_to_domain
        from `tabWorkspace` w
        inner join `tabWorkspace Link` l on w.`name` = l.parent
        where l.link_to = %(doc_name)s
        {condition}
        limit 1
        """,
        values,
        as_dict=True,
    )

    if rows:
        return [{"module": rows[0]["module"]}]

    return []


@frappe.whitelist()
def change_language(language):
    frappe.db.set_value("User", frappe.session.user, "language", language)
    clear()
    return True


@frappe.whitelist()
def get_current_language():
    return frappe.db.get_value("User", frappe.session.user, "language")


@frappe.whitelist()
def get_company_logo():
    logo_path = ""
    current_company = frappe.defaults.get_user_default("company")
    if current_company:
        logo_path = frappe.db.get_value("Company", current_company, "company_logo")

    return logo_path


@frappe.whitelist(allow_guest=True)
def get_theme_settings():
    doc = frappe.get_single("Theme Settings")

    slideshow_photos = []
    if doc.background_type == "Slideshow":
        slideshow_photos = [
            {"photo": row.photo}
            for row in doc.get("slideshow_photos", [])
        ]

    return {
        "enable_background": doc.enable_background,
        "background_photo": doc.background_photo,
        "background_type": doc.background_type,
        "full_page_background": doc.full_page_background,
        "transparent_background": doc.transparent_background,
        "slideshow_photos": slideshow_photos,
        "dark_view": doc.dark_view,
        "theme_color": doc.theme_color,
        "open_workspace_on_mobile_menu": doc.open_workspace_on_mobile_menu,
        "show_icon_label": doc.show_icon_label,
        "hide_icon_tooltip": doc.hide_icon_tooltip,
        "always_close_sub_menu": doc.always_close_sub_menu,
        "menu_opening_type": doc.menu_opening_type,
        "loading_image": doc.loading_image,
        "theme_logo": getattr(doc, "theme_logo", ""),
        "favicon": getattr(doc, "favicon", ""),
        "font_family": getattr(doc, "font_family", ""),
    }


@frappe.whitelist()
def update_theme_settings(**data):
    data = frappe._dict(data)
    doc = frappe.get_single("Theme Settings")

    allowed_fields = [
        "theme_color",
        "apply_on_menu",
        "apply_on_dashboard",
        "apply_on_workspace",
        "apply_on_navbar",
        "dark_view",
        "enable_background",
        "background_photo",
        "background_type",
        "full_page_background",
        "transparent_background",
        "open_workspace_on_mobile_menu",
        "show_icon_label",
        "hide_icon_tooltip",
        "always_close_sub_menu",
        "menu_opening_type",
        "loading_image",
        "theme_logo",
        "favicon",
        "font_family",
    ]

    for field in allowed_fields:
        if field in data:
            doc.set(field, data.get(field))

    doc.save(ignore_permissions=True)
    frappe.clear_cache()

    return doc


@frappe.whitelist()
def get_events(start=getdate(), end=getdate().year, user=None, for_reminder=False, filters=None):
    end = str(getdate().year) + "-12-31"
    if not user:
        user = frappe.session.user

    if isinstance(filters, string_types):
        filters = json.loads(filters)

    filter_condition = get_filters_cond('Event', filters, [])

    tables = ["`tabEvent`"]
    if "`tabEvent Participants`" in filter_condition:
        tables.append("`tabEvent Participants`")

    events = frappe.db.sql("""
        SELECT `tabEvent`.name,
                `tabEvent`.subject,
                `tabEvent`.description,
                `tabEvent`.color,
                `tabEvent`.starts_on,
                `tabEvent`.ends_on,
                `tabEvent`.owner,
                `tabEvent`.all_day,
                `tabEvent`.event_type,
                `tabEvent`.repeat_this_event,
                `tabEvent`.repeat_on,
                `tabEvent`.repeat_till,
                `tabEvent`.monday,
                `tabEvent`.tuesday,
                `tabEvent`.wednesday,
                `tabEvent`.thursday,
                `tabEvent`.friday,
                `tabEvent`.saturday,
                `tabEvent`.sunday
        FROM {tables}
        WHERE (
                (
                    (date(`tabEvent`.starts_on) BETWEEN date(%(start)s) AND date(%(end)s))
                    OR (date(`tabEvent`.ends_on) BETWEEN date(%(start)s) AND date(%(end)s))
                    OR (
                        date(`tabEvent`.starts_on) <= date(%(start)s)
                        AND date(`tabEvent`.ends_on) >= date(%(end)s)
                    )
                )
                OR (
                    date(`tabEvent`.starts_on) <= date(%(start)s)
                    AND `tabEvent`.repeat_this_event=1
                    AND coalesce(`tabEvent`.repeat_till, '3000-01-01') > date(%(start)s)
                )
            )
        {reminder_condition}
        {filter_condition}
        AND (
                `tabEvent`.event_type='Public'
                OR `tabEvent`.owner=%(user)s
                OR EXISTS(
                    SELECT `tabDocShare`.name
                    FROM `tabDocShare`
                    WHERE `tabDocShare`.share_doctype='Event'
                        AND `tabDocShare`.share_name=`tabEvent`.name
                        AND `tabDocShare`.user=%(user)s
                )
            )
        AND `tabEvent`.status='Open'
        ORDER BY `tabEvent`.starts_on""".format(
        tables=", ".join(tables),
        filter_condition=filter_condition,
        reminder_condition="AND coalesce(`tabEvent`.send_reminder, 0)=1" if for_reminder else ""
    ), {
        "start": start,
        "end": end,
        "user": user,
    }, as_dict=1)

    return events


@frappe.whitelist()
def update_menu_modules(modules):
    modules_list = json.loads(modules)
    for module in modules_list:
        if frappe.db.exists("Workspace", module["name"]):
            if (module["_is_deleted"] == 'true'):
                frappe.delete_doc("Workspace", module["name"], force=True)
            else:
                frappe.db.set_value("Workspace", module["name"], {
                    "title": module['title'],
                    "label": module["title"],
                    "icon": module["icon"],
                    "sequence_id": int(module["sequence_id"])
                })
        else:
            if (module["_is_new"] == 'true'):
                workspace = frappe.new_doc("Workspace")
                workspace.title = module["title"]
                workspace.icon = module["icon"]
                workspace.content = module["content"]
                workspace.label = module["label"]
                workspace.sequence_id = int(module["sequence_id"])
                workspace.for_user = ""
                workspace.public = 1
                workspace.save(ignore_permissions=True)

    return True


def clear():
    frappe.local.session_obj.update(force=True)
    frappe.local.db.commit()
    clear_user_cache(frappe.session.user)
    frappe.response['message'] = _("Cache Cleared")
