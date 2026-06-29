const SPECIAL_CHAR_REGEX = /[!@#$%^&*(),.?":{}|<>_\-+=[\]\\;/'`~]/;

export function validateRegisterPassword(password) {
  if (!password) {
    return { valid: false, message: 'Password is required' };
  }

  if (password.length < 8) {
    return { valid: false, message: 'Password must be at least 8 characters' };
  }

  if (password.length > 128) {
    return { valid: false, message: 'Password must be at most 128 characters' };
  }

  if (!/[A-Z]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one uppercase letter' };
  }

  if (!/[a-z]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one lowercase letter' };
  }

  if (!/[0-9]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one number' };
  }

  if (!SPECIAL_CHAR_REGEX.test(password)) {
    return {
      valid: false,
      message: 'Password must contain at least one special character',
    };
  }

  if (/\s/.test(password)) {
    return { valid: false, message: 'Password must not contain spaces' };
  }

  return { valid: true };
}

export function validateLoginPassword(password) {
  if (!password) {
    return { valid: false, message: 'Password is required' };
  }

  if (password.length < 6) {
    return { valid: false, message: 'Password must be at least 6 characters' };
  }

  if (password.length > 128) {
    return { valid: false, message: 'Password must be at most 128 characters' };
  }

  return { valid: true };
}
