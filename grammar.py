# grammar.py

SCHTASKS_CMDLINE_GRAMMAR = {
    "<start>": ["<executable> <params_reordered>"],

    # 1. Recoding (Mã hóa lại) & Substitution (Thay thế)
    "<executable>": [
        "schtasks.exe",
        "%windir%\\system32\\schtasks.exe", # Dùng biến môi trường
        "C:\\Users\\Public\\updater.exe"     # Copy và đổi tên
    ],
    
    # 2. Reordering (Sắp xếp lại)
    "<params_reordered>": [
        "<create_verb> <tn_param> <tr_param> /sc ONSTART",
        "<tn_param> <tr_param> <create_verb> /sc ONSTART", # Hoán vị thứ tự
        "<tr_param> <create_verb> <tn_param> /sc ONSTART"
    ],

    # 3. Insertion (Chèn) & 4. Omission (Lược bỏ)/Substitution (Thay thế)
    "<create_verb>": [
        "/create",
        "/cr",          # Alias (Omission/Substitution)
        "'/create'",    # Insertion
        "\"/create\"",  # Insertion
        "/c^r^e^ate"    # Insertion
    ],
    
    "<tn_param>": ["/tn \"MyTask\""],
    "<tr_param>": ["/tr \"C:\\Temp\\payload.exe\""]
}