# -*- coding: UTF-8 -*-
import appModuleHandler
import api
import ui
import controlTypes

class AppModule(appModuleHandler.AppModule):

	def event_gainFocus(self, obj, nextHandler):
		textList = []
		if obj.name:
			textList.append(obj.name)
		if obj.value:
			textList.append(obj.value)
		textList.append(controlTypes.roleLabels[obj.role])
		text = " ".join(textList)
		ui.message(text)
		if obj.role is controlTypes.ROLE_TREEVIEW:
			nextHandler()


	def script_reportChannelMember(self,gesture):
		gesture.send()
		obj = api.getFocusObject()
		if obj.role is controlTypes.ROLE_UNKNOWN:
				objP = obj.parent
				if objP is not None and objP.name:
					api.setNavigatorObject(objP)
					ui.message(objP.name)


	__gestures = {
		"kb:UPARROW": "reportChannelMember",
		"kb:DOWNARROW": "reportChannelMember",
	}
