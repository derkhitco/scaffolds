import sys

if len(sys.argv) == 1:
    print("Please provide a page name")
    sys.exit(1)

# Getting info about the page name
page_name = sys.argv[1]
page_words = page_name.split()


def move_page_files(file_name, text_capital, store, text):
    from_edit_page = 'resources/EditPage.vue'
    from_page = 'resources/Page.vue'
    to_edit_page = f'./../src/views/admin/Edit{file_name}.vue'
    to_page = f'./../src/views/site/{file_name}.vue'

    with open(from_edit_page, 'r') as file_from, open(to_edit_page, 'w+') as file_to:
        for line in file_from.readlines():
            content = line.replace('{%PAGETEXTCAPITAL%}', text_capital)
            content = content.replace('{%PAGESTORE%}', store)
            content = content.replace('{%PAGETEXT%}', text)
            file_to.write(content)

    with open(from_page, 'r') as file_from, open(to_page, 'w+') as file_to:
        for line in file_from.readlines():
            content = line.replace('{%PAGETEXTCAPITAL%}', text_capital)
            content = content.replace('{%PAGESTORE%}', store)
            content = content.replace('{%PAGETEXT%}', text)
            file_to.write(content)

def add_type(file_name, store):
    types = './../src/util/types.ts'
    with open(types, 'r') as file:
        content = file.readlines()
    new_content = []
    
    where = 'root'
    for line in content:
        if where == 'pages':
            new_content.append(f"\t{store}: {file_name}\n")
            where = ''
        if '// pages type definition, do not remove this line' in line:
            where = 'pages'
        new_content.append(line)

    new_content.append(f"\n")
    new_content.append(f"export type {file_name} = {{\n")
    new_content.append(f"\ttitle: string\n")
    new_content.append("}")

    with open(types, 'w') as file:
        file.writelines(new_content)

def add_routes(file_name, text_capital):
    routes = './../src/router.ts'
    with open(routes, 'r') as file:
        content = file.readlines()
    new_content = []    
    
    where = 'root'
    for line in content:
        if where == 'siteImports':
            new_content.append(f"import {file_name} from './views/site/{file_name}.vue'\n")
            where = ''
        if where == 'adminImports':
            new_content.append(f"import Edit{file_name} from './views/admin/Edit{file_name}.vue'\n")
            where = ''
        if where == 'site':
            new_content.append('\t\t\t{\n')
            new_content.append(f"\t\t\t\tpath: '{file_name.lower()}',\n")
            new_content.append(f"\t\t\t\tname: '{text_capital}',\n")
            new_content.append(f"\t\t\t\tcomponent: {file_name},\n")
            new_content.append("\t\t\t\tmeta: {inHeader: true},\n")
            new_content.append('\t\t\t},\n')
            where = ''
        if where == 'admin':
            new_content.append('\t\t\t{\n')
            new_content.append(f"\t\t\t\tpath: '{file_name.lower()}',\n")
            new_content.append(f"\t\t\t\tname: '{text_capital} pagina',\n")
            new_content.append(f"\t\t\t\tcomponent: Edit{file_name},\n")
            new_content.append("\t\t\t\tmeta: {inHeader: true},\n")
            new_content.append('\t\t\t},\n')
            where = ''
        if '// Site imports (do not remove this line)' in line:
            where = 'siteImports'
        if '// placeholder for adding site children. Do not remove' in line:
            where = 'site'
        if '// Admin imports (do not remove this line)' in line:
            where = 'adminImports'
        if '// placeholder for adding admin children. Do not remove' in line:
            where = 'admin'
        new_content.append(line)
    
    with open(routes, 'w') as file:
        file.writelines(new_content)

def add_to_store(store):
    store_file = './../src/stores/pages.ts'
    with open(store_file, 'r') as file:
        content = file.readlines()
    new_content = []

    where = 'root'
    for line in content:
        if where == 'default':
            new_content.append(f"\t\t{store}: {{title: ''}},\n")
            where = ''
        if where == 'computed':
            new_content.append(f"\tconst {store} = computed(() => texts.value.{store})\n")
            where = ''
        if where == 'return':
            new_content.append(f"\t\t{store},\n")
            where = ''
        if '// default values, do not remove this line' in line:
            where = 'default'
        if '// computed pages, do not remove this line' in line:
            where = 'computed'
        if '// return statement, do not remove this line' in line:
            where = 'return'
        new_content.append(line)

    with open(store_file, 'w') as file:
        file.writelines(new_content)

# Names to be used
file_name = ''.join([x.lower().capitalize() for x in page_words]) 
store = file_name[0].lower() + file_name[1:]
text = ' '.join(page_words)
text_capital = text.capitalize()
 
move_page_files(file_name, text_capital, store, text)
add_type(file_name, store)
add_routes(file_name, text_capital)
add_to_store(store)
print('gelukt')


sys.exit(0)
    