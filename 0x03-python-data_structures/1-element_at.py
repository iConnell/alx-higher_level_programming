#!/usr/bin/python3

if __name__ == "__main__":
    
    def element_at(my_list, idx):

        if idx > len(my_list) - 1 or idx < 0:
            return 'None'
        else:
            return my_list[idx]
