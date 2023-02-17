import sys

if len(sys.argv) == 1:
    print("Please provide a page name")
    sys.exit(1)

# Getting info about the page name
page_name = sys.argv[1]
page_words = page_name.split()


def _copy_with_replace(old_file, new_file, **placeholdervals):
    with open(old_file, 'r') as file_from, open(new_file, 'w+') as file_to:
        for line in file_from.readlines():
            content = line
            for placeholder, value in placeholdervals.items():
                content = content.replace(
                    f'{{%{placeholder.upper()}%}}', value)
            file_to.write(content)


def _insert_into_file(insert_file, append_end=[], **markervals):

    with open(insert_file, 'r') as file:
        content = file.readlines()
    new_content = []

    where = 'root'
    for line in content:
        if where in markervals.keys():
            new_content.append(markervals[where])
            where = 'root'

        for marker in markervals.keys():
            if marker in line:
                where = marker

        new_content.append(line)

    new_content.extend(append_end)

    with open(insert_file, 'w') as file:
        file.writelines(new_content)


def move_page_files(file_name, text_capital, store, text):
    from_edit_page = 'resources/EditPage.vue'
    from_page = 'resources/Page.vue'
    to_edit_page = f'./../pages/admin/{file_name}.vue'
    to_page = f'./../pages/{file_name}.vue'
    _copy_with_replace(from_edit_page, to_edit_page,
                       pagetextcapital=text_capital, pagestore=store, pagetext=text)
    _copy_with_replace(
        from_page, to_page, pagetextcapital=text_capital, pagestore=store, pagetext=text)


def add_type(file_name, store):
    types_file = './../util/types.ts'
    replace_markers = {
        '// pages type definition, do not remove this line': f"\t{store}: {file_name}"
    }
    extend_content = [
        "\n", f"export type {file_name} = {{\n", "\ttitle: string\n", "}"]
    _insert_into_file(types_file, extend_content, **replace_markers)


def add_to_store(store):
    store_file = './../stores/pages.ts'
    replace_markers = {
        '// default values, do not remove this line': f"\t\t{store}: {{title: ''}},\n",
        '// computed pages, do not remove this line': f"\tconst {store} = computed(() => pages.value.{store})\n",
        '// return statement, do not remove this line': f"\t\t{store},\n"
    }
    _insert_into_file(store_file, **replace_markers)


# Names to be used
file_name = ''.join([x.lower().capitalize() for x in page_words])
store = file_name[0].lower() + file_name[1:]
text = ' '.join(page_words)
text_capital = text.capitalize()

move_page_files(file_name, text_capital, store, text)
add_type(file_name, store)
add_to_store(store)
print('gelukt')

sys.exit(0)
