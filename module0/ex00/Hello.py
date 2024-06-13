''' Basic Operations on the Following Data Types '''

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = 'World!'                  # access elements with [] operator

ft_tuple = (ft_tuple[0], 'Austria!')   # immutable, so create a new tuple

ft_set.remove('tutu!')                 # remove the element tutu! from the set
ft_set.add('Vienna!')                  # add required element to the set

ft_dict["Hello"] = '42Vienna!'         # in map, access elements by key

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
