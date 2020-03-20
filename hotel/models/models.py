# -*- coding: utf-8 -*-

from odoo import models, fields, api


class hotel(models.Model):
    _name = 'hotel.hotel'
    _description = 'hotel.hotel'

    name = fields.Char()
    value = fields.Integer()

class HotelFloor(models.Model):
    _name = 'hotel.floor'
    _description = 'hotel.floor'

    name = fields.Char()
    floor_number = fields.Char()
    no_of_room = fields.Integer()
    building_id = fields.Char()

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'hotel.room'

    room_no = fields.Char()
    roomtypemap_code = fields.Char()
    roomview_code = fields.Char()
    roommap_code = fields.Char()
    room_bedtype = fields.Char()
    room_ratecode = fields.Char()
    room_facilitycode = fields.Char()
    room_size = fields.Char()
    room_extension = fields.Char()
    room_image = fields.Binary()
    room_description = fields.Char()

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Property(models.Model):
    _name = 'property.property'
    _description = 'property.property'

    name = fields.Char(string='Hotel Name', required=True)
    code = fields.Char(string='Hotel Code', required=True)
    address1 = fields.Char(string='Address1', required=True)
    address2 = fields.Char(string='Address2', required=True)
    address3 = fields.Char(string='Address3', required=True)