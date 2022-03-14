# Using std library from this file isn`t recomended,
# but if you forgot to put std.bino to folder with binarian executable
# it will be used

# This file can update not as frequently as std.bino in github repo

std_lib_code = \
"""
func xor : val1 val2 (
    return {not {or {and val1 val2} {not {or val1 val2}}}}
)

func add : num1 num2 (
    // Actually I created this language just to write this function. 
    set carry 0
    set ret []

    for dig {zip num1 num2} (
        set a {index dig [0]}
        set b {index dig [1]}

        set sum {xor {xor a b} carry}
        set carry {or {and carry {xor a b}} {and a b}}

        append ret sum
    )

    if carry (
        append ret carry
    )

    return ret
)

func half-subt : a b (
    set dif {xor a b}
    set borrow {and {not a} b}

    return [dif borrow]
)

func subt : num1 num2 (
    // Please just not use this if first number is smaller than second one.
    // It can`t deal with negative numbers as everything in this language

    set borrow 0
    set ret []

    for dig {zip num1 num2} (
        set a {index dig [0]}
        set b {index dig [1]}

        set half {half-subt a b}
        set half2 {half-subt {index half [0]} borrow}

        set dif {index half2 [0]}
        set borrow {or {index half [1]} {index half2 [1]}}

        append ret dif
    )

    return ret
)

func eq : num1 num2 (
    for dig {zip num1 num2} (
        set a {index dig [0]}
        set b {index dig [1]}

        if {xor a b} (
            return 0
        )
    )

    return 1
)

func sum : list (
    set sum [0]
    for i list (
        set sum {add sum i}
    )

    return sum
)
"""