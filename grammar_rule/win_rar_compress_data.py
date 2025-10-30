win_rar_compress_data_grammar = {
    "<start>": [
        "<executable> <params_reordered>"
    ],
    "<executable>": [
        "rar.exe",
        "RAR",
        "\"%ProgramFiles%\\WinRAR\\Rar.exe\""
    ],
    "<params_reordered>": [
        "<add_verb> <switches> <archive_name> <files_to_add>",
        "<add_verb> <archive_name> <switches> <files_to_add>"
    ],
    "<add_verb>": [
        "a",
        "A",
        "'a'",
        "\"a\""
    ],
    "<switches>": [
        "",
        "-r",
        "-pS3cr3t",
        "-hp -pS3cr3t",
        "-s"
    ],
    "<archive_name>": [
        "backup.rar",
        "\"%TEMP%\\archive.zip\""
    ],
    "<files_to_add>": [
        "C:\\Users\\Public\\Documents",
        "\"%USERPROFILE%\\Desktop\\*.docx\"",
        "@files_list.txt"
    ]
}