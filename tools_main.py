def spliter_mail_hash(filename2, separator):
    mails = []
    hashes = []
    bad_lines = []
    with open(filename2, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue
            if separator not in line:
                bad_lines.append(line)
                continue

            mail, hash_value = line.split(separator, 1)
            mails.append(mail)
            hashes.append(hash_value)
    with open("mails.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(mails))
    with open("hashes.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(hashes))
    with open("bad_line.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(bad_lines))
    return 'файлы созданы'



def connector_mail_hash(file_mails, file_hashes, separator):
    with open(file_mails, "r", encoding="utf-8") as f:
        mails = [line.strip() for line in f if line.strip()]
    with open(file_hashes, "r", encoding="utf-8") as f:
        hashes = [line.strip() for line in f if line.strip()]
    with open('unite.txt', "w", encoding="utf-8") as f:
        for mail, hash_value in zip(mails, hashes):
            f.write(f"{mail}{separator}{hash_value}\n")
    return 'файл создан'

def fast_hex_tu_utf(hex_text):
    result = bytes.fromhex(hex_text).decode("utf-8")
    return result

def hex_tu_utf(filename):
    with open(filename, 'r', encoding="utf-8") as f, open('dehex.txt', 'w', encoding="utf-8") as fs:
        for i in f:
            hex = i.strip()
            result = bytes.fromhex(hex).decode("utf-8")
            fs.write(f'{result}\n')
    return 'файл создан'

def gluing_files(file_list, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for file in file_list:
            with open(file, 'r', encoding='utf-8') as g:
                data = g.read()
                f.write(f"{data}\n")
    return 'файл создан'

def breakdown_files(file_name, lines_count):
    count = 1
    current_lines = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            current_lines.append(line)
            if len(current_lines) == int(lines_count):
                outfile = f'file_{count}.txt'
                with open(outfile, 'w', encoding='utf-8') as out:
                    out.writelines(current_lines)
                current_lines = []
                count += 1
    if current_lines:
        output_name = f"part_{count}.txt"
        with open(output_name, "w", encoding="utf-8") as out:
            out.writelines(current_lines)
    return f"Создано файлов: {count}"



    



