import cmd

from prettytable import PrettyTable
    
class Table(object):
	def __init__(self):
		self.table = PrettyTable()
		self.table.field_names = ["Title", "URL", "Site", "Text content", "Extension", "Type of file:", "Exact match of title", "Exact match of URL", "Excluded terms", "Information"]
		self.rows = [ "" for fields in self.table.field_names]
		self.table.add_row(self.rows)
		# self.related = []
		# self.info = []
		# self.excluded_terms
		#.clear_rows()

class InteractiveMode(cmd.Cmd):
	"""Simple command processor example."""
	table = Table()
	prompt = "dork@generator~> "
	intro = "Simple dork generator."
	doc_header = 'doc_header'
	misc_header = 'misc_header'
	undoc_header = 'undoc_header'

	ruler = '-'

	def do_show(self, line):
		"""test 
		Ce script ne sert à rien
		"""
		print(InteractiveMode.table.table)

	def do_set(self, line):
		"""set title [title of search]
		Allows to specify the title of the related search
		"""
		field,value = [s for s in line.split()]
		self.replace_val(field, value)		
		#InteractiveMode.table.del_row(index)


	def do_exit(self, line):
		""" exit
		Quit the current process"""
		return True

	def do_EOF(self, line):
		return True

	def postloop(self):
		print ("Thank you")

	def replace_val(self, field, value):
		InteractiveMode.table.table.clear_rows()
		lowers = [elem.lower() for elem in InteractiveMode.table.table.field_names]
		position = lowers.index(field.lower())
		InteractiveMode.table.rows[position] = value
		InteractiveMode.table.table.add_row(InteractiveMode.table.rows)


class RawQuery(object):

	def __init__(self):
		self.exact_title = ""
		self.exact_url = ""
		self.exact_text = ""
		self.title = []
		self.url = []
		self.site = []
		self.text = []
		self.extension = []
		self.filetype = []
		self.allintitle = []
		self.allinurl = []
		self.related = []
		self.info = []
		self.exact_terms = []
		self.excluded_terms = []
		self.query = ""

if __name__ == '__main__':
	InteractiveMode().cmdloop()