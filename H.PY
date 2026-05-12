import urllib.request
from html.parser import HTMLParser

class GoogleDocParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_tr = False
        self.in_td = False
        self.current_cell = []
        self.current_row = []
        self.table_data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.in_tr = True
            self.current_row = []
        elif tag == 'td' and self.in_tr:
            self.in_td = True
            self.current_cell = []

    def handle_endtag(self, tag):
        if tag == 'td' and self.in_td:
            self.in_td = False
            # Clean up newlines but preserve actual spaces
            cell_text = "".join(self.current_cell).replace('\n', '')
            self.current_row.append(cell_text)
        elif tag == 'tr' and self.in_tr:
            self.in_tr = False
            if self.current_row:
                self.table_data.append(self.current_row)

    def handle_data(self, data):
        if self.in_td:
            self.current_cell.append(data)

def decode_message(url):
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return

    parser = GoogleDocParser()
    parser.feed(html_content)

    points = []
    max_x = max_y = 0

    for row in parser.table_data[1:]:
        if len(row) >= 3:
            try:
                x = int(row[0].strip())
                char = row[1]
                if not char: 
                    char = ' '
                y = int(row[2].strip())
                
                points.append((char, x, y))
                max_x = max(max_x, x)
                max_y = max(max_y, y)
            except ValueError:
                continue

    if not points:
        print("No valid grid data found.")
        return

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in points:
        grid[y][x] = char

    for row in reversed(grid):
        print("".join(row))

doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
decode_message(doc_url)