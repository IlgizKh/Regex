import re
import csv


def create_list(file):
    with open(file, encoding="utf8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list
        # print(len(contacts_list[1]))


def phones(in_file, out_file):
    with open(in_file, encoding="utf8") as f:
        text = f.read()
    pattern_phone = r'(\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*(\w*\.*)\s*(\d*)\)*'
    fixed_phones = re.sub(pattern_phone, r'+7(\2)\3-\4-\5 \6\7', text)
    with open(out_file, 'w+', encoding="utf8") as f:
        text = f.write(fixed_phones)


def names(list):
    for person in list[1:]:
        name_person_0 = person[0].split(" ")
        name_person_1 = person[1].split(" ")
        if len(name_person_0) == 3:
            person[0] = name_person_0[0]
            person[1] = name_person_0[1]
            person[2] = name_person_0[2]
        elif len(name_person_0) == 2:
            person[0] = name_person_0[0]
            person[1] = name_person_0[1]
        elif len(name_person_1) == 2:
            person[1] = name_person_1[0]
            person[2] = name_person_1[1]
    return (list)


def merge(list):
    new_list = []
    for i, column in enumerate(list):
        first_name = column[0]
        last_name = column[1]
        for j, contact in enumerate(list):
            new_first_name = contact[0]
            new_last_name = contact[1]
            if first_name == new_first_name and last_name == new_last_name and contact != column:
                new_contact = [y if x == "" else x for x, y in zip(column, contact)]
                list[i] = new_contact
                list[j] = new_contact

    for contact in list:
        if contact not in new_list:
            new_list.append(contact)
    return new_list


def write_to_file(list):
    with open("phonebook.csv", "w", encoding="utf8") as f:
        datawriter = csv.writer(f, delimiter=',')

        ## Вместо contacts_list подставьте свой список:
        datawriter.writerows(list)


def main():
    phones(in_file="phonebook_raw.csv", out_file="fixed_phones.csv")
    contacts_list = create_list("fixed_phones.csv")
    list = names(contacts_list)
    dubl = merge(list)
    write_to_file(dubl)


if __name__ == '__main__':
    main()