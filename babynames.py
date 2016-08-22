#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_year(file_as_string):
  match = re.search(r'Popularity\sin\s(\d+)', file_as_string)

  if match:
    return match.group(1)
  else:
    print 'No matches'
    sys.exit(0)

def extract_matches(file_as_string):
  matches = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file_as_string)

  if len(matches) > 0:
    return matches
  else:
    print 'No matches'
    sys.exit(0)

def remove_duplicates(names):
  result = list()

  name_rank = dict()

  for pair in names:
    name_rank[pair.split()[0]] = pair.split()[1]

  pre_process = [(name, name_rank[name]) for name in sorted(name_rank.keys())]

  for i in range(1, len(pre_process)):
    if pre_process[i - 1][0] == pre_process[i][0]:
      if int(pre_process[i - 1][1]) > int(pre_process[i][1]):
        result.pop()
        result.append(pre_process[i][0] + ' ' + pre_process[i][1])
    else:
      result.append(pre_process[i][0] + ' ' + pre_process[i][1])

  return result

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  input_file = open(filename, 'r')
  file_as_string = input_file.read()

  result = list()

  result.append(extract_year(file_as_string))

  matches = extract_matches(file_as_string)
  names = list()

  for match in matches:
    names.append(match[1] + ' ' + match[0])
    names.append(match[2] + ' ' + match[0])

  names.sort()

  result += remove_duplicates(names)

  input_file.close()
  return result


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for arg in args:
    if not summary:
      text = '\n'.join(extract_names(arg)) + '\n'
      print text
    else:
      output_file = open(arg + '.summary', 'w')
      text = '\n'.join(extract_names(arg)) + '\n'
      output_file.write(text)
      output_file.close()

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
