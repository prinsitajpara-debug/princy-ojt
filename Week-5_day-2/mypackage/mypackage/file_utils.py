from .config import Config

def write_file(filename, content):
    try:
        with open(filename, "w", encoding=Config.DEFAULT_ENCODING) as f:
            f.write(content)
        return "File written successfully"
    except Exception as e:
        return f"Error writing file: {str(e)}"

def read_file(filename):
    try:
        with open(filename, "r", encoding=Config.DEFAULT_ENCODING) as f:
            return f.read()
    except FileNotFoundError:
        return "Error: file not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"