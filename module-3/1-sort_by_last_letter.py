

def sort_by_last_letter(strings):
    #note: A new function is created everytime sort_by_last_letter is run.
    def last_letter(s):
        return s[-1:]
    return sorted(strings, key=last_letter)