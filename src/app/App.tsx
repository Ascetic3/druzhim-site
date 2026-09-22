import styles from './App.module.scss';

export function App() {
  return (
    <main className={styles.shell}>
      <div className={styles.status}>
        <p className={styles.eyebrow}>Техническая основа проекта</p>
        <h1>ДРУЖИМ</h1>
        <p>
          Среда разработки готова. Визуальная концепция, контент и секции будут
          определены на следующем этапе.
        </p>
      </div>
    </main>
  );
}
