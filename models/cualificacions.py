# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cualificacions(models.Model):
    _name = 'lago_javier.cualificacions'
    _description = 'lago_javier.lago_javier'

    apelidos = fields.Char(required=True, size=20, string="Apelidos")
    nome = fields.Char(required=True, size=20, string="Nome")
    ano = fields.Char(required=True, size=20, string="Ano academico")
    ciclo = fields.Char(required=True, size=20, string="Ciclo")
    quenda = fields.Selection([('Vespertino', 'Vespertino'), ('Ordinario', 'Ordinario'), ('FPDual', 'FPDual')],
                              string="Quenda")
    curso = fields.Integer(required=True)
    modulo = fields.Char(required=True)
    notatexto = fields.Char(compute="_notatexto", store=True, string="Nota texto")
    nota = fields.Integer(string="Nota")

    @api.depends('nota')
    def _notatexto(self):
        for rexistro in self:
            if rexistro.nota < 5:
                rexistro.notatexto = "Suspenso"
            elif rexistro.nota == 5:
                rexistro.notatexto = "Aprobado"
            elif rexistro.nota == 6:
                rexistro.notatexto = "Ben"
            elif rexistro.nota == 7:
                rexistro.notatexto = "Ben"
            elif rexistro.nota == 8:
                rexistro.notatexto = "Notable"
            elif rexistro.nota == 9:
                rexistro.notatexto = "Sobresaliente"
            else:
                rexistro.notatexto = "Sobresaliente"
