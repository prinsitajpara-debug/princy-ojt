def to_upper(text):
    try:
        return text.upper()
    except AttributeError:
        return "Error: input must be a string"

def reverse(text):
    try:
        return text[::-1]
    except Exception as e:
        return f"Error: {str(e)}"