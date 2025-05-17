# Kcorrupt

## 📄 Cos'è?
**Korrupt** è un tool creato per **corrompere file PDF** e **generare PDF corrotti** con dimensioni controllate.

---

## 🛠️ Come si usa?
All'avvio dell'applicazione, tramite la finestra dei comandi, ti verrà richiesto di:

1. **Specificare il percorso della cartella dei PDF**:
   - Può essere un percorso **relativo** o **assoluto**.
   - Esempi:
     - Percorso assoluto: `C:\0000_XXXX\PE\CONSEGNA\PDF\`
     - Percorso relativo: `PDF` (se avviato nella cartella "CONSEGNA").
   - Se la cartella non esiste, verrà **creata automaticamente**.

2. **Inserire i nomi dei file PDF**:
   - Specifica i nomi (senza estensione `.pdf`) dei file da generare o corrompere.
   - Puoi opzionalmente indicare la dimensione in KB (1 MB = 1024 KB), separata da una **tabulazione**.
   - Esempio:
     ```plaintext
     XXXX_GEN_PLA_03_A
     XXXX_TRA_SEZ_02_B
     XXXX_STR_REL_01_C    12864
     ```

3. **Risultati**:
   - Per ogni file, verrà mostrato un messaggio di conferma:
     ```plaintext
     XXXX_GEN_PLA_03_A [creato] corrotto con successo.
     XXXX_TRA_SEZ_02_B [esistente] corrotto con successo.
     XXXX_STR_REL_01_C [creato] corrotto con successo.
     ```

---

## ⚙️ Come funziona?
- **Creazione di PDF corrotti**:
  - Genera un contenuto casuale di byte nella cartella specificata.
  - Dimensioni:
    - Se specificate: usa la dimensione indicata.
    - Se non specificate: genera un file tra **1000 e 3000 KB**.

- **Corruzione di PDF esistenti**:
  - Mescola casualmente i byte del file mantenendo la dimensione originale.
  - Può anche adattare la dimensione del file alla richiesta (allungandolo o accorciandolo).

- **Gestione degli errori**:
  - In caso di input errato, il programma segnala il tipo di errore.

---

## 🚧 Limitazioni
- Per evitare problemi di memoria, la dimensione massima per ogni file è fissata a **1 GB** (1048576 KB).

---

## ⚠️ Avvertimento!
- **Attenzione ai file esistenti**: i PDF con nomi corrispondenti verranno **danneggiati permanentemente**.
- Il processo è **irreversibile**: i file corrotti non possono essere recuperati.

---

## 📌 Nota legale
L'autore **non si assume alcuna responsabilità** per eventuali danni causati dall'uso del codice. L'utente è responsabile di verificare la conformità alle leggi locali.

---

### 16/03/2025 | **Eslam Anter**
