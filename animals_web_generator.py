import data_fetcher

def create_html_from_json(animals_data):
    """ creates a HTML structure with the data from JSON"""
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def serialize_animal(animal):
    """handle a single animal serialization"""
    output = ''
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    locations = animal["locations"][0]
    animal_type = animal["characteristics"].get("type")
    output += '<li class="cards__item">'
    if name:
        output += f'<div class="card__title">{name}</div>\n'
    output += '<p class="card__text">'
    if diet:
        output += f'<strong>Diet: </strong>{diet}<br/>\n'
    if locations:
        output += f'<strong>Location: </strong>{locations}<br/>\n'
    if animal_type:
        output += f'<strong>Type: </strong>{animal_type}<br/>\n'
    output += '</p>'
    output += '</li>'
    return output


def load_html(html_path):
    """loads HTML file"""
    with open(html_path, "r") as html_file:
        return html_file.read()


def write_html(html_output, html_text, text_to_replace):
    """create new html from the template and the output from JSON"""
    new_html_text = html_text.replace(text_to_replace, html_output)
    with open("animals.html", "w") as new_html:
        new_html.write(new_html_text)


def main():
    animal_name = input("Please enter an animal: ")
    print("Website was successfully generated to the file animals.html.")
    animals_data = data_fetcher.fetch_data(animal_name)

    # if no animal is found a message will be shown on the website "The animal xxxx doesn't exist."
    if not animals_data:
        html_output = f"<h2 style='text-align: center'>The animal <div style='color: red'>{animal_name}</div> doesn't exist.</h2>"
        html_text = load_html("animals_template.html")
        text_to_replace = "__REPLACE_ANIMALS_INFO__"
        write_html(html_output, html_text, text_to_replace)
    else:
        html_output = create_html_from_json(animals_data)
        html_text = load_html("animals_template.html")
        text_to_replace = "__REPLACE_ANIMALS_INFO__"
        write_html(html_output, html_text, text_to_replace)

if __name__ == "__main__":
    main()