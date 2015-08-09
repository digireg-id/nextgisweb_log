# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nextgisweb import dynmenu as dm

from pyramid.httpexceptions import HTTPForbidden
from sqlalchemy import desc

from .model import LogEntry


def check_permission(request):
    if not request.user.is_administrator:
        raise HTTPForbidden("Membership in group 'administrators' required!")


def messages_browse(request):
    check_permission(request)
    return dict(
        title=u'Журнал сообщений',
        obj_list=LogEntry.query().order_by(desc(LogEntry.id)),
        dynmenu=request.env.pyramid.control_panel)


def message_info(request):
    check_permission(request)
    return dict(
        title=u'Запись %s' % request.matchdict['id'],
        obj=LogEntry.filter_by(id=request.matchdict['id']).one(),
        dynmenu=request.env.pyramid.control_panel)


def setup_pyramid(comp, config):

    config.add_route(
        'log.message.browse',
        '/log/messages/') \
        .add_view(messages_browse, renderer='nextgisweb_log:/template/message_browse.mako')

    config.add_route(
        'log.message.info',
        '/log/message/{id:\d+}', client=('id', )) \
        .add_view(message_info, renderer='nextgisweb_log:/template/message_info.mako')


    #  menu in admin

    class LogMenu(dm.DynItem):
        def build(self, kwargs):
            yield dm.Link(
                self.sub('browse'), u'Просмотреть',
                lambda kwargs: kwargs.request.route_url('log.message.browse')
            )

    LogMenu.__dynmenu__ = comp.env.pyramid.control_panel

    comp.env.pyramid.control_panel.add(
        dm.Label('log', u'Журнал сообщений'),
        LogMenu('log'),
    )

