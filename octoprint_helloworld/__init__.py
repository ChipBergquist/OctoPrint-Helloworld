# -*- coding: utf-8 -*-
#
# The main entry point to the plugin.
#
# 2020-07-29 - Initial version.
# 2020-07-30 - Comments, header, test GitHub.
#              Added first version of Event handler.
# 2020-08-03 - Simple API Support
#
from __future__ import absolute_import, unicode_literals

import flask
import json

import octoprint.events
import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.EventHandlerPlugin,
                       octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.SimpleApiPlugin):
    def on_after_startup(self):
        self._logger.info("URL: %s" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]
    
    def get_assets(self):
        return dict(
            js=["js/helloworld.js"]
        )
    
    def on_event(self, event, payload):
        self._logger.info('Event: {0} - {1}'.format(event, json.dumps(payload)))


    def custom_atcommand_handler(self, comm, phase, command, parameters, tags=None, *args, **kwargs):
        self._logger.info('Command: {0}'.format(command))

    def get_api_commands(self):
        self._logger.info('get_api_commands')
        return dict(
            command1=[],
            command2=["some_parameter"]
        )

    def on_api_command(self, command, data):
        self._logger.info('on_api_command')
        if command == "command1":
            parameter = "unset"
            if "parameter" in data:
                parameter = "set"
            self._logger.info("command1 called, parameter is {parameter}".format(**locals()))
        elif command == "command2":
            self._logger.info("command2 called, some_parameter is {some_parameter}".format(**data))
        return flask.jsonify(who="you")

    def on_api_get(self, request):
        self._logger.info('on_api_get')
        return flask.jsonify(foo="bar")
        

__plugin_name__ = "CNC Camera"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
__plugin_hooks__ = {"octoprint.comm.protocol.atcommand.queuing": __plugin_implementation__.custom_atcommand_handler}