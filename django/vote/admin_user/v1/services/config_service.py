from admin_user import models

class Config(object):
	def __init__(self):
		self.config = models.Config.objects.all()
		self.type = {
		"integer":int,
		"float":float,
		"string":str
		}
	def get_config(self):
		config_data=dict()
		for row in self.config:
			try:
				config_data[row.attribute_name] = self.type[row.attribute_type](row.attribute_value)
			except Exception as e:
				config_data[row.attribute_name] = row.attribute_value
		return {
					"config":config_data
			}
