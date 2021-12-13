sentences = []


def add_sentence(regex, actor, state_add, state_remove):
    sentences.append({
        "regex": regex,
        "actor": actor,
        "state_add": state_add,
        "state_remove": state_remove
    })


# Seller dialog

add_sentence(
    r'(?P<hello1>(hi)|(hello))',
    "seller",
    ["start_introduction"],
    []
)

add_sentence(
    r'(?P<request_order1>what ((can I get you)|(would you like to have))\?)',
    "seller",
    ["end_introduction"],
    ["start_introduction"]
)

add_sentence(
    r'(?P<request_type1>(do you want a )?cup or cone\?)',
    "seller",
    ["end_introduction", "request_type"],
    ["start_introduction"]
)

add_sentence(
    r'(?P<request_size1>((great)|(alright), )?how many scoops\?)',
    "seller",
    ["end_introduction", "request_size"],
    ["start_introduction"]
)

add_sentence(
    r'((great)|(alright), )?which flavors would you like\?',
    "seller",
    ["end_introduction", "request_flavors"],
    ["start_introduction"]
)

add_sentence(
    r'(?P<request_topping1>any ((sprinkles)|(whipped cream)))\?',
    "seller",
    ["request_topping"],
    []
)

add_sentence(
    r'there is the ((?P<chocolate1>chocolate)|(?P<vanilla1>vanilla)|(?P<raspberry1>raspberry)|(?P<banana1>banana)) (and ((?P<chocolate2>chocolate)|(?P<vanilla2>vanilla)|(?P<raspberry2>raspberry)|(?P<banana2>banana)))?',
    "seller",
    ["pointing_to_item"],
    []
)

add_sentence(
    r'(?P<request_payment1>((great)|(alright), )?your total is \$. will you be paying cash or credit\?)',
    "seller",
    ["request_payment_type"],
    []
)


add_sentence(
    r'(thank you! )?(looks good, )?(okay.)? and here is your change!',
    "seller",
    ["pointint_to_change"],
    []
)

add_sentence(
    r'Aw thats so sweet! Enjoy your ice cream!',
    "seller",
    ["end_sale"],
    []
)


# Seller actions

add_sentence(
    r'\*((?P<he1>he)|(?P<she1>she) )extends the ((?P<cone1>cone)|(?P<cup1>cup)) to you\*',
    "seller-action",
    ["offers_icecream"],
    []
)

add_sentence(
    r'\*((?P<he1>he)|(?P<she1>she) )stares the void\*',
    "seller-action",
    ["void"],
    []
)


# Buyer dialog

add_sentence(
    r'(?P<hello1>(hi)|(hello))',
    "buyer",
    ["start_introduction"],
    []
)


add_sentence(
    r'Id like some ice cream( please)?!',
    "buyer",
    ["start_introduction"],
    []
)

add_sentence(
    r'I would like (to ((buy)|(have)))? ((some)|((?P<two_scoops1>two scoops)|(?P<one_scoop1>one scoop)) of)? ((?P<chocolate1>chocolate)|(?P<vanilla1>vanilla)|(?P<raspberry1>raspberry)|(?P<banana1>banana)) (and ((?P<chocolate2>chocolate)|(?P<vanilla2>vanilla)|(?P<raspberry2>raspberry)|(?P<banana2>banana)))? (in a ((?P<cone1>cone)|(?P<cup1>cup)))? (topped with some ((?P<sprinkles1>sprinkles)|(?P<whipped_cream1>whipped cream)))?(, please)?',
    "buyer",
    ["end_introduction", "make_order"],
    ["start_introduction"]
)

add_sentence(
    r'Im gona have a ((?P<one_scoop1>simple)|(?P<two_scoops1>double)) scoop',
    "buyer",
    ["end_introduction", "set_size"],
    ["start_introduction"]
)

add_sentence(
    r'I will have one scoop of ((?P<chocolate1>chocolate)|(?P<vanilla1>vanilla)|(?P<raspberry1>raspberry)|(?P<banana1>banana)) and the other scoop of ((?P<chocolate2>chocolate)|(?P<vanilla2>vanilla)|(?P<raspberry2>raspberry)|(?P<banana2>banana))(, please)',
    "buyer",
    ["end_introduction", "make_order"],
    ["start_introduction"]
)

add_sentence(
    r'((?P<chocolate1>chocolate)|(?P<vanilla1>vanilla)|(?P<raspberry1>raspberry)|(?P<banana1>banana)) (and ((?P<chocolate2>chocolate)|(?P<vanilla2>vanilla)|(?P<raspberry2>raspberry)|(?P<banana2>banana)))?(, please)',
    "buyer",
    ["end_introduction", "set_flavor"],
    ["start_introduction"]
)

add_sentence(
    r'((?P<chocolate1>chocolate)|(?P<vanilla1>vanilla)|(?P<raspberry1>raspberry)|(?P<banana1>banana)) (and ((?P<chocolate2>chocolate)|(?P<vanilla2>vanilla)|(?P<raspberry2>raspberry)|(?P<banana2>banana)))? in a ((?P<cone1>cone)|(?P<cup1>cup))(, please)',
    "buyer",
    ["end_introduction", "set_size", "set_flavor", "set_type"],
    ["start_introduction"]
)

add_sentence(
    r'in a ((?P<cone1>cone)|(?P<cup1>cup))(, please)',
    "buyer",
    ["set_type"],
    []
)

add_sentence(
    r'I just need one scoop',
    "buyer",
    ["set_size"],
    []
)

add_sentence(
    r'((?P<one_scoops1>one)|(?P<two_scoops1>two))(, please)',
    "buyer",
    ["set_size"],
    []
)

add_sentence(
    r'(?P<yes1>yes(, please))',
    "buyer",
    ["say_yes"],
    []
)

add_sentence(
    r'(?P<no1>no(, thanks))',
    "buyer",
    ["say_no"],
    []
)

add_sentence(
    r'((?P<cash1>cash)|(?P<credit1>credit)), please',
    "buyer",
    ["request_payment_type"],
    []
)

add_sentence(
    r'you can keep it, thanks',
    "buyer",
    ["tip"],
    []
)

# Buyer actions

add_sentence(
    r'\*you take the ((?P<cone1>cone)|(?P<cup1>cup))\*',
    "buyer-action",
    ["gets_icecream"],
    []
)

add_sentence(
    r'\*you stare the void\*',
    "buyer-action",
    ["void"],
    []
)
