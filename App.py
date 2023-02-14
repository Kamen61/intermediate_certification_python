from Controller import Controller as Contr
from jsonModul import JsonModul as JM
from View import View as V


# '1 - создать заметку\n'
# '2 - прочитать заметку\n'
# '3 - редактировать заметку\n'
# '4 - удалить заметку\n'
# '5 - удалить все заметки\n'
# '6 - прочитать все заметки\n'
# '7 - выход\n'
def run():
    act = True
    con = Contr(JM('notes.json'), V())
    while (act):
        match con.menu():
            case 1:
                con.create_note()
            case 2:
                con.read_note()
            case 3:
                con.update_note()
            case 4:
                con.del_note()
            case 5:
                con.del_all_notes()
            case 6:
                con.print_all_notes()
            case 7:
                act = False
            case _:
                con.bad_menu_index()


run()