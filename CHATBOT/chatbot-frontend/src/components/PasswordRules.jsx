import { PASSWORD_RULES } from '../utils/passwordValidation';
import styles from '../pages/Auth.module.css';

export default function PasswordRules({ password }) {
  return (
    <ul className={styles.rulesList}>
      {PASSWORD_RULES.map((rule) => {
        const passed = password.length > 0 && rule.test(password);
        return (
          <li
            key={rule.id}
            className={`${styles.ruleItem} ${passed ? styles.rulePass : styles.ruleFail}`}
          >
            {rule.label}
          </li>
        );
      })}
    </ul>
  );
}
