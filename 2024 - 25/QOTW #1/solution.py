decode_message = lambda message, shifts: [
    new_message := [],
    [
        [
            shift := shifts[index if index < len(shifts) else index % len(shifts)],
            new_char := ord(char) - shift,
            new_char := chr(
                ord("a") + (new_char % ord("z")) - 1
                if new_char > ord("z")
                else (
                    (ord("z") - (ord("a") % new_char) + 1)
                    if new_char < ord("a")
                    else new_char
                )
            ),
            new_message.append(new_char),
        ]
        for index, char in enumerate(message)
    ],
    print("".join(new_message)),
]

decode_message(
    "gdkkn",
    [1, 2, 3, 4, 5],
)
