Transitions explanations:

    Copying Y to X:
        "cpy_0",
        "cpy_1",
        "cpy_2",
        "cpy_3",
        "clear_Y_after_cpy", -> clear B on Y and then HALT

    Looking for match between series in X and Y:
        "match_1_a",
        "match_1_b",
        "match_1_c",
        "match_1_d",
        "match_2_a",
        "match_2_b",
        "yes_match",
        "no_match",
        "clear_after_match",
    
    Sub Y to Z:
        "sub",
        "move_far_right",
        Erase the first term after Z:
            "shift_left",
            "shift_left_1",
            "shift_left_0",
            "move_left_to_z",
        "insert",
        Mark term in x to "count" the number of 1 to insert:
            "insert_move_left_to_x",
            "insert_mark_x",
            "insert_move_right_to_z",
        Add one term after Z:
            "insert_z",
            "shift_right_1",
            "shift_right_0",

    Z11010110 .

    Z11010110 0.

    Z1101011 0.

    Z1101010 1.
