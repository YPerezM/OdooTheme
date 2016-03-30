# -*- coding: utf-8 -*-

from datetime import timedelta

from openerp import models, fields, api, exceptions, _



class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)

    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")
        
    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', _(u"Copy of {}%").format(self.name))])

        if not copied_count:
            new_name = _(u"Copy of {}").format(self.name)

        else:
            new_name = _(u"Copy of {} ({})").format(self.name, copied_count)


        default['name'] = new_name
        return super(Course, self).copy(default)

        
    
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]




class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    color = fields.Integer()

    
    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=['|', ('instructor', '=', True),
                     ('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)

    attendee_ids = fields.Many2many('res.partner', string="Attendees")