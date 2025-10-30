win_cmd_path_traversal_grammar = {
    "<start>": [
        "<executable> <flag> <command_with_traversal>"
    ],
    "<executable>": [
        "cmd.exe",
        "CMD.EXE",
        "%COMSPEC%",
        "%windir%\\system32\\cmd.exe"
    ],
    "<flag>": [
        "/c",
        "/C",
        "/k",
        "/K",
        "/r",
        "/R"
    ],
    "<command_with_traversal>": [
        "dir <traversal>",
        "echo test <traversal>",
        "type C:\\Users\\Public<traversal>\\windows\\win.ini"
    ],
    "<traversal>": [
        "\\..\\..",
        "/..\\..",
        "\\..\\../",
        "/..^/..",
        "\"/..\\..\""
    ]
}