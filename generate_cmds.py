# generate_cmds.py

from fuzzingbook.GrammarFuzzer import GrammarFuzzer
#from grammar import SCHTASKS_CMDLINE_GRAMMAR
#from grammar_rule.win_bcdedit_boot_conf_tamper import win_bcdedit_boot_conf_tamper_grammar as CMDLINE_GRAMMAR
from grammar_rule.win_cmd_assoc_execution import win_cmd_assoc_execution_grammar as CMDLINE_GRAMMAR
# --- CẤU HÌNH ---
ITERATIONS = 5000  # Số lượng lệnh muốn tạo
OUTPUT_FILE = "outputs/win_cmd_assoc_execution.txt"  # Tên tệp kết quả
# -----------------

class CommandLineGenerator:
    def __init__(self):
        # Khởi tạo fuzzer với ngữ pháp đã định nghĩa
        self.fuzzer = GrammarFuzzer(CMDLINE_GRAMMAR)
    
    def generate(self) -> str:
        # Tạo ra một dòng lệnh
        return self.fuzzer.fuzz()

def main():
    generator = CommandLineGenerator()
    unique_commands = set() # Dùng 'set' để tự động loại bỏ các lệnh trùng lặp

    print(f"--- Bắt đầu tạo {ITERATIONS} dòng lệnh để kiểm tra ---")

    for i in range(ITERATIONS):
        command_line = generator.generate()
        unique_commands.add(command_line)
        # In ra tiến trình để biết chương trình vẫn đang chạy
        if (i + 1) % 500 == 0:
            print(f"Đã tạo {i + 1}/{ITERATIONS} lệnh...")

    # Ghi các lệnh không trùng lặp ra file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # Sắp xếp lại danh sách để tệp kết quả dễ đọc hơn
        for cmd in sorted(list(unique_commands)):
            f.write(cmd + "\n")

    print(f"\n--- Hoàn tất! ---")
    print(f"Đã tạo ra {len(unique_commands)} dòng lệnh độc nhất.")
    print(f"Kết quả đã được lưu vào tệp: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()