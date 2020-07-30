# -*- coding: utf-8 -*-
#
# The main entry point to the plugin.
#
# 2020-07-29 - Initial version.
# 2020-07-30 - Comments, header, test GitHub.
#              Added first version of Event handler.
#
from __future__ import absolute_import, unicode_literals

import octoprint.events
import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.EventHandlerPlugin,
                       octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
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
        if event == octoprint.events.Events.UPLOAD:
            self._logger.info("File Uploaded: %s" % payload["file"])

        elif event == octoprint.events.Events.CLIENT_OPENED:
            self._logger.info("File Uploaded: %s" % payload["remoteAddress"])

        else:
            self._logger.info("Unhandled Event: %s" % event)



__plugin_name__ = "CNC Camera"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()