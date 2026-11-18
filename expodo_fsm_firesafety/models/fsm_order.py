from odoo import models, fields


class FsmOrder(models.Model):
    _inherit = "expodo.fsm.order"

    # Equipment
    equipment_type = fields.Selection(
        [
            ("extinguisher", "Fire extinguisher"),
            ("fire_alarm", "Fire alarm / panel"),
            ("smoke_detector", "Smoke / heat detector"),
            ("emergency_light", "Emergency lighting"),
            ("hose_reel", "Fire hose reel"),
            ("sprinkler", "Sprinkler system"),
            ("dry_riser", "Dry / wet riser"),
            ("fire_door", "Fire door"),
            ("fire_blanket", "Fire blanket"),
            ("other", "Other"),
        ],
        string="Equipment Type",
    )
    agent_type = fields.Selection(
        [
            ("water", "Water"),
            ("foam", "Foam (AFFF)"),
            ("co2", "CO2"),
            ("dry_powder", "Dry powder (ABC)"),
            ("wet_chemical", "Wet chemical"),
            ("clean_agent", "Clean agent"),
            ("other", "Other"),
        ],
        string="Extinguishing Agent",
        help="For extinguishers",
    )
    device_brand = fields.Char(string="Brand")
    device_model = fields.Char(string="Model Reference")
    serial_number = fields.Char(string="Serial / Asset No.", index=True)
    building = fields.Char(string="Building / Site")
    device_location = fields.Char(
        string="Location", help="Where the device is installed (floor, room, zone...)"
    )
    capacity = fields.Char(string="Capacity", help="For example 6 kg, 9 L")
    install_date = fields.Date(string="Install Date")

    # Inspection and testing
    last_inspection_date = fields.Date(string="Last Inspection")
    next_inspection_date = fields.Date(
        string="Next Inspection Due", help="Date the next periodic inspection is due"
    )
    inspection_body = fields.Char(string="Inspection Body")
    compliance_ref = fields.Char(string="Compliance Certificate Ref")
    last_pressure_test = fields.Date(
        string="Last Pressure Test", help="Last hydrostatic pressure test"
    )
    next_pressure_test = fields.Date(string="Next Pressure Test Due")

    # Condition checks
    pressure_gauge_ok = fields.Boolean(string="Pressure Gauge in Range")
    seal_intact = fields.Boolean(string="Tamper Seal Intact")
    safety_pin_ok = fields.Boolean(string="Safety Pin in Place")
    hose_nozzle_ok = fields.Boolean(string="Hose / Nozzle OK")
    access_clear = fields.Boolean(string="Access Clear / Unobstructed")
    signage_ok = fields.Boolean(string="Signage in Place")
