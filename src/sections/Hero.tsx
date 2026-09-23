import { Action } from '../components/Action';
import styles from './Hero.module.scss';

export function Hero() {
  return (
    <section id="top" className={styles.hero} aria-labelledby="hero-title">
      <div className={styles.inner}>
        <h1 id="hero-title" className={styles.heading}>
          <span>У каждого — свой путь.</span> <span>Рядом — ДРУЖИМ.</span>
        </h1>
        <p className={styles.copy}>
          Помогаем детям, молодежи и семьям развивать навыки, находить поддержку
          и становиться самостоятельнее.
        </p>
        <Action href="#season" className={styles.action}>
          Узнать о группах
        </Action>
      </div>
    </section>
  );
}
