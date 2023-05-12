def first_second(my_list):
    # TODO
    ordered = []
    for element in my_list:
        if element not in ordered:
            ordered.append(element)
    ordered.sort(reverse=True)
    return (ordered[0], ordered[1])
