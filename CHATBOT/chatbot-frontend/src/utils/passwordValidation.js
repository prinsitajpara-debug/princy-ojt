const SPECIAL_CHAR_REGEX = /[!@#$%^&*(),.?":{}|<>_\-+=[\]\\;/'`~]/;

export const PASSWORD_RULES = [
  { id: 'length', label: 'At least 8 characters', test: (p) => p.length >= 8 },
  { id: 'upper', label: 'One uppercase letter (A-Z)', test: (p) => /[A-Z]/.test(p) },
  { id: 'lower', label: 'One lowercase letter (a-z)', test: (p) => /[a-z]/.test(p) },
  { id: 'number', label: 'One number (0-9)', test: (p) => /[0-9]/.test(p) },
  {
    id: 'special',
    label: 'One special character (!@#$...)',
    test: (p) => SPECIAL_CHAR_REGEX.test(p),
  },
  { id: 'nospace', label: 'No spaces', test: (p) => !/\s/.test(p) },
];

export function validateRegisterPassword(password) {
  if (!password) {
    return { valid: false, message: 'Password is required' };
  }

  if (password.length > 128) {
    return { valid: false, message: 'Password must be at most 128 characters' };
  }

  const failed = PASSWORD_RULES.filter((rule) => !rule.test(password));
  if (failed.length > 0) {
    return {
      valid: false,
      message: `Password must include: ${failed.map((r) => r.label.toLowerCase()).join(', ')}`,
    };
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

export function validatePasswordMatch(password, confirmPassword) {
  if (password !== confirmPassword) {
    return { valid: false, message: 'Passwords do not match' };
  }
  return { valid: true };
}
