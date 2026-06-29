import {
  validateRegisterPassword,
  validateLoginPassword,
  validatePasswordMatch,
} from '../utils/passwordValidation';

export function validateRegisterForm({ name, email, password, confirmPassword }) {
  const trimmedName = name.trim();
  const normalizedEmail = email.trim().toLowerCase();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!trimmedName) {
    return { valid: false, message: 'Full name is required' };
  }

  if (trimmedName.length < 2) {
    return { valid: false, message: 'Name must be at least 2 characters' };
  }

  if (!normalizedEmail) {
    return { valid: false, message: 'Email is required' };
  }

  if (!emailRegex.test(normalizedEmail)) {
    return { valid: false, message: 'Please enter a valid email address' };
  }

  const passwordCheck = validateRegisterPassword(password);
  if (!passwordCheck.valid) return passwordCheck;

  const matchCheck = validatePasswordMatch(password, confirmPassword);
  if (!matchCheck.valid) return matchCheck;

  return { valid: true };
}

export function validateLoginForm({ email, password }) {
  const normalizedEmail = email.trim().toLowerCase();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!normalizedEmail) {
    return { valid: false, message: 'Email is required' };
  }

  if (!emailRegex.test(normalizedEmail)) {
    return { valid: false, message: 'Please enter a valid email address' };
  }

  return validateLoginPassword(password);
}
