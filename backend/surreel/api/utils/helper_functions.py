def format_validation_errors(e):
    error_messages = [str(error) for errors in e.detail.values() for error in errors]
    return error_messages
