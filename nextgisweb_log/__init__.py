# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nextgisweb.component import Component
from .model import Base


class LogComponent(Component):
    identity = 'log'
    metadata = Base.metadata

    def initialize(self):
        pass

    def setup_pyramid(self, config):
        from . import view  # NOQA
        view.setup_pyramid(self, config)


def pkginfo():
    return dict(components=dict(
        log="nextgisweb_log"))


def amd_packages():
    return ((
        'ngw-log', 'nextgisweb_log:amd/ngw-log'),
    )
