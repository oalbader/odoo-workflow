# -*- coding: utf8 -*-
from odoo import models, fields, api,_


class Workflow(models.Model):
    _name = 'workflow.workflow'

    name = fields.Char(string='Name', required=True)
    model_id = fields.Many2one('ir.model', string='Model', required=True)
    node_ids = fields.One2many('workflow.node', 'workflow_id', string='Nodes')


class WorkflowNode(models.Model):
    _name = 'workflow.node'

    name = fields.Char(string='Name', required=True)
    workflow_id = fields.Many2one('workflow.workflow', string='Workflow', required=True, ondelete='cascade')
    out_link_ids = fields.One2many('workflow.link', 'node_from', string='Outgoing link')
    in_link_ids = fields.One2many('workflow.link', 'node_to', string='Ingoing link')
    start_node = fields.Boolean(string='Workflow start', default=False)
    end_node = fields.Boolean(string='Workflow end', default=False)


class WorkflowLik(models.Model):
    _name = 'workflow.link'

    name = fields.Char(string='Name')
    node_from = fields.Many2one('workflow.node', string='Source Node', required=True)
    node_to = fields.Many2one('workflow.node', string='Destination Node', required=True)

