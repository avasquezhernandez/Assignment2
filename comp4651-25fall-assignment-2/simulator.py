def main():
    acc = 0
    with open("guest_program.txt", "r") as f:

        lines = f.readlines()
        for line in lines:
            adj_line = line.strip()
            if "add" in adj_line:
                ad= adj_line.split()
                acc += int(ad[1])
                print(f"[Guest] Executing: add {ad[1]}")
            elif "print" in adj_line:
                print("[Guest] Executing: print")
                print(f"Accumulator value: {acc}")
            elif "halt" in adj_line:
                print("[VMM] Trapped privileged instruction 'halt'. Halting guest.")

            elif "scan_disk" in adj_line:
                print("[VMM] Trapped privileged instruction 'scan_disk', emulating...")

if __name__ == "__main__":
    main()


