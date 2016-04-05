# This script exists purely to convert input text to a format for skype
# which looks like the kind of threat a certain character might give

from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

# Declare variables
n_data = []
lens = []
text = []

# Purely because I don't know how to impliment an input from a webpage:
# Grab input from a text file called 'text.txt' 
with open ("text.txt", "rb") as myfile:
	data = myfile.readlines()
	i = 0
	for item in data:
		# Strip out new lines, 'cause we need to impliment our own
		# to make the skype message prettier~!
		n_data.append( str( data[i].upper() ).replace("\n","") ) 
		i += 1
data = ''.join(n_data)

# Calculate the length of each word and store in 'lens' array
# We use the lens calculated here
i = 0
for char in data:
	if char.isspace():
		lens.append(i)
		i = 0
	if not char.isspace():
		i += 1
# Slap on the straggler
if i > 0:
	lens.append(i)

# Create the special text~~
text.append("!! ")
i = 0
j = 1
for char in data:
	# Skype only uses 42 chars (in this font, at max) before a new line
	if char.isspace():
		if (int(lens[j])*2 + i + 2) > 42:
			text.append("\n")
			i = 0
			j += 1
		else:
			text.append("  ")
			i += 2
			j += 1
	else:
		text.append(char + " ")
		i += 2

# Turn it into a string
output = ''.join(text)

# Display the location and temperature in HTML
html = '''
<!doctype html>
<html>
<body bgcolor="#1A1A1A">
<pre>%s</pre>
</body>
</html>
'''

@app.route("/")
def root():
    return html % (output)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=80)
