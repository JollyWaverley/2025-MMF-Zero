# function here
def generate_statement(statement, decoration, lines):
    """will make the headings (3 lines), subhaedings(2 lines) and emphasised text / mini-heading (1 line).
       Only use emoji for single line statements"""

    middle=(f"{decoration * 3} {statement} {decoration * 3}")
    top_bottem = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottem)

    else:
        print(top_bottem)
        print(middle)
        print(top_bottem)


# Main routine here
#generate_statement("programing is fun", "=",3)
print()
#generate_statement("programing is still fun" , "-",2)
print()
generate_statement("Instuctions","⚠️",1)