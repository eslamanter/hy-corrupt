import os
import random

# 16.03.25
print("Korrupt 1.2 | Eslam Anter\n")

def corrupt_pdf(file_path, required_size):
    try:
        with open(file_path, 'rb+') as pdf_file:
            content = pdf_file.read()
            corrupted_content = list(content)
            random.shuffle(corrupted_content)
            corrupted_content = bytes(corrupted_content)
            if required_size > 0:
                if len(corrupted_content) > required_size:
                    corrupted_content = corrupted_content[:required_size]
                elif len(corrupted_content) < required_size:
                    padding_length = required_size - len(corrupted_content)
                    corrupted_content += bytes([random.randint(0, 255) for _ in range(padding_length)])
            pdf_file.seek(0)
            pdf_file.write(corrupted_content)
            pdf_file.truncate()
        print(f"{os.path.splitext(os.path.basename(file_path))[0]} [esistente] corrotto con successo.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")


def create_corrupted_pdfs():
    try:
        directory = input("Inserire il percorso della cartella dei PDF: ").strip()
        if not os.path.exists(directory):
            os.makedirs(directory)
        print("Inserire i nomi dei PDF da corrompere, ciascuno su una nuova riga:\n(eventualmente seguiti dalle dimensioni in KB, separate da una tabulazione)")
        input_data = []
        while True:
            line = input()
            if line:
                input_data.append(line)
            else:
                break
        for entry in input_data:
            parts = entry.split('\t')
            name = parts[0]
            if len(parts) > 1:
                if parts[1].strip().isnumeric():
                    input_kb = int(parts[1].strip())
                    if input_kb < 1048576:
                        required_size = input_kb * 1024
                    else:
                        required_size = 1073741824
                else:
                    required_size = random.randint(1000, 3000) * 1024
            else:
                required_size = random.randint(1000, 3000) * 1024
            output_path = os.path.join(directory, name.strip())
            if not output_path.endswith('.pdf'):
                output_path += '.pdf'
            if os.path.exists(output_path):
                corrupt_pdf(output_path, required_size)
            else:
                corrupted_data = bytes([random.randint(0, 255) for _ in range(required_size)])
                with open(output_path, 'wb') as output_pdf:
                    output_pdf.write(corrupted_data)
                print(f"{os.path.splitext(os.path.basename(output_path))[0]} [creato] corrotto con successo.")
        print("\nCorrompi responsabilmente!")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

create_corrupted_pdfs()
input()
