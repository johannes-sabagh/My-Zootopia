import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def create_html():
    animals_data = load_data("animals_data.json")
    output = ''
    for animal in animals_data:
        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        locations = animal["locations"][0]
        animal_type = animal["characteristics"].get("type")
        output += '<li class="cards__item">'
        output += f'<div class="card__title">{name}</div>\n'
        output += '<p class="card__text">'
        output += f'<strong>Diet: </strong>{diet}<br/>\n'
        output += f'<strong>Location: </strong>{locations}<br/>\n'
        if animal_type:
            output += f'<strong>Type: </strong>{animal_type}<br/>\n'
        output += '</p>'
        output += '</li>'
    return output
html_output = create_html()
def load_html(html_path):
    """loads HTML file"""
    with open(html_path, "r") as html_file:
        return html_file.read()
html_text = load_html("animals_template.html")

def write_html(html_output, html_text):
    """create new html from the template and the output from JSON"""
    new_html_text = html_text.replace("__REPLACE_ANIMALS_INFO__", html_output)
    with open("animals.html", "w") as new_html:
        new_html.write(new_html_text)


def main():
    create_html()
    write_html(html_output, html_text)

if __name__ == "__main__":
    main()