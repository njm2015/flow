class Circuit(object):

	def __init__(self, source_voltage):
		self.source = None
		self.source_voltage = source_voltage
		self.series_components = []

	def set_source(self, component):
		self.source = component

	def propogate(self):
		# Logic to propogate voltage across components
		self.propogate_rec(self.source, [])

	def propogate_rec(self, component, cur_series):

		if component.id == self.source.id and len(cur_series) > 0:
			# we have reached the end
			return cur_series

		if len(component.output) == 0:
			# component is not connected to anything
			# don't add it to the series components
			return None
		elif len(component.output) == 1:
			# easy - component is connected and only has 1 output
			cur_series.append(component)
			return propogate_rec(component.output[0], cur_series)
		elif len(component.output) > 1:
			# difficult one
			
			# find where the points meet up

			# create new component

	def print(self):
		self.print_rec(self.source, set())
		
	def print_rec(self, component, visited):

		if component.id in visited:
			return visited

		print('ID: {}\tName: {}'.format(component.id, component.name))
		visited.add(component.id)

		for out_component in component.output:
			visited = self.print_rec(out_component, visited)

		return visited



class Component(object):

	def __init__(self, id, name, is_power=False):
		self.id = id
		self.name = name
		self.is_power = is_power
		self.input = set()
		self.output = set()
		self.subcomponents = set()

	def connect(self, other):
		self.output.add(other)
		other.input.add(self)

	def has_next(self):
		return len(self.output) > 0
