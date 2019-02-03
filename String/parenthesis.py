def my_para(whatever):
    my_list = [ ]
    for i in range ( len ( whatever ) ):
        # print(my_list)
        if whatever[ i ] == '[' or whatever[ i ] == '{' or whatever[ i ] == '(':
            my_list.append ( whatever[ i ] )
        if whatever[ i ] == ']':
            try:
                if my_list[ -1 ] != '[':
                    return 'not balanced'
                else:
                    my_list.pop ()
            except:
                return 'not balanced'
        if whatever[ i ] == '}':
            try:
                if my_list[ -1 ] != '{':
                    return 'not balanced'
                else:
                    my_list.pop ()

            except:
                return 'not balanced'
