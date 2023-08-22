from src.lib.managedb import ManageDB


def get_contacts():
    dt = ManageDB()

    return dt.write_contacts()
