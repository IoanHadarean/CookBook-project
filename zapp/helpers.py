def get_results(data):
    """ Create list of dictionaries from the form data """
    # Create temporary list for filters storage
    filters = list()
    # Loop through each of the keys from the form
    for key in data:
        # Store the original key for later use
        value_key = key
        # Split the key by "-"
        key = key.split("-")
        # Take the first value from the list
        key = key[0]
        # Create temporary dictionary for storing the filter
        search_filter = dict()
        search_filter[key] = data[value_key]
        # Append the filter to the list of filters
        filters.append(search_filter)
        print(filters)
    return filters
        
        